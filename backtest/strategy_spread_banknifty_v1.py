"""
Credit spread tuned for BankNifty's monthly (long-dated) cycle, not the weekly one
strategy_spread_v1 was built for. Why a different structure is needed: strategy_spread_v1
was basically breakeven on BankNifty's real monthly calendar (avg 18 DTE at entry) - because
far from expiry, theta decay per single day is slow and 2/4-strike-OTM legs barely respond
to one day's price action (low gamma that far out), so the 50%-target/2x-stop thresholds
almost never trigger and most trades just drift to EOD on noise.

Fix: move strikes much closer to the money (higher gamma -> a normal day's move actually
moves the spread's value meaningfully) and use a smaller, more realistic profit target for
a single day's decay at long DTE.
"""

SHORT_OFFSET_STEPS = 1   # near-ATM instead of v1's 2 - needs more gamma to react within a day
LONG_OFFSET_STEPS = 3
ADX_CHOP_THRESHOLD = 18.0
PROFIT_TARGET_PCT = 0.15   # smaller target - realistic for one day's decay at long DTE
SL_MULTIPLE = 1.5          # tighter stop to match the smaller target (keep reward:risk sane)


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
