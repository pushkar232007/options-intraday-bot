#!/usr/bin/env python3
"""
Pure-logic risk helpers matching the guardrails in memory/strategy.md. No API calls -
these are calculator functions a routine calls before placing or skipping a trade.

Usage (CLI, for quick manual checks):
  python3 scripts/risk.py size-spread --capital 100000 --width 200 --credit 130 --lot-size 75
  python3 scripts/risk.py circuit-breaker --capital 100000 --day-pnl -10500
"""
import argparse


RISK_PCT_PER_TRADE = 5.0
DAILY_LOSS_CAP_PCT = 10.0


def max_loss_per_unit(strike_width, net_credit):
    """strike_width: difference between short and long strike (same currency as credit)."""
    return strike_width - net_credit


def size_spread(capital, strike_width, net_credit, lot_size, risk_pct=RISK_PCT_PER_TRADE):
    """Returns qty in lots, sized so max possible loss <= risk_pct% of capital.
    Returns 0 if even 1 lot would breach the risk cap (skip the trade)."""
    loss_per_unit = max_loss_per_unit(strike_width, net_credit)
    if loss_per_unit <= 0:
        return 0  # credit >= width shouldn't happen - treat as a pricing error, not a free trade
    risk_amount = capital * (risk_pct / 100.0)
    qty_lots = int(risk_amount / (loss_per_unit * lot_size))
    return max(qty_lots, 0)


def circuit_breaker_tripped(capital, day_pnl, cap_pct=DAILY_LOSS_CAP_PCT):
    return day_pnl <= -(capital * (cap_pct / 100.0))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="command", required=True)

    p = sub.add_parser("size-spread")
    p.add_argument("--capital", type=float, required=True)
    p.add_argument("--width", type=float, required=True)
    p.add_argument("--credit", type=float, required=True)
    p.add_argument("--lot-size", type=int, required=True)
    p.add_argument("--risk-pct", type=float, default=RISK_PCT_PER_TRADE)

    p2 = sub.add_parser("circuit-breaker")
    p2.add_argument("--capital", type=float, required=True)
    p2.add_argument("--day-pnl", type=float, required=True)
    p2.add_argument("--cap-pct", type=float, default=DAILY_LOSS_CAP_PCT)

    args = ap.parse_args()
    if args.command == "size-spread":
        qty = size_spread(args.capital, args.width, args.credit, args.lot_size, args.risk_pct)
        print(f"qty_lots={qty}")
    elif args.command == "circuit-breaker":
        tripped = circuit_breaker_tripped(args.capital, args.day_pnl, args.cap_pct)
        print(f"tripped={tripped}")
