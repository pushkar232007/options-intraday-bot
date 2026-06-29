"""
v1 strategy: opening-range breakout + EMA trend filter + RSI momentum filter.
Buys ATM option only (no spreads yet) in the breakout direction. This is the simplest
possible version of the signal stack described in memory/strategy.md - intentionally
basic so we have a baseline to beat with later versions.

Interface every strategy_vN module exposes, so backtest.py can swap between them:
  decide_entry(day_candles, idx_in_day, ind, global_idx) -> "CE" | "PE" | None
    where ind is a dict of per-candle indicator series: ema9, ema21, rsi14, atr14
  exit_check(entry_premium, current_premium, peak_premium) -> "SL" | "TARGET_TRAIL" | None
"""

SL_PCT = 0.35           # exit if premium drops 35% from entry
TRAIL_ARM_PCT = 0.50    # once premium is up 50%, start trailing
TRAIL_GIVEBACK_PCT = 0.20  # ...and lock in by exiting if it gives back 20% from peak


def decide_entry(day_candles, idx_in_day, ind, global_idx):
    """Only evaluate at idx_in_day == 1 (second 15m candle of the day, ~9:30 IST) -
    i.e. opening-range breakout confirmed on the very next candle, not chased later."""
    if idx_in_day != 1:
        return None
    opening_range = day_candles[0]
    confirm_candle = day_candles[1]

    e9, e21, rsi = ind["ema9"][global_idx], ind["ema21"][global_idx], ind["rsi14"][global_idx]
    if e9 is None or e21 is None or rsi is None:
        return None

    breakout_up = confirm_candle["c"] > opening_range["h"]
    breakout_down = confirm_candle["c"] < opening_range["l"]
    uptrend = e9 > e21
    downtrend = e9 < e21

    if breakout_up and uptrend and rsi > 55:
        return "CE"
    if breakout_down and downtrend and rsi < 45:
        return "PE"
    return None


def exit_check(entry_premium, current_premium, peak_premium):
    if current_premium <= entry_premium * (1 - SL_PCT):
        return "SL"
    if peak_premium >= entry_premium * (1 + TRAIL_ARM_PCT):
        if current_premium <= peak_premium * (1 - TRAIL_GIVEBACK_PCT):
            return "TARGET_TRAIL"
    return None
