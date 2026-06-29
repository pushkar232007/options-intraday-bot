"""
Fetches free historical OHLC data from Yahoo Finance for the underlying indices
(Nifty, BankNifty, Sensex) and India VIX. There is no free historical *option premium*
data source for NSE/BSE options, so this backtest simulates option payoffs from the
underlying's real price action + real India VIX via Black-Scholes (see bs_pricer.py)
instead of replaying actual historical option chain prices. That's an approximation,
not real option market microstructure (real bid/ask, OI shifts, skew) - flagged here
so it doesn't get mistaken for higher-fidelity data than it is.
"""
import json
import os
import urllib.request
import urllib.parse

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
BASE_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"

SYMBOLS = {
    "NIFTY": "%5ENSEI",
    "BANKNIFTY": "%5ENSEBANK",
    "SENSEX": "%5EBSESN",
    "INDIAVIX": "%5EINDIAVIX",
}


def _fetch(symbol_enc, range_, interval):
    url = BASE_URL.format(symbol=symbol_enc) + "?" + urllib.parse.urlencode({
        "range": range_, "interval": interval,
    })
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        body = json.loads(resp.read())
    result = body["chart"]["result"]
    if not result:
        raise RuntimeError(f"no data for {symbol_enc} range={range_} interval={interval}")
    r = result[0]
    ts = r["timestamp"]
    quote = r["indicators"]["quote"][0]
    candles = []
    for i, t in enumerate(ts):
        o, h, l, c, v = (quote["open"][i], quote["high"][i], quote["low"][i],
                          quote["close"][i], quote.get("volume", [None] * len(ts))[i])
        if c is None:
            continue
        candles.append({"t": t, "o": o, "h": h, "l": l, "c": c, "v": v})
    return candles


def cache_path(name, interval):
    return os.path.join(DATA_DIR, f"{name}_{interval}.json")


def fetch_and_cache(name, range_, interval):
    candles = _fetch(SYMBOLS[name], range_, interval)
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(cache_path(name, interval), "w") as f:
        json.dump(candles, f)
    print(f"{name} {interval}: cached {len(candles)} candles")
    return candles


def load_cached(name, interval):
    with open(cache_path(name, interval)) as f:
        return json.load(f)


if __name__ == "__main__":
    for name in ("NIFTY", "BANKNIFTY", "SENSEX"):
        fetch_and_cache(name, "10y", "1d")   # daily, long history - regime/trend context
        fetch_and_cache(name, "60d", "15m")  # intraday - signal backtesting (Yahoo's max for 15m)
        fetch_and_cache(name, "60d", "5m")   # finer intraday - Yahoo's max for 5m is also 60d
        fetch_and_cache(name, "2y", "1h")    # intraday, longer window - robustness check
    fetch_and_cache("INDIAVIX", "10y", "1d")
    fetch_and_cache("INDIAVIX", "60d", "15m")
    fetch_and_cache("INDIAVIX", "60d", "5m")
    fetch_and_cache("INDIAVIX", "2y", "1h")
