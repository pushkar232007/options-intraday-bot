"""Pure-Python indicator helpers (no numpy/pandas dependency, same style as delta-backtest)."""


def ema_series(values, period):
    k = 2 / (period + 1)
    out = [None] * len(values)
    ema = None
    for i, v in enumerate(values):
        if ema is None:
            if i < period - 1:
                continue
            ema = sum(values[i - period + 1:i + 1]) / period
        else:
            ema = v * k + ema * (1 - k)
        out[i] = ema
    return out


def rsi_series(closes, period=14):
    out = [None] * len(closes)
    gains, losses = [], []
    for i in range(1, len(closes)):
        delta = closes[i] - closes[i - 1]
        gains.append(max(delta, 0))
        losses.append(max(-delta, 0))
        if i >= period:
            avg_gain = sum(gains[-period:]) / period
            avg_loss = sum(losses[-period:]) / period
            if avg_loss == 0:
                out[i] = 100.0
            else:
                rs = avg_gain / avg_loss
                out[i] = 100 - (100 / (1 + rs))
    return out


def atr_series(highs, lows, closes, period=14):
    trs = [None] * len(closes)
    for i in range(1, len(closes)):
        trs[i] = max(highs[i] - lows[i], abs(highs[i] - closes[i - 1]), abs(lows[i] - closes[i - 1]))
    out = [None] * len(closes)
    atr = None
    for i in range(len(closes)):
        if trs[i] is None:
            continue
        if atr is None:
            window = [t for t in trs[max(1, i - period + 1):i + 1] if t is not None]
            if len(window) < period:
                continue
            atr = sum(window) / period
        else:
            atr = (atr * (period - 1) + trs[i]) / period
        out[i] = atr
    return out


def adx_series(highs, lows, closes, period=14):
    """Standard Wilder ADX - measures trend *strength* regardless of direction.
    Used to filter out chop days, which simple EMA/RSI breakout logic can't tell apart
    from real trending days."""
    n = len(closes)
    plus_dm = [0.0] * n
    minus_dm = [0.0] * n
    tr = [0.0] * n
    for i in range(1, n):
        up_move = highs[i] - highs[i - 1]
        down_move = lows[i - 1] - lows[i]
        plus_dm[i] = up_move if (up_move > down_move and up_move > 0) else 0.0
        minus_dm[i] = down_move if (down_move > up_move and down_move > 0) else 0.0
        tr[i] = max(highs[i] - lows[i], abs(highs[i] - closes[i - 1]), abs(lows[i] - closes[i - 1]))

    def wilder_smooth(series):
        out = [None] * n
        sm = None
        for i in range(n):
            if sm is None:
                if i < period:
                    continue
                sm = sum(series[i - period + 1:i + 1])
            else:
                sm = sm - sm / period + series[i]
            out[i] = sm
        return out

    tr_sm = wilder_smooth(tr)
    plus_dm_sm = wilder_smooth(plus_dm)
    minus_dm_sm = wilder_smooth(minus_dm)

    dx = [None] * n
    for i in range(n):
        if tr_sm[i] is None or tr_sm[i] == 0:
            continue
        plus_di = 100 * plus_dm_sm[i] / tr_sm[i]
        minus_di = 100 * minus_dm_sm[i] / tr_sm[i]
        denom = plus_di + minus_di
        dx[i] = 100 * abs(plus_di - minus_di) / denom if denom else 0.0

    out = [None] * n
    adx = None
    valid_dx = [v for v in dx if v is not None]
    first_dx_idx = next((i for i, v in enumerate(dx) if v is not None), None)
    if first_dx_idx is None:
        return out
    for i in range(first_dx_idx, n):
        if dx[i] is None:
            continue
        if adx is None:
            window = [v for v in dx[max(0, i - period + 1):i + 1] if v is not None]
            if len(window) < period:
                continue
            adx = sum(window) / period
        else:
            adx = (adx * (period - 1) + dx[i]) / period
        out[i] = adx
    return out


def session_vwap(candles_today):
    """candles_today: list of dicts with o/h/l/c/v, same trading day, in order."""
    cum_pv = 0.0
    cum_v = 0.0
    out = []
    for c in candles_today:
        typical = (c["h"] + c["l"] + c["c"]) / 3
        vol = c["v"] or 0
        cum_pv += typical * vol
        cum_v += vol
        out.append(cum_pv / cum_v if cum_v > 0 else c["c"])
    return out


def group_by_day(candles, tz_offset_seconds=19800):
    """Groups 15m candles into per-day lists using IST day boundaries (epoch ts are UTC)."""
    days = {}
    for c in candles:
        local_t = c["t"] + tz_offset_seconds
        day_key = local_t // 86400
        days.setdefault(day_key, []).append(c)
    return [days[k] for k in sorted(days.keys())]
