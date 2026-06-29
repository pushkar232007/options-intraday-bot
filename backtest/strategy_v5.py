"""
v5: different axis from v1-v4. Those all used a *fixed* signal point (the opening
range, checked once) and direction filters (EMA, RSI) that can't tell a real trend day
from a choppy one. v5 adds an ADX trend-strength gate (skip chop entirely, only act on
days the market is actually trending) and scans every candle through the day for a
rolling N-candle high/low breakout, instead of only checking the open.
"""

SL_PCT = 0.30
TARGET_PCT = 0.60
LOOKBACK = 4          # rolling N-candle range instead of fixed opening range
ADX_THRESHOLD = 20.0  # below this, Wilder considers the move non-trending/chop


def decide_entry(day_candles, idx_in_day, ind, global_idx, daily_trend=None):
    if idx_in_day < LOOKBACK:
        return None
    if daily_trend not in ("up", "down"):
        return None

    adx = ind["adx14"][global_idx]
    rsi = ind["rsi14"][global_idx]
    e9, e21 = ind["ema9"][global_idx], ind["ema21"][global_idx]
    if adx is None or rsi is None or e9 is None or e21 is None:
        return None
    if adx < ADX_THRESHOLD:
        return None  # chop - sit out regardless of direction

    window = day_candles[idx_in_day - LOOKBACK:idx_in_day]
    rolling_high = max(c["h"] for c in window)
    rolling_low = min(c["l"] for c in window)
    current = day_candles[idx_in_day]

    breakout_up = current["c"] > rolling_high
    breakout_down = current["c"] < rolling_low

    if breakout_up and e9 > e21 and rsi > 50 and daily_trend == "up":
        return "CE"
    if breakout_down and e9 < e21 and rsi < 50 and daily_trend == "down":
        return "PE"
    return None


def exit_check(entry_premium, current_premium, peak_premium):
    if current_premium <= entry_premium * (1 - SL_PCT):
        return "SL"
    if current_premium >= entry_premium * (1 + TARGET_PCT):
        return "TARGET"
    return None
