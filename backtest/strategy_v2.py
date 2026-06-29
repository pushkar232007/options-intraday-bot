"""
v2: same opening-range breakout idea as v1, but adds a volatility filter (skip days
where the opening range is too narrow to mean anything - that was firing on noise in
v1) and tightens the RSI band to avoid chasing already-overbought/oversold moves.
Exit logic switches from "arm-then-trail" to a fixed reward:risk target, which is
simpler to reason about and let's us see if v1's bad win/loss ratio was an exit-logic
problem or an entry-logic problem.
"""

SL_PCT = 0.30          # slightly tighter than v1's 0.35
TARGET_PCT = 0.60      # book the win at +60% premium - fixed 2:1 reward:risk
MIN_RANGE_ATR_MULT = 0.35  # opening range must be at least this big a fraction of ATR14


def decide_entry(day_candles, idx_in_day, ind, global_idx):
    if idx_in_day != 1:
        return None
    opening_range = day_candles[0]
    confirm_candle = day_candles[1]

    e9, e21, rsi, atr = (ind["ema9"][global_idx], ind["ema21"][global_idx],
                          ind["rsi14"][global_idx], ind["atr14"][global_idx])
    if e9 is None or e21 is None or rsi is None or atr is None:
        return None

    range_size = opening_range["h"] - opening_range["l"]
    if range_size < MIN_RANGE_ATR_MULT * atr:
        return None  # too quiet an open to trust a breakout

    breakout_up = confirm_candle["c"] > opening_range["h"]
    breakout_down = confirm_candle["c"] < opening_range["l"]
    uptrend = e9 > e21
    downtrend = e9 < e21

    if breakout_up and uptrend and 55 < rsi < 75:
        return "CE"
    if breakout_down and downtrend and 25 < rsi < 45:
        return "PE"
    return None


def exit_check(entry_premium, current_premium, peak_premium):
    if current_premium <= entry_premium * (1 - SL_PCT):
        return "SL"
    if current_premium >= entry_premium * (1 + TARGET_PCT):
        return "TARGET"
    return None
