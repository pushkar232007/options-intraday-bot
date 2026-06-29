"""
v4: v1/v2/v3 all chased the opening-range breakout direction and all failed badly on
the larger 491-day hourly sample (win rate 13-31%, consistently negative P&L). That's
a real signal that naive breakout-chasing has no edge here, not a parameter problem.
This version tests the opposite hypothesis: fade the open instead of chasing it -
buy a PE when price pushes above the opening range into overbought RSI (expecting a
pullback), buy a CE when price pushes below the opening range into oversold RSI
(expecting a bounce). Still gated by the daily-trend filter, but now trading *with*
mean-reversion rather than *with* momentum.
"""

SL_PCT = 0.30
TARGET_PCT = 0.60


def decide_entry(day_candles, idx_in_day, ind, global_idx, daily_trend=None):
    if idx_in_day != 1:
        return None
    if daily_trend not in ("up", "down"):
        return None

    opening_range = day_candles[0]
    confirm_candle = day_candles[1]
    rsi = ind["rsi14"][global_idx]
    if rsi is None:
        return None

    pushed_above = confirm_candle["c"] > opening_range["h"]
    pushed_below = confirm_candle["c"] < opening_range["l"]

    # Fade an overbought push higher with a PE, but only with the daily trend down
    # (don't fade a push higher if the bigger trend also agrees with going higher).
    if pushed_above and rsi > 70 and daily_trend == "down":
        return "PE"
    # Fade an oversold push lower with a CE, only with the daily trend up.
    if pushed_below and rsi < 30 and daily_trend == "up":
        return "CE"
    return None


def exit_check(entry_premium, current_premium, peak_premium):
    if current_premium <= entry_premium * (1 - SL_PCT):
        return "SL"
    if current_premium >= entry_premium * (1 + TARGET_PCT):
        return "TARGET"
    return None
