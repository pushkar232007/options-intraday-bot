"""
Parameter sweep: tests every combination of SL multiple and profit target
on both the index backtest (Black-Scholes) and stock backtest (real Bhavcopy prices).

Answers the question: is the current 2x SL / 50% target optimal, or does
a tighter SL (better R:R) actually produce better results?

Usage:
  python3 sweep_params.py           # both index + stock
  python3 sweep_params.py --index   # index only (faster, no Bhavcopy needed)
  python3 sweep_params.py --stocks  # stock only
"""
import argparse
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

SL_MULTIPLES      = [1.0, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0]
PROFIT_TARGETS    = [0.25, 0.33, 0.50, 0.75]
CURRENT_SL        = 2.0
CURRENT_TARGET    = 0.50


# ── Index sweep (patches strategy module constants) ───────────────────────────

def _run_index(sl_multiple, profit_target_pct):
    import strategy_spread_v1 as strat
    strat.SL_MULTIPLE = sl_multiple
    strat.PROFIT_TARGET_PCT = profit_target_pct

    import backtest_spreads as bs
    result = bs.run("strategy_spread_v1", days_to_expiry=3,
                    risk_pct=5.0, daily_loss_cap_pct=999.0)  # cap=999 = effectively disabled
    trades = result["trades"]
    n = len(trades)
    if n == 0:
        return None
    wins = sum(1 for t in trades if t["pnl"] > 0)
    total_pnl = sum(t["pnl"] for t in trades)
    equity = result["equity_curve"]
    peak = equity[0]
    max_dd = 0.0
    for e in equity:
        peak = max(peak, e)
        max_dd = max(max_dd, (peak - e) / peak)
    return {"n": n, "wr": wins / n * 100, "pnl": total_pnl, "dd": max_dd * 100}


def sweep_index():
    print("\n" + "=" * 72)
    print("  INDEX BACKTEST SWEEP (Black-Scholes, NIFTY/BANKNIFTY/SENSEX)")
    print("=" * 72)
    _print_header()

    for sl in SL_MULTIPLES:
        for pt in PROFIT_TARGETS:
            r = _run_index(sl, pt)
            if r:
                _print_row(sl, pt, r["n"], r["wr"], r["pnl"], r["dd"])


# ── Stock sweep ───────────────────────────────────────────────────────────────

def _run_stocks(sl_multiple, profit_target_pct):
    import backtest_stocks as bst
    result = bst.run(
        adx_threshold=18.0, min_dte=2, max_dte=7, min_oi=1000,
        profit_target_pct=profit_target_pct,
        sl_multiple=sl_multiple,
        verbose=False,
    )
    trades = result["trades"]
    n = len(trades)
    if n == 0:
        return None
    wins = sum(1 for t in trades if t["pnl_per_share"] > 0)
    total_pnl = sum(t["pnl_per_share"] for t in trades)
    return {"n": n, "wr": wins / n * 100, "pnl": total_pnl, "dd": 0.0}


def sweep_stocks():
    print("\n" + "=" * 72)
    print("  STOCK BACKTEST SWEEP (Real Bhavcopy prices, Nifty 50 F&O)")
    print("=" * 72)
    print("  NOTE: P&L is per-share sum across all trades (lot-size agnostic)")
    _print_header()

    for sl in SL_MULTIPLES:
        for pt in PROFIT_TARGETS:
            r = _run_stocks(sl, pt)
            if r:
                _print_row(sl, pt, r["n"], r["wr"], r["pnl"], r["dd"])


# ── Formatting ────────────────────────────────────────────────────────────────

def _print_header():
    print(f"\n  {'SL':>6}  {'Target':>7}  {'Trades':>7}  "
          f"{'Win Rate':>9}  {'Total P&L':>11}  {'Max DD':>7}  {'Note'}")
    print(f"  {'-'*6}  {'-'*7}  {'-'*7}  {'-'*9}  {'-'*11}  {'-'*7}  {'-'*10}")


def _print_row(sl, pt, n, wr, pnl, dd):
    is_current = (sl == CURRENT_SL and abs(pt - CURRENT_TARGET) < 0.01)
    tag = "← CURRENT" if is_current else ""
    dd_str = f"{dd:.1f}%" if dd > 0 else "  n/a"
    print(f"  {sl:>5.2f}x  {pt*100:>6.0f}%  {n:>7d}  "
          f"{wr:>8.1f}%  {pnl:>+11.1f}  {dd_str:>7}  {tag}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Sweep SL/target parameters")
    ap.add_argument("--index",  action="store_true", help="Index sweep only")
    ap.add_argument("--stocks", action="store_true", help="Stock sweep only")
    args = ap.parse_args()

    run_index  = args.index  or (not args.index and not args.stocks)
    run_stocks = args.stocks or (not args.index and not args.stocks)

    print("Running parameter sweep — this takes a few minutes...")
    print(f"SL multiples tested:    {SL_MULTIPLES}")
    print(f"Profit targets tested:  {[f'{p*100:.0f}%' for p in PROFIT_TARGETS]}")

    if run_index:
        sweep_index()
    if run_stocks:
        sweep_stocks()

    print("\nDone. Look for the combination with the best P&L AND acceptable drawdown.")
    print("Higher P&L with very low trade count = overfit. Prefer consistency.")
