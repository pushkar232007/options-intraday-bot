"""
v3: same as v2 (volatility-filtered opening-range breakout, fixed 2:1 R:R), plus a
daily-timeframe trend filter. v2's BankNifty trades were mostly PE (puts) that got
stopped out while BankNifty was in a daily uptrend - the 15m EMA9/21 was agreeing with
the PE signal in the moment but fighting the bigger trend. This adds a "don't fight
yesterday's daily trend" gate: CE only if daily trend is up, PE only if daily trend is
down, using *yesterday's* daily close vs daily EMA20 (no lookahead - that's the trend
information actually known before today's open).
"""

SL_PCT = 0.30
TARGET_PCT = 0.60
MIN_RANGE_ATR_MULT = 0.35


def decide_entry(day_candles, idx_in_day, ind, global_idx, daily_trend=None):
    if idx_in_day != 1:
        return None
    if daily_trend not in ("up", "down"):
        return None  # no usable daily trend reading (e.g. first day in series) -> skip

    opening_range = day_candles[0]
    confirm_candle = day_candles[1]

    e9, e21, rsi, atr = (ind["ema9"][global_idx], ind["ema21"][global_idx],
                          ind["rsi14"][global_idx], ind["atr14"][global_idx])
    if e9 is None or e21 is None or rsi is None or atr is None:
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
