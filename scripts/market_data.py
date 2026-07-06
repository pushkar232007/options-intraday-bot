#!/usr/bin/env python3
"""
Real price/VIX data + ADX + option-premium estimates, for use while Dhan's sandbox can't
supply market data (confirmed 404 on /optionchain and /marketfeed/* there - see
memory/signals-learnings.md). Uses Yahoo Finance for real spot/VIX data (same source the
backtest validated against) and the same Black-Scholes estimate the backtest used to decide
whether a setup is worth taking and how to size it. Once Dhan's live Data API subscription is
active, prefer real option-chain premiums over the `estimate-premium` command here - this is
a stand-in for sandbox/early-paper-trading, not meant to be the permanent source live.

Usage:
  python3 scripts/market_data.py scan                          # ADX + spot + VIX for all 3
  python3 scripts/market_data.py spot NIFTY
  python3 scripts/market_data.py vix
  python3 scripts/market_data.py adx NIFTY
  python3 scripts/market_data.py estimate-premium NIFTY 24000 CE --dte 2
"""
import argparse
import json
import math
import urllib.parse
import urllib.request

YF_SYMBOLS = {"NIFTY": "%5ENSEI", "BANKNIFTY": "%5ENSEBANK", "SENSEX": "%5EBSESN", "INDIAVIX": "%5EINDIAVIX"}
INSTRUMENTS = ["NIFTY", "BANKNIFTY", "SENSEX"]

# Nifty 50 F&O stocks — NSE symbol → Yahoo Finance symbol
# AXISBANK and BHARTIARTL excluded (backtest showed negative edge: 68% and 64% WR respectively)
STOCK_BLOCKLIST = {"AXISBANK", "BHARTIARTL"}
STOCK_UNIVERSE = {
    "RELIANCE": "RELIANCE.NS", "HDFCBANK": "HDFCBANK.NS", "ICICIBANK": "ICICIBANK.NS",
    "INFY": "INFY.NS", "TCS": "TCS.NS", "SBIN": "SBIN.NS", "KOTAKBANK": "KOTAKBANK.NS",
    "BAJFINANCE": "BAJFINANCE.NS", "HINDUNILVR": "HINDUNILVR.NS", "LT": "LT.NS",
    "ITC": "ITC.NS", "TATAMOTORS": "TATAMOTORS.NS", "TATASTEEL": "TATASTEEL.NS",
    "WIPRO": "WIPRO.NS", "HCLTECH": "HCLTECH.NS", "SUNPHARMA": "SUNPHARMA.NS",
    "NTPC": "NTPC.NS", "POWERGRID": "POWERGRID.NS", "ADANIENT": "ADANIENT.NS",
    "ADANIPORTS": "ADANIPORTS.NS", "BAJAJFINSV": "BAJAJFINSV.NS", "MARUTI": "MARUTI.NS",
    "TITAN": "TITAN.NS", "ASIANPAINT": "ASIANPAINT.NS", "DRREDDY": "DRREDDY.NS",
    "CIPLA": "CIPLA.NS", "HINDALCO": "HINDALCO.NS", "JSWSTEEL": "JSWSTEEL.NS",
    "HEROMOTOCO": "HEROMOTOCO.NS", "EICHERMOT": "EICHERMOT.NS", "TECHM": "TECHM.NS",
    "ULTRACEMCO": "ULTRACEMCO.NS", "GRASIM": "GRASIM.NS", "COALINDIA": "COALINDIA.NS",
    "BPCL": "BPCL.NS", "ONGC": "ONGC.NS", "INDUSINDBK": "INDUSINDBK.NS",
    "APOLLOHOSP": "APOLLOHOSP.NS", "TATACONSUM": "TATACONSUM.NS", "NESTLEIND": "NESTLEIND.NS",
    "BEL": "BEL.NS", "HDFCLIFE": "HDFCLIFE.NS", "SBILIFE": "SBILIFE.NS",
    "BAJAJ-AUTO": "BAJAJ-AUTO.NS", "HINDZINC": "HINDZINC.NS", "VEDL": "VEDL.NS",
    "NMDC": "NMDC.NS", "BANKBARODA": "BANKBARODA.NS", "PNB": "PNB.NS",
    "CANBK": "CANBK.NS", "SIEMENS": "SIEMENS.NS", "PIDILITIND": "PIDILITIND.NS",
    "DMART": "DMART.NS",
}


def _fetch_yf(symbol_enc, range_="5d", interval="15m"):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol_enc}?" + urllib.parse.urlencode(
        {"range": range_, "interval": interval})
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read())
    r = body["chart"]["result"][0]
    ts = r["timestamp"]
    q = r["indicators"]["quote"][0]
    candles = []
    for i, t in enumerate(ts):
        if q["close"][i] is None:
            continue
        candles.append({"t": t, "o": q["open"][i], "h": q["high"][i], "l": q["low"][i], "c": q["close"][i]})
    return candles


def get_spot(instrument):
    candles = _fetch_yf(YF_SYMBOLS[instrument], range_="1d", interval="1m")
    return candles[-1]["c"]


def get_vix():
    candles = _fetch_yf(YF_SYMBOLS["INDIAVIX"], range_="1d", interval="1m")
    return candles[-1]["c"]


def _adx14(candles, period=14):
    highs, lows, closes = [c["h"] for c in candles], [c["l"] for c in candles], [c["c"] for c in candles]
    n = len(closes)
    plus_dm, minus_dm, tr = [0.0] * n, [0.0] * n, [0.0] * n
    for i in range(1, n):
        up, down = highs[i] - highs[i - 1], lows[i - 1] - lows[i]
        plus_dm[i] = up if (up > down and up > 0) else 0.0
        minus_dm[i] = down if (down > up and down > 0) else 0.0
        tr[i] = max(highs[i] - lows[i], abs(highs[i] - closes[i - 1]), abs(lows[i] - closes[i - 1]))

    def smooth(series):
        out, sm = [None] * n, None
        for i in range(n):
            if sm is None:
                if i < period:
                    continue
                sm = sum(series[i - period + 1:i + 1])
            else:
                sm = sm - sm / period + series[i]
            out[i] = sm
        return out

    tr_s, plus_s, minus_s = smooth(tr), smooth(plus_dm), smooth(minus_dm)
    dx = [None] * n
    for i in range(n):
        if not tr_s[i]:
            continue
        pdi, mdi = 100 * plus_s[i] / tr_s[i], 100 * minus_s[i] / tr_s[i]
        denom = pdi + mdi
        dx[i] = 100 * abs(pdi - mdi) / denom if denom else 0.0
    valid = [v for v in dx if v is not None]
    if len(valid) < period:
        return None
    adx = sum(valid[:period]) / period
    for v in valid[period:]:
        adx = (adx * (period - 1) + v) / period
    return adx


def get_adx(instrument, interval="15m"):
    candles = _fetch_yf(YF_SYMBOLS[instrument], range_="5d", interval=interval)
    return _adx14(candles)


def _norm_cdf(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0


def estimate_premium(spot, strike, dte_days, iv_pct, option_type, r=0.06):
    t = max(dte_days, 0.25) / 365.0
    sigma = max(iv_pct, 1.0) / 100.0
    d1 = (math.log(spot / strike) + (r + sigma ** 2 / 2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)
    if option_type == "CE":
        price = spot * _norm_cdf(d1) - strike * math.exp(-r * t) * _norm_cdf(d2)
    else:
        price = strike * math.exp(-r * t) * _norm_cdf(-d2) - spot * _norm_cdf(-d1)
    return max(price, 0.05)


def cmd_scan(args):
    vix = get_vix()
    result = {"vix": round(vix, 2), "instruments": {}}
    for name in INSTRUMENTS:
        spot = get_spot(name)
        adx = get_adx(name)
        result["instruments"][name] = {
            "spot": round(spot, 2),
            "adx14": round(adx, 2) if adx is not None else None,
            "range_bound": (adx is not None and adx < 18.0),
        }
    print(json.dumps(result, indent=2))


def cmd_spot(args):
    print(json.dumps({"instrument": args.instrument, "spot": round(get_spot(args.instrument), 2)}))


def cmd_vix(args):
    print(json.dumps({"vix": round(get_vix(), 2)}))


def cmd_adx(args):
    adx = get_adx(args.instrument)
    print(json.dumps({"instrument": args.instrument, "adx14": round(adx, 2) if adx is not None else None}))


def cmd_estimate_premium(args):
    # For stock symbols, fetch spot from Yahoo Finance daily data
    if args.instrument in STOCK_UNIVERSE:
        candles = _fetch_yf_daily(STOCK_UNIVERSE[args.instrument], range_="5d")
        spot = candles[-1]["c"]
    else:
        spot = get_spot(args.instrument)
    iv = args.iv if args.iv is not None else get_vix()
    premium = estimate_premium(spot, args.strike, args.dte, iv, args.option_type)
    print(json.dumps({"instrument": args.instrument, "spot": round(spot, 2), "iv_pct": round(iv, 2),
                        "strike": args.strike, "dte": args.dte, "option_type": args.option_type,
                        "estimated_premium": round(premium, 2)}))


def _fetch_yf_daily(yahoo_symbol, range_="3mo"):
    """Fetches daily OHLC candles — used for stock ADX (daily bars, not 15m)."""
    enc = urllib.parse.quote(yahoo_symbol)
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{enc}?"
           + urllib.parse.urlencode({"range": range_, "interval": "1d"}))
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read())
    r = body["chart"]["result"][0]
    ts = r["timestamp"]
    q = r["indicators"]["quote"][0]
    candles = []
    for i, t in enumerate(ts):
        if q["close"][i] is None:
            continue
        candles.append({"t": t, "o": q["open"][i], "h": q["high"][i],
                        "l": q["low"][i], "c": q["close"][i]})
    return candles


def _hist_vol(candles, days=30):
    """Annualised historical volatility (%) from last `days` daily closes."""
    closes = [c["c"] for c in candles][-days - 1:]
    if len(closes) < 10:
        return None
    returns = [math.log(closes[i] / closes[i - 1]) for i in range(1, len(closes))]
    mean = sum(returns) / len(returns)
    variance = sum((r - mean) ** 2 for r in returns) / len(returns)
    return math.sqrt(variance) * math.sqrt(252) * 100


def get_stock_scan_data(nse_symbol, yahoo_symbol, adx_threshold=18.0):
    """Returns scan data dict for one stock, or None if data unavailable."""
    try:
        candles = _fetch_yf_daily(yahoo_symbol, range_="3mo")
        if len(candles) < 20:
            return None
        adx = _adx14(candles)
        if adx is None:
            return None
        spot = candles[-1]["c"]
        hv = _hist_vol(candles)
        return {
            "symbol": nse_symbol,
            "spot": round(spot, 2),
            "adx14_daily": round(adx, 2),
            "hist_vol_pct": round(hv, 2) if hv else None,
            "range_bound": adx < adx_threshold,
        }
    except Exception:
        return None


def cmd_scan_stocks(args):
    """Scans all Nifty 50 F&O stocks for ADX < 18 on daily bars.
    Qualifying stocks are candidates for iron condor entry.
    Use dhan.py lookup to find strike step and lot size before trading."""
    threshold = args.adx_threshold
    qualifying = []
    trending = []
    errors = []

    for nse_sym, yahoo_sym in sorted(STOCK_UNIVERSE.items()):
        if nse_sym in STOCK_BLOCKLIST:
            continue
        data = get_stock_scan_data(nse_sym, yahoo_sym, threshold)
        if data is None:
            errors.append(nse_sym)
            continue
        if data["range_bound"]:
            qualifying.append(data)
        else:
            trending.append({"symbol": nse_sym, "adx14_daily": data["adx14_daily"]})

    qualifying.sort(key=lambda x: x["adx14_daily"])  # lowest ADX first = most range-bound

    result = {
        "adx_threshold": threshold,
        "qualifying_count": len(qualifying),
        "qualifying": qualifying,
        "trending_count": len(trending),
        "trending": trending,
        "errors": errors,
        "note": (
            "For each qualifying stock: use `dhan.py lookup <SYMBOL> <expiry> <strike> CE` "
            "to find strike step and lot size. Use hist_vol_pct instead of India VIX for "
            "estimate-premium on stocks. Target DTE 2-7 days."
        ),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="command", required=True)

    sub.add_parser("scan").set_defaults(func=cmd_scan)

    p = sub.add_parser("spot")
    p.add_argument("instrument", choices=INSTRUMENTS)
    p.set_defaults(func=cmd_spot)

    sub.add_parser("vix").set_defaults(func=cmd_vix)

    p = sub.add_parser("adx")
    p.add_argument("instrument", choices=INSTRUMENTS)
    p.set_defaults(func=cmd_adx)

    p = sub.add_parser("estimate-premium")
    p.add_argument("instrument")  # accepts both index names and stock NSE symbols
    p.add_argument("strike", type=float)
    p.add_argument("option_type", choices=["CE", "PE"])
    p.add_argument("--dte", type=float, default=2.0)
    p.add_argument("--iv", type=float, default=None,
                   help="Override IV% (use hist_vol_pct from scan-stocks for stock symbols)")
    p.set_defaults(func=cmd_estimate_premium)

    p = sub.add_parser("scan-stocks",
                       help="Scan all Nifty 50 F&O stocks for ADX<18 on daily bars")
    p.add_argument("--adx-threshold", type=float, default=18.0)
    p.set_defaults(func=cmd_scan_stocks)

    args = ap.parse_args()
    args.func(args)
