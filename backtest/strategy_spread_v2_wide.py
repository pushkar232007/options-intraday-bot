"""
Same logic as strategy_spread_v1 (sell an iron condor on low-ADX/chop days), just
wider strikes: 3 steps OTM for the sold legs, 6 for the protective bought legs,
instead of v1's 2/4. Lower win rate and lower total P&L than v1 in testing, but also
meaningfully lower max drawdown (under 7% at every DTE tested) - the standard
fewer-but-safer tradeoff of selling further from the money.
"""
from strategy_spread_v1 import decide_entry, exit_check, ADX_CHOP_THRESHOLD, PROFIT_TARGET_PCT, SL_MULTIPLE

SHORT_OFFSET_STEPS = 3
LONG_OFFSET_STEPS = 6
