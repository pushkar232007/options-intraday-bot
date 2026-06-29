"""
BankNifty-specific backtest using its REAL monthly expiry calendar, instead of the fixed
1-6 day sweep used for NIFTY/SENSEX (which assumed weekly expiries - wrong for BankNifty,
see memory/signals-learnings.md). Days-to-expiry varies naturally day-to-day within the
month here, the way it actually will live, rather than being a fixed backtest parameter.

BankNifty's monthly expiry weekday changed multiple times during the 2-year backtest
window (Wednesday -> Thursday -> Monday -> Tuesday, per NSE/SEBI changes through 2025) -
modeling all of that accurately is more trouble than it's worth. This restricts the test
to since 2025-09-01, when SEBI's standardization made "last Tuesday of the month" the
stable, current convention - shorter sample (~9-10 months) than the NIFTY/SENSEX test,
but it's the only period whose expiry calendar actually matches what we'll trade going
forward. Don't extend this further back without re-deriving the expiry weekday changes.

Usage: python3 backtest_banknifty_monthly.py [--strategy strategy_spread_v1] [--risk-pct 5]
"""
import argparse
import calendar
import datetime
import importlib

from fetch_data import load_cached
from indicators import ema_series, rsi_series, atr_series, adx_series, group_by_day
from bs_pricer import STRIKE_STEP, LOT_SIZE
from iron_condor import build_condor, condor_net_value
from backtest import STARTING_CAPITAL, build_day_index, vix_close_at, ist_date

WINDOW_START = datetime.date(2025, 9, 1)  # stable "last Tuesday" convention starts here
IST_OFFSET = 19800


def last_tuesday(year, month):
    last_day = calendar.monthrange(year, month)[1]
    d = datetime.date(year, month, last_day)
    while d.weekday() != 1:  # Tuesday=1
        d -= datetime.timedelta(days=1)
    return d


def build_expiry_calendar(start_date, end_date):
    expiries = []
    y, m = start_date.year, start_date.month
    while True:
        expiries.append(last_tuesday(y, m))
        if y == end_date.year and m == end_date.month:
            break
        m += 1
        if m > 12:
            m = 1
            y += 1
    return sorted(expiries)


def dte_for_date(d, expiry_calendar):
    for e in expiry_calendar:
        if e >= d:
            return (e - d).days
    return None  # past the last known expiry in our calendar


def run(strategy_name, risk_pct, daily_loss_cap_pct, interval="1h", max_dte=None):
    strategy = importlib.import_module(strategy_name)

    candles = load_cached("BANKNIFTY", interval)
    candles = [c for c in candles
               if datetime.date.fromtimestamp(c["t"] + IST_OFFSET) >= WINDOW_START]
    closes = [c["c"] for c in candles]
    highs = [c["h"] for c in candles]
    lows = [c["l"] for c in candles]
    ema9 = ema_series(closes, 9)
    ema21 = ema_series(closes, 21)
    rsi14 = rsi_series(closes, 14)
    atr14 = atr_series(highs, lows, closes, 14)
    adx14 = adx_series(highs, lows, closes, 14)
    ind = dict(ema9=ema9, ema21=ema21, rsi14=rsi14, atr14=atr14, adx14=adx14)
    days, day_start_idx = build_day_index(candles)

    vix_candles = load_cached("INDIAVIX", interval)
    vix_candles = [c for c in vix_candles
                    if datetime.date.fromtimestamp(c["t"] + IST_OFFSET) >= WINDOW_START]
    vix_days, _ = build_day_index(vix_candles)

    last_day_date = datetime.date.fromtimestamp(candles[-1]["t"] + IST_OFFSET)
    expiry_calendar = build_expiry_calendar(WINDOW_START, last_day_date)

    step = STRIKE_STEP["BANKNIFTY"]
    lot = LOT_SIZE["BANKNIFTY"]
    capital = STARTING_CAPITAL
    trades = []
    equity_curve = [capital]
    circuit_breaker_days = 0
    skipped_no_expiry = 0

    for day_pos, day_candles in enumerate(days):
        if len(day_candles) < 3 or day_pos >= len(vix_days):
            continue
        day_date = datetime.date.fromtimestamp(day_candles[0]["t"] + IST_OFFSET)
        dte_today = dte_for_date(day_date, expiry_calendar)
        if dte_today is None:
            skipped_no_expiry += 1
            continue
        if dte_today == 0:
            dte_today = 0.25  # expiry day itself - floor, same convention as bs_pricer
        if max_dte is not None and dte_today > max_dte:
            equity_curve.append(capital)
            continue

        global_start = day_start_idx[day_pos]
        day_start_capital = capital
        day_pnl = 0.0

        take = strategy.decide_entry(day_candles, 1, ind, global_start + 1)
        if not take:
            equity_curve.append(capital)
            continue

        spot_entry = day_candles[1]["c"]
        strikes = build_condor(spot_entry, step, strategy.SHORT_OFFSET_STEPS, strategy.LONG_OFFSET_STEPS)
        iv = vix_close_at(vix_days, day_pos, 1)
        entry_credit = condor_net_value(strikes, spot_entry, dte_today, iv)
        if entry_credit <= 0:
            equity_curve.append(capital)
            continue

        max_loss_per_unit = (strategy.LONG_OFFSET_STEPS - strategy.SHORT_OFFSET_STEPS) * step - entry_credit
        if max_loss_per_unit <= 0:
            equity_curve.append(capital)
            continue
        risk_amount = capital * (risk_pct / 100.0)
        qty_lots = int(risk_amount / max(max_loss_per_unit * lot, 1))
        if qty_lots < 1:
            equity_curve.append(capital)
            continue

        exit_value = entry_credit
        exit_reason = "EOD"
        remaining_candles = day_candles[2:]
        elapsed_fraction_per_candle = 1.0 / max(len(day_candles), 1)

        for j, candle in enumerate(remaining_candles, start=2):
            spot_now = candle["c"]
            iv_now = vix_close_at(vix_days, day_pos, j)
            dte_now = max(dte_today - j * elapsed_fraction_per_candle, 0.05)
            value_now = condor_net_value(strikes, spot_now, dte_now, iv_now)
            reason = strategy.exit_check(entry_credit, value_now)
            exit_value = value_now
            if reason:
                exit_reason = reason
                break

        pnl = (entry_credit - exit_value) * qty_lots * lot
        capital += pnl
        day_pnl += pnl
        trades.append(dict(day=day_pos, date=str(day_date), dte_at_entry=round(dte_today, 1),
                            entry_credit=entry_credit, exit_value=exit_value, qty_lots=qty_lots,
                            pnl=pnl, reason=exit_reason))

        if day_pnl <= -(day_start_capital * (daily_loss_cap_pct / 100.0)):
            circuit_breaker_days += 1
        equity_curve.append(capital)

    return dict(trades=trades, final_capital=capital, equity_curve=equity_curve,
                circuit_breaker_days=circuit_breaker_days, num_days=len(days),
                skipped_no_expiry=skipped_no_expiry)


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

    print(f"Days simulated: {result['num_days']} (skipped {result['skipped_no_expiry']} with no known expiry ahead)")
    print(f"Trades taken:   {n}")
    if n:
        print(f"Win rate:       {len(wins) / n * 100:.1f}%  ({len(wins)}W / {len(losses)}L)")
        dtes = [t["dte_at_entry"] for t in trades]
        print(f"DTE at entry:   min {min(dtes)}, max {max(dtes)}, avg {sum(dtes)/len(dtes):.1f}")
    print(f"Total P&L:      {total_pnl:.0f}")
    print(f"Final capital:  {result['final_capital']:.0f}  (started {STARTING_CAPITAL:.0f})")
    print(f"Max drawdown:   {max_dd * 100:.1f}%")
    print(f"Circuit-breaker tripped on {result['circuit_breaker_days']} days")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--strategy", default="strategy_spread_v1")
    ap.add_argument("--risk-pct", type=float, default=5.0)
    ap.add_argument("--daily-loss-cap-pct", type=float, default=10.0)
    ap.add_argument("--interval", default="1h")
    ap.add_argument("--max-dte", type=float, default=None)
    ap.add_argument("--dump", action="store_true")
    args = ap.parse_args()

    result = run(args.strategy, args.risk_pct, args.daily_loss_cap_pct, interval=args.interval,
                 max_dte=args.max_dte)
    summarize(result)
    if args.dump:
        print()
        for t in result["trades"]:
            print(t)
