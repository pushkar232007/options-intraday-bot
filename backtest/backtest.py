"""
Backtest engine - loads cached 15m underlying + India VIX data, walks forward day by
day across NIFTY/BANKNIFTY/SENSEX together sharing one capital pool and one daily-loss
circuit breaker (mirrors how the live bot will actually run), and simulates option
trades via Black-Scholes (see bs_pricer.py) using a pluggable strategy module.

Usage: python3 backtest.py --strategy strategy_v1 [--days-to-expiry 2] [--risk-pct 5] [--daily-loss-cap-pct 10]
"""
import argparse
import importlib
import inspect
import statistics
import time

from fetch_data import load_cached
from indicators import ema_series, rsi_series, atr_series, adx_series, group_by_day
from bs_pricer import bs_price, atm_strike, STRIKE_STEP, LOT_SIZE

INSTRUMENTS = ["NIFTY", "BANKNIFTY", "SENSEX"]
STARTING_CAPITAL = 100_000.0
IST_OFFSET = 19800


def ist_date(ts):
    return time.gmtime(ts + IST_OFFSET).tm_yday, time.gmtime(ts + IST_OFFSET).tm_year


def build_daily_trend_lookup(daily_candles):
    """Maps each IST (year, yday) -> trend ('up'/'down'/None) using *yesterday's* daily
    close vs daily EMA20, so there's no lookahead into today's still-unknown close."""
    closes = [c["c"] for c in daily_candles]
    ema20 = ema_series(closes, 20)
    dates = [ist_date(c["t"]) for c in daily_candles]
    lookup = {}
    for i in range(1, len(daily_candles)):
        prev_close, prev_ema = closes[i - 1], ema20[i - 1]
        trend = None
        if prev_ema is not None:
            trend = "up" if prev_close > prev_ema else "down"
        lookup[dates[i]] = trend
    return lookup


def build_day_index(candles):
    """Returns (days: list of per-day candle lists, day_key -> global_start_idx)."""
    days = group_by_day(candles)
    day_start_idx = []
    idx = 0
    for d in days:
        day_start_idx.append(idx)
        idx += len(d)
    return days, day_start_idx


def vix_close_at(vix_days, day_pos, idx_in_day, fallback=15.0):
    if day_pos >= len(vix_days):
        return fallback
    day = vix_days[day_pos]
    idx_in_day = min(idx_in_day, len(day) - 1)
    return day[idx_in_day]["c"]


def run(strategy_name, days_to_expiry, risk_pct, daily_loss_cap_pct, interval="15m", verbose=False):
    strategy = importlib.import_module(strategy_name)

    per_instr = {}
    for name in INSTRUMENTS:
        candles = load_cached(name, interval)
        closes = [c["c"] for c in candles]
        highs = [c["h"] for c in candles]
        lows = [c["l"] for c in candles]
        ema9 = ema_series(closes, 9)
        ema21 = ema_series(closes, 21)
        rsi14 = rsi_series(closes, 14)
        atr14 = atr_series(highs, lows, closes, 14)
        adx14 = adx_series(highs, lows, closes, 14)
        days, day_start_idx = build_day_index(candles)
        vix_candles = load_cached("INDIAVIX", interval)
        vix_days, _ = build_day_index(vix_candles)
        ind = dict(ema9=ema9, ema21=ema21, rsi14=rsi14, atr14=atr14, adx14=adx14)
        daily_candles = load_cached(name, "1d")
        daily_trend_lookup = build_daily_trend_lookup(daily_candles)
        per_instr[name] = dict(days=days, day_start_idx=day_start_idx,
                                ind=ind, vix_days=vix_days, daily_trend_lookup=daily_trend_lookup)

    accepts_daily_trend = "daily_trend" in inspect.signature(strategy.decide_entry).parameters

    num_days = min(len(per_instr[n]["days"]) for n in INSTRUMENTS)

    capital = STARTING_CAPITAL
    trades = []
    equity_curve = [capital]
    circuit_breaker_days = 0

    for day_pos in range(num_days):
        day_start_capital = capital
        day_pnl = 0.0
        breaker_tripped = False

        for name in INSTRUMENTS:
            info = per_instr[name]
            day_candles = info["days"][day_pos]
            if len(day_candles) < 3:
                continue
            global_start = info["day_start_idx"][day_pos]
            step = STRIKE_STEP[name]
            lot = LOT_SIZE[name]

            if breaker_tripped:
                continue

            today_date = ist_date(day_candles[0]["t"]) if accepts_daily_trend else None
            daily_trend = info["daily_trend_lookup"].get(today_date) if accepts_daily_trend else None

            # Scan every candle of the day (not just the open) - leave at least one
            # candle after entry to monitor for exit.
            signal = None
            entry_idx_in_day = None
            for idx in range(1, len(day_candles) - 1):
                if accepts_daily_trend:
                    candidate = strategy.decide_entry(day_candles, idx, info["ind"],
                                                       global_start + idx, daily_trend=daily_trend)
                else:
                    candidate = strategy.decide_entry(day_candles, idx, info["ind"], global_start + idx)
                if candidate is not None:
                    signal = candidate
                    entry_idx_in_day = idx
                    break
            if signal is None:
                continue

            spot_entry = day_candles[entry_idx_in_day]["c"]
            strike = atm_strike(spot_entry, step)
            iv = vix_close_at(info["vix_days"], day_pos, entry_idx_in_day)
            entry_premium = bs_price(spot_entry, strike, days_to_expiry, iv, signal)

            risk_amount = capital * (risk_pct / 100.0)
            sl_amount_per_unit = entry_premium * strategy.SL_PCT
            max_qty_lots_by_risk = int(risk_amount / max(sl_amount_per_unit * lot, 1))
            if max_qty_lots_by_risk < 1:
                continue  # capital too small to take even 1 lot within risk budget
            qty_lots = max_qty_lots_by_risk

            peak_premium = entry_premium
            exit_premium = entry_premium
            exit_reason = "EOD"
            remaining_candles = day_candles[entry_idx_in_day + 1:]
            elapsed_fraction_per_candle = 1.0 / max(len(day_candles), 1)

            for j, candle in enumerate(remaining_candles, start=entry_idx_in_day + 1):
                spot_now = candle["c"]
                iv_now = vix_close_at(info["vix_days"], day_pos, j)
                dte_now = max(days_to_expiry - j * elapsed_fraction_per_candle, 0.05)
                premium_now = bs_price(spot_now, strike, dte_now, iv_now, signal)
                peak_premium = max(peak_premium, premium_now)
                reason = strategy.exit_check(entry_premium, premium_now, peak_premium)
                if reason:
                    exit_premium = premium_now
                    exit_reason = reason
                    break
                exit_premium = premium_now  # keep updating in case we run to EOD

            pnl = (exit_premium - entry_premium) * qty_lots * lot
            capital += pnl
            day_pnl += pnl
            trades.append(dict(day=day_pos, instrument=name, signal=signal, strike=strike,
                                entry=entry_premium, exit=exit_premium, qty_lots=qty_lots,
                                pnl=pnl, reason=exit_reason))

            if day_pnl <= -(day_start_capital * (daily_loss_cap_pct / 100.0)):
                breaker_tripped = True

        if breaker_tripped:
            circuit_breaker_days += 1
        equity_curve.append(capital)

    return dict(trades=trades, final_capital=capital, equity_curve=equity_curve,
                circuit_breaker_days=circuit_breaker_days, num_days=num_days)


def summarize(result):
    trades = result["trades"]
    n = len(trades)
    wins = [t for t in trades if t["pnl"] > 0]
    losses = [t for t in trades if t["pnl"] <= 0]
    total_pnl = sum(t["pnl"] for t in trades)
    equity = result["equity_curve"]
    peak = equity[0]
    max_dd = 0.0
    for e in equity:
        peak = max(peak, e)
        max_dd = max(max_dd, (peak - e) / peak)

    print(f"Days simulated: {result['num_days']}")
    print(f"Trades taken:   {n}")
    if n:
        print(f"Win rate:       {len(wins) / n * 100:.1f}%  ({len(wins)}W / {len(losses)}L)")
        print(f"Avg win:        {statistics.mean([t['pnl'] for t in wins]):.0f}" if wins else "Avg win: n/a")
        print(f"Avg loss:       {statistics.mean([t['pnl'] for t in losses]):.0f}" if losses else "Avg loss: n/a")
    print(f"Total P&L:      {total_pnl:.0f}")
    print(f"Final capital:  {result['final_capital']:.0f}  (started {STARTING_CAPITAL:.0f})")
    print(f"Max drawdown:   {max_dd * 100:.1f}%")
    print(f"Circuit-breaker tripped on {result['circuit_breaker_days']} of {result['num_days']} days")
    by_instr = {}
    for t in trades:
        by_instr.setdefault(t["instrument"], []).append(t["pnl"])
    for name, pnls in by_instr.items():
        print(f"  {name}: {len(pnls)} trades, P&L {sum(pnls):.0f}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--strategy", default="strategy_v1")
    ap.add_argument("--days-to-expiry", type=float, default=2.0)
    ap.add_argument("--risk-pct", type=float, default=5.0)
    ap.add_argument("--daily-loss-cap-pct", type=float, default=10.0)
    ap.add_argument("--interval", default="15m")
    ap.add_argument("--dump", action="store_true")
    args = ap.parse_args()

    result = run(args.strategy, args.days_to_expiry, args.risk_pct, args.daily_loss_cap_pct,
                 interval=args.interval)
    summarize(result)
    if args.dump:
        print()
        for t in result["trades"]:
            print(t)
