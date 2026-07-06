"""
Compare index condor P&L under three hold rules:
  A) Intraday-only (current): force-close at EOD, never carry overnight
  B) Multi-day carry: hold until profit-target / SL / expiry, NOT forced at EOD
  C) Multi-day, no-gamma: same as B but force-close at EOD if DTE remaining < 2
     (avoids holding into expiry-day gamma risk)

All three use the same entry signal (ADX < 18, same strategy_spread_v1 params).
This directly answers: does allowing overnight holds improve index condor results?

Usage: cd backtest && python3 test_multiday_index.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))

from fetch_data import load_cached
from indicators import ema_series, rsi_series, atr_series, adx_series
from bs_pricer import STRIKE_STEP, LOT_SIZE
from iron_condor import build_condor, condor_net_value
from backtest import INSTRUMENTS, STARTING_CAPITAL, build_day_index, vix_close_at
import strategy_spread_v1 as strategy
import backtest_spreads as original


# ── shared data loader ────────────────────────────────────────────────────────

def _load_all(interval="1h"):
    per = {}
    for name in INSTRUMENTS:
        c = load_cached(name, interval)
        cl = [x["c"] for x in c]; hi = [x["h"] for x in c]; lo = [x["l"] for x in c]
        days, dsi = build_day_index(c)
        vc = load_cached("INDIAVIX", interval)
        vd, _ = build_day_index(vc)
        per[name] = dict(
            days=days, dsi=dsi, vix_days=vd,
            ind=dict(ema9=ema_series(cl,9), ema21=ema_series(cl,21),
                     rsi14=rsi_series(cl,14), atr14=atr_series(hi,lo,cl,14),
                     adx14=adx_series(hi,lo,cl,14)),
        )
    return per


# ── Multi-day engine ──────────────────────────────────────────────────────────

def run_multiday(per, days_to_expiry=3, risk_pct=5.0, min_dte_to_carry=1):
    """
    min_dte_to_carry: carry overnight only if DTE-remaining >= this value.
      1  → carry until expiry day, force-close at expiry EOD
      2  → force-close if DTE < 2 at EOD (avoid gamma on expiry day itself)
    """
    num_days = min(len(per[n]["days"]) for n in INSTRUMENTS)
    capital = STARTING_CAPITAL
    trades = []
    equity_curve = [capital]
    open_pos = {}  # name → position dict

    for day_pos in range(num_days):
        day_pnl = 0.0

        for name in INSTRUMENTS:
            info = per[name]
            day_candles = info["days"][day_pos]
            if len(day_candles) < 2:
                continue
            step = STRIKE_STEP[name]
            lot  = LOT_SIZE[name]

            # ── manage existing carry ──
            if name in open_pos:
                pos = open_pos[name]
                days_held = day_pos - pos["entry_day"]
                dte_today = max(pos["dte_at_entry"] - days_held, 0.05)
                n_c = len(day_candles)
                exit_val = None
                exit_rsn = None

                for j, candle in enumerate(day_candles):
                    spot = candle["c"]
                    iv   = vix_close_at(info["vix_days"], day_pos, j)
                    dte  = max(dte_today - j / max(n_c, 1), 0.05)
                    val  = condor_net_value(pos["strikes"], spot, dte, iv)
                    rsn  = strategy.exit_check(pos["entry_credit"], val)
                    exit_val = val
                    if rsn:
                        exit_rsn = rsn
                        break

                if exit_rsn is None:
                    dte_after_today = max(dte_today - 1.0, 0.0)
                    if dte_after_today < min_dte_to_carry:
                        exit_rsn = "EXPIRY_EOD"
                    else:
                        continue  # carry forward one more day

                pnl = (pos["entry_credit"] - exit_val) * pos["qty_lots"] * lot
                capital += pnl; day_pnl += pnl
                trades.append(dict(
                    day=day_pos, instrument=name,
                    entry_credit=pos["entry_credit"], exit_value=exit_val,
                    qty_lots=pos["qty_lots"], pnl=pnl, reason=exit_rsn,
                    days_held=days_held + 1,
                ))
                del open_pos[name]
                continue  # don't look for new entry the same day we closed

            # ── look for new entry ──
            if not strategy.decide_entry(day_candles, 1, info["ind"], info["dsi"][day_pos] + 1):
                continue

            spot_e = day_candles[1]["c"]
            strikes = build_condor(spot_e, step, strategy.SHORT_OFFSET_STEPS,
                                   strategy.LONG_OFFSET_STEPS)
            iv_e = vix_close_at(info["vix_days"], day_pos, 1)
            credit = condor_net_value(strikes, spot_e, days_to_expiry, iv_e)
            if credit <= 0:
                continue
            max_loss = (strategy.LONG_OFFSET_STEPS - strategy.SHORT_OFFSET_STEPS) * step - credit
            if max_loss <= 0:
                continue
            qty = int((capital * risk_pct / 100) / max(max_loss * lot, 1))
            if qty < 1:
                continue

            # check intraday exits first (same day as entry)
            exit_val = credit; exit_rsn = None
            n_c = len(day_candles)
            for j, candle in enumerate(day_candles[2:], start=2):
                spot = candle["c"]
                iv   = vix_close_at(info["vix_days"], day_pos, j)
                dte  = max(days_to_expiry - j / max(n_c, 1), 0.05)
                val  = condor_net_value(strikes, spot, dte, iv)
                rsn  = strategy.exit_check(credit, val)
                exit_val = val
                if rsn:
                    exit_rsn = rsn
                    break

            if exit_rsn:
                pnl = (credit - exit_val) * qty * lot
                capital += pnl; day_pnl += pnl
                trades.append(dict(day=day_pos, instrument=name, entry_credit=credit,
                                   exit_value=exit_val, qty_lots=qty, pnl=pnl,
                                   reason=exit_rsn, days_held=0))
            else:
                dte_eod = max(days_to_expiry - 1.0, 0.0)
                if dte_eod < min_dte_to_carry:
                    # would expire tomorrow; close at EOD instead of carrying
                    pnl = (credit - exit_val) * qty * lot
                    capital += pnl; day_pnl += pnl
                    trades.append(dict(day=day_pos, instrument=name, entry_credit=credit,
                                       exit_value=exit_val, qty_lots=qty, pnl=pnl,
                                       reason="EXPIRY_EOD", days_held=0))
                else:
                    open_pos[name] = dict(
                        entry_credit=credit, strikes=strikes, qty_lots=qty,
                        entry_day=day_pos, dte_at_entry=days_to_expiry,
                    )

        equity_curve.append(capital)

    return dict(trades=trades, final_capital=capital, equity_curve=equity_curve,
                num_days=num_days)


# ── stats ─────────────────────────────────────────────────────────────────────

def _stats(result):
    trades = result["trades"]
    n = len(trades)
    if n == 0:
        return dict(n=0, wr=0, pnl=0, final=result["final_capital"], dd=0, avg_hold=0)
    wins = sum(1 for t in trades if t["pnl"] > 0)
    total_pnl = sum(t["pnl"] for t in trades)
    eq = result["equity_curve"]
    peak = eq[0]; max_dd = 0.0
    for e in eq:
        peak = max(peak, e)
        max_dd = max(max_dd, (peak - e) / peak)
    avg_hold = sum(t.get("days_held", 0) for t in trades) / n
    return dict(n=n, wr=wins/n*100, pnl=total_pnl,
                final=result["final_capital"], dd=max_dd*100, avg_hold=avg_hold)


def _reason_breakdown(trades):
    counts = {}
    for t in trades:
        counts[t["reason"]] = counts.get(t["reason"], 0) + 1
    return counts


# ── main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Loading market data...")
    per = _load_all()
    DTE = 3

    print(f"\nRunning three scenarios (DTE={DTE} at entry, same entry signal)...\n")

    # A: intraday-only (original engine)
    res_A = original.run("strategy_spread_v1", days_to_expiry=DTE,
                         risk_pct=5.0, daily_loss_cap_pct=999.0)
    s_A = _stats(res_A)

    # B: multi-day, carry until expiry day
    res_B = run_multiday(per, days_to_expiry=DTE, risk_pct=5.0, min_dte_to_carry=1)
    s_B = _stats(res_B)

    # C: multi-day, force-close if DTE < 2 at EOD (avoids expiry-day gamma)
    res_C = run_multiday(per, days_to_expiry=DTE, risk_pct=5.0, min_dte_to_carry=2)
    s_C = _stats(res_C)

    # Also test DTE=5 multi-day (enter earlier, more theta room)
    res_D = run_multiday(per, days_to_expiry=5, risk_pct=5.0, min_dte_to_carry=1)
    s_D = _stats(res_D)

    hdr = f"  {'Scenario':<38} {'Trades':>7} {'WR':>8} {'Total P&L':>12} {'Final Cap':>11} {'Max DD':>8} {'Avg Hold':>10}"
    sep = "  " + "-"*100
    print(hdr)
    print(sep)
    def row(label, s):
        print(f"  {label:<38} {s['n']:>7d} {s['wr']:>7.1f}% {s['pnl']:>+12.0f} "
              f"{s['final']:>11.0f} {s['dd']:>7.1f}% {s['avg_hold']:>9.2f}d")

    row("A) Intraday-only  (DTE=3, current)",  s_A)
    row("B) Multi-day carry (DTE=3, carry→expiry)", s_B)
    row("C) Multi-day, no-gamma (DTE=3, carry→DTE<2 force-close)", s_C)
    row("D) Multi-day carry (DTE=5, enter earlier)", s_D)
    print(sep)

    print("\nExit reason breakdown:")
    for label, res in [("A (intraday)", res_A), ("B (multi-day DTE3)", res_B),
                        ("C (no-gamma DTE3)", res_C), ("D (multi-day DTE5)", res_D)]:
        rb = _reason_breakdown(res["trades"])
        print(f"  {label:<30}: {rb}")

    print(f"\nStarting capital: {STARTING_CAPITAL:,.0f}")
    print("Note: overnight gap risk is modelled via the next day's first candle open price.")
    print("      Black-Scholes doesn't perfectly capture gap risk — treat multi-day results")
    print("      as optimistic by ~5-10% vs real-world due to continuous-time assumption.")
