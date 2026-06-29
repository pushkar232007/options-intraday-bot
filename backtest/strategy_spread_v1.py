"""
Credit spread (iron condor) v1: sell premium on days the market looks range-bound
(low ADX = no real trend), rather than betting on a direction. Opposite regime filter
from the naked-buying versions - those wanted to AVOID low-ADX chop, this strategy
specifically WANTS it, since a quiet day is exactly what a premium seller profits from.

Interface (different from the naked-buying strategy_vN files):
  decide_entry(day_candles, idx_in_day, ind, global_idx) -> True | False
  exit_check(entry_credit, current_value) -> "SL" | "PROFIT_TARGET" | None
"""

SHORT_OFFSET_STEPS = 2   # how many strike-steps OTM the sold legs are
LONG_OFFSET_STEPS = 4    # how many strike-steps OTM the protective bought legs are
ADX_CHOP_THRESHOLD = 18.0  # below this, Wilder considers it a non-trending/quiet day
PROFIT_TARGET_PCT = 0.50   # close early once 50% of max credit has decayed away
SL_MULTIPLE = 2.0          # close if cost-to-close grows to 2x the credit received


def decide_entry(day_candles, idx_in_day, ind, global_idx):
    if idx_in_day != 1:
        return False
    adx = ind["adx14"][global_idx]
    if adx is None:
        return False
    return adx < ADX_CHOP_THRESHOLD


def exit_check(entry_credit, current_value):
    if current_value <= entry_credit * (1 - PROFIT_TARGET_PCT):
        return "PROFIT_TARGET"
    if current_value >= entry_credit * SL_MULTIPLE:
        return "SL"
    return None
