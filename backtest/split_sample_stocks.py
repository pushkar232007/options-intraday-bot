"""
Split-sample validation for stock iron condors at multiple DTE windows.

Splits the Bhavcopy database in half by date and runs the backtest independently
on each half. Reports Profit Factor for each half — both must be > 1.2 to pass.

Usage:
  python3 split_sample_stocks.py                   # tests DTE 2-7, 8-14, 15-30
  python3 split_sample_stocks.py --min-dte 8 --max-dte 14
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import bhavcopy_db as db_mod
from backtest_stocks import (
    load_stock_candles, build_price_adx_lookup, UNIVERSE,
    _find_expiry, _find_atm_and_step, _get_condor_prices,
    SHORT_OFFSET_STEPS, LONG_OFFSET_STEPS,
    DEFAULT_PROFIT_TARGET_PCT, DEFAULT_SL_MULTIPLE,
)


def run_range(conn, all_dates, date_subset, adx_threshold=18.0,
              min_dte=2, max_dte=7, min_oi=1000,
              profit_target_pct=DEFAULT_PROFIT_TARGET_PCT,
              sl_multiple=DEFAULT_SL_MULTIPLE,
              stock_price=None, stock_adx=None):
    """Run backtest restricted to date_subset (a set of date strings)."""
    date_to_idx = {d: i for i, d in enumerate(all_dates)}
    trades = []

    for trade_date in all_dates:
        if trade_date not in date_subset:
            continue

        bhavcopy_symbols = set(db_mod.symbols_on_date(conn, trade_date))

        for symbol in sorted(UNIVERSE.keys()):
            if symbol not in bhavcopy_symbols:
                continue
            if symbol not in stock_adx:
                continue
            adx_val = stock_adx[symbol].get(trade_date)
            if adx_val is None or adx_val >= adx_threshold:
                continue

            spot = stock_price[symbol].get(trade_date)
            if spot is None:
                continue

            expiry, dte = _find_expiry(conn, symbol, trade_date, min_dte, max_dte)
            if expiry is None:
                continue

            atm, step = _find_atm_and_step(conn, symbol, trade_date, expiry, spot)
            if atm is None or step <= 0:
                continue

            strikes = {
                "sp": atm - SHORT_OFFSET_STEPS * step,
                "lp": atm - LONG_OFFSET_STEPS * step,
                "sc": atm + SHORT_OFFSET_STEPS * step,
                "lc": atm + LONG_OFFSET_STEPS * step,
            }

            entry_prices = _get_condor_prices(conn, symbol, trade_date, expiry, strikes)
            if entry_prices is None:
                continue
            sp_e, lp_e, sc_e, lc_e = entry_prices
            entry_credit = (sp_e - lp_e) + (sc_e - lc_e)
            if entry_credit <= 0:
                continue

            sp_oi = db_mod.get_open_interest(
                conn, symbol, trade_date, expiry, "PE", strikes["sp"])
            sc_oi = db_mod.get_open_interest(
                conn, symbol, trade_date, expiry, "CE", strikes["sc"])
            if sp_oi < min_oi or sc_oi < min_oi:
                continue

            width = (LONG_OFFSET_STEPS - SHORT_OFFSET_STEPS) * step
            max_loss_per_share = width - entry_credit
            if max_loss_per_share <= 0:
                continue

            exit_cost = None
            exit_reason = "EXPIRY"

            start_idx = date_to_idx.get(trade_date, -1) + 1
            for future_date in all_dates[start_idx:]:
                prices_now = _get_condor_prices(
                    conn, symbol, future_date, expiry, strikes)
                if prices_now is None:
                    if future_date >= expiry:
                        exit_cost = 0.0
                        exit_reason = "EXPIRY_ZERO"
                    continue

                sp_n, lp_n, sc_n, lc_n = prices_now
                cost_now = (sp_n - lp_n) + (sc_n - lc_n)
                exit_cost = cost_now
                exit_reason = "EOD_HOLD"

                if cost_now <= entry_credit * (1 - profit_target_pct):
                    exit_reason = "PROFIT_TARGET"
                    break
                if cost_now >= entry_credit * sl_multiple:
                    exit_reason = "SL"
                    break
                if future_date >= expiry:
                    exit_reason = "EXPIRY"
                    break

            if exit_cost is None:
                continue

            pnl_per_share = entry_credit - exit_cost
            trades.append({
                "pnl": pnl_per_share,
                "entry_credit": entry_credit,
                "dte": dte,
                "exit_reason": exit_reason,
            })

    return trades


def profit_factor(trades):
    wins   = sum(t["pnl"] for t in trades if t["pnl"] > 0)
    losses = abs(sum(t["pnl"] for t in trades if t["pnl"] <= 0))
    if losses == 0:
        return float("inf")
    return wins / losses


def wr(trades):
    if not trades:
        return 0.0
    return sum(1 for t in trades if t["pnl"] > 0) / len(trades) * 100


def print_result(label, trades, n_days):
    pf = profit_factor(trades)
    n  = len(trades)
    passes = pf >= 1.2
    tag = "PASS ✓" if passes else "FAIL ✗"
    avg_credit = sum(t["entry_credit"] for t in trades) / n if n else 0
    avg_pnl    = sum(t["pnl"] for t in trades) / n if n else 0
    print(f"  {label}: [{tag}]  PF={pf:.2f}  WR={wr(trades):.1f}%  "
          f"trades={n}  (~{n/(n_days/21):.1f}/mo)  "
          f"avg_credit=₹{avg_credit:.2f}  avg_pnl=₹{avg_pnl:.2f}")


def validate(min_dte, max_dte, conn, all_dates, stock_price, stock_adx):
    mid = len(all_dates) // 2
    h1_dates = set(all_dates[:mid])
    h2_dates = set(all_dates[mid:])

    print(f"\nDTE {min_dte}-{max_dte}:")
    print(f"  H1 period: {all_dates[0]} → {all_dates[mid-1]}  ({mid} days)")
    print(f"  H2 period: {all_dates[mid]} → {all_dates[-1]}  ({len(all_dates)-mid} days)")

    t1 = run_range(conn, all_dates, h1_dates, min_dte=min_dte, max_dte=max_dte,
                   stock_price=stock_price, stock_adx=stock_adx)
    t2 = run_range(conn, all_dates, h2_dates, min_dte=min_dte, max_dte=max_dte,
                   stock_price=stock_price, stock_adx=stock_adx)

    print_result("H1", t1, mid)
    print_result("H2", t2, len(all_dates) - mid)

    pf1, pf2 = profit_factor(t1), profit_factor(t2)
    verdict = "VALIDATED (PF > 1.2 in both halves)" if pf1 >= 1.2 and pf2 >= 1.2 \
              else "NOT VALIDATED"
    print(f"  >> {verdict}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-dte", type=int, default=None)
    ap.add_argument("--max-dte", type=int, default=None)
    args = ap.parse_args()

    print("Connecting to Bhavcopy database...")
    conn = db_mod.connect()
    all_dates = db_mod.trading_dates(conn)
    print(f"  {len(all_dates)} trading days ({all_dates[0]} → {all_dates[-1]})")

    print("\nLoading stock price data...")
    stock_price, stock_adx = {}, {}
    for nse_sym, yahoo_sym in sorted(UNIVERSE.items()):
        try:
            candles = load_stock_candles(nse_sym, yahoo_sym)
            if len(candles) >= 20:
                pl, al = build_price_adx_lookup(candles)
                stock_price[nse_sym] = pl
                stock_adx[nse_sym]   = al
        except Exception:
            pass
    print(f"  {len(stock_adx)} stocks loaded")

    print("\n" + "=" * 65)
    print("  SPLIT-SAMPLE VALIDATION — Stock Iron Condors")
    print("=" * 65)

    if args.min_dte is not None and args.max_dte is not None:
        validate(args.min_dte, args.max_dte, conn, all_dates, stock_price, stock_adx)
    else:
        for lo, hi in [(2, 7), (8, 14), (15, 30)]:
            validate(lo, hi, conn, all_dates, stock_price, stock_adx)

    conn.close()
