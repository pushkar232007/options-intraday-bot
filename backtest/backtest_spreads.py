"""
Backtest engine for credit-spread (iron condor) strategies - same data/indicator
pipeline as backtest.py, but P&L comes from selling a condor (net credit) and buying
it back later, instead of buying a single naked option.

Usage: python3 backtest_spreads.py --strategy strategy_spread_v1 [--days-to-expiry 3] [--risk-pct 5] [--interval 1h]
"""
import argparse
import importlib
import statistics

from fetch_data import load_cached
from indicators import ema_series, rsi_series, atr_series, adx_series, group_by_day
from bs_pricer import STRIKE_STEP, LOT_SIZE
from iron_condor import build_condor, condor_net_value
from backtest import (INSTRUMENTS, STARTING_CAPITAL, build_day_index, vix_close_at,
                       ist_date, build_daily_trend_lookup)

import inspect


def run(strategy_name, days_to_expiry, risk_pct, daily_loss_cap_pct, interval="1h"):
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
        per_instr[name] = dict(days=days, day_start_idx=day_start_idx, ind=ind, vix_days=vix_days)

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

            take = strategy.decide_entry(day_candles, 1, info["ind"], global_start + 1)
            if not take:
                continue

            spot_entry = day_candles[1]["c"]
            strikes = build_condor(spot_entry, step, strategy.SHORT_OFFSET_STEPS,
                                    strategy.LONG_OFFSET_STEPS)
            iv = vix_close_at(info["vix_days"], day_pos, 1)
            entry_credit = condor_net_value(strikes, spot_entry, days_to_expiry, iv)
            if entry_credit <= 0:
                continue

            max_loss_per_unit = (strategy.LONG_OFFSET_STEPS - strategy.SHORT_OFFSET_STEPS) * step - entry_credit
            if max_loss_per_unit <= 0:
                continue
            risk_amount = capital * (risk_pct / 100.0)
            qty_lots = int(risk_amount / max(max_loss_per_unit * lot, 1))
            if qty_lots < 1:
                continue

            exit_value = entry_credit
            exit_reason = "EOD"
            remaining_candles = day_candles[2:]
            elapsed_fraction_per_candle = 1.0 / max(len(day_candles), 1)

            for j, candle in enumerate(remaining_candles, start=2):
                spot_now = candle["c"]
                iv_now = vix_close_at(info["vix_days"], day_pos, j)
                dte_now = max(days_to_expiry - j * elapsed_fraction_per_candle, 0.05)
                value_now = condor_net_value(strikes, spot_now, dte_now, iv_now)
                reason = strategy.exit_check(entry_credit, value_now)
                exit_value = value_now
                if reason:
                    exit_reason = reason
                    break

            pnl = (entry_credit - exit_value) * qty_lots * lot
            capital += pnl
            day_pnl += pnl
            trades.append(dict(day=day_pos, instrument=name, entry_credit=entry_credit,
                                exit_value=exit_value, qty_lots=qty_lots, pnl=pnl, reason=exit_reason))

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
    ap.add_argument("--strategy", default="strategy_spread_v1")
    ap.add_argument("--days-to-expiry", type=float, default=3.0)
    ap.add_argument("--risk-pct", type=float, default=5.0)
    ap.add_argument("--daily-loss-cap-pct", type=float, default=10.0)
    ap.add_argument("--interval", default="1h")
    ap.add_argument("--dump", action="store_true")
    args = ap.parse_args()

    result = run(args.strategy, args.days_to_expiry, args.risk_pct, args.daily_loss_cap_pct,
                 interval=args.interval)
    summarize(result)
    if args.dump:
        print()
        for t in result["trades"]:
            print(t)
