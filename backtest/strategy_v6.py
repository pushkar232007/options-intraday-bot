"""
v6: v5's idea (ADX trend-strength gate) was right, but its rolling-lookback scan ate
most of the day before an entry, leaving no runway before forced EOD exit - that's
why it looked even worse than v1-v4, not because the ADX gate itself is bad.

v6 = v3's entry timing exactly (fixed opening-range breakout, checked once at the
first confirm candle right after the open, so a winning trade gets the whole day to
develop) + v5's ADX(14) trend-strength filter added as an extra gate on top of v3's
existing EMA/RSI/daily-trend filters. Isolates whether ADX-gating chop days is what
actually helps, independent of the scan-timing bug.
"""

SL_PCT = 0.30
TARGET_PCT = 0.60
MIN_RANGE_ATR_MULT = 0.35
ADX_THRESHOLD = 20.0


def decide_entry(day_candles, idx_in_day, ind, global_idx, daily_trend=None):
    if idx_in_day != 1:
        return None
    if daily_trend not in ("up", "down"):
        return None

    opening_range = day_candles[0]
    confirm_candle = day_candles[1]

    e9, e21, rsi, atr, adx = (ind["ema9"][global_idx], ind["ema21"][global_idx],
                               ind["rsi14"][global_idx], ind["atr14"][global_idx],
                               ind["adx14"][global_idx])
    if e9 is None or e21 is None or rsi is None or atr is None or adx is None:
        return None
    if adx < ADX_THRESHOLD:
        return None

    range_size = opening_range["h"] - opening_range["l"]
    if range_size < MIN_RANGE_ATR_MULT * atr:
        return None

    breakout_up = confirm_candle["c"] > opening_range["h"]
    breakout_down = confirm_candle["c"] < opening_range["l"]
    uptrend_intraday = e9 > e21
    downtrend_intraday = e9 < e21

    if breakout_up and uptrend_intraday and 55 < rsi < 75 and daily_trend == "up":
        return "CE"
    if breakout_down and downtrend_intraday and 25 < rsi < 45 and daily_trend == "down":
        return "PE"
    return None


def exit_check(entry_premium, current_premium, peak_premium):
    if current_premium <= entry_premium * (1 - SL_PCT):
        return "SL"
    if current_premium >= entry_premium * (1 + TARGET_PCT):
        return "TARGET"
    return None
