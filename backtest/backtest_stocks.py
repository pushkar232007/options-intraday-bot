"""
Stock iron condor scanner backtest using real NSE Bhavcopy settlement prices.

Strategy: same as the validated index strategy — sell iron condors on stocks that
are range-bound (ADX(14) < 18 on daily bars). Instead of pre-selecting stocks,
the scanner checks ALL Nifty 50 F&O stocks daily and trades every one that qualifies.

Key differences from the index backtest:
  - Option prices come from real Bhavcopy settlement data (not Black-Scholes estimates)
  - ADX uses daily bars (not hourly) since Bhavcopy is daily
  - Positions are held until profit target, stop-loss, or expiry (not forced intraday)
  - Spot price from Yahoo Finance daily close is used to determine ATM strike

P&L is reported per-share (lot-size-agnostic) for strategy validation.
Multiply by your lot size to get real rupee P&L once you know the lot size.

Prerequisites:
  python3 fetch_bhavcopy.py          # download 2 years of NSE Bhavcopy files
  python3 bhavcopy_db.py             # build the SQLite index

Usage:
  python3 backtest_stocks.py                             # default params
  python3 backtest_stocks.py --adx-threshold 20         # looser filter
  python3 backtest_stocks.py --min-dte 1 --max-dte 5
  python3 backtest_stocks.py --min-oi 2000              # stricter liquidity
  python3 backtest_stocks.py --dump                     # print every trade
  python3 backtest_stocks.py --refresh-prices           # re-fetch Yahoo Finance data
"""
import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta

sys.path.insert(0, os.path.dirname(__file__))
from indicators import adx_series
import bhavcopy_db as db_mod

# ── Stock universe ────────────────────────────────────────────────────────────
# Nifty 50 F&O stocks: NSE symbol → Yahoo Finance symbol (.NS suffix)
UNIVERSE = {
    "RELIANCE":   "RELIANCE.NS",
    "HDFCBANK":   "HDFCBANK.NS",
    "ICICIBANK":  "ICICIBANK.NS",
    "INFY":       "INFY.NS",
    "TCS":        "TCS.NS",
    "SBIN":       "SBIN.NS",
    "AXISBANK":   "AXISBANK.NS",
    "KOTAKBANK":  "KOTAKBANK.NS",
    "BAJFINANCE": "BAJFINANCE.NS",
    "HINDUNILVR": "HINDUNILVR.NS",
    "LT":         "LT.NS",
    "ITC":        "ITC.NS",
    "TATAMOTORS": "TATAMOTORS.NS",
    "TATASTEEL":  "TATASTEEL.NS",
    "WIPRO":      "WIPRO.NS",
    "HCLTECH":    "HCLTECH.NS",
    "SUNPHARMA":  "SUNPHARMA.NS",
    "NTPC":       "NTPC.NS",
    "POWERGRID":  "POWERGRID.NS",
    "BHARTIARTL": "BHARTIARTL.NS",
    "ADANIENT":   "ADANIENT.NS",
    "ADANIPORTS": "ADANIPORTS.NS",
    "BAJAJFINSV": "BAJAJFINSV.NS",
    "MARUTI":     "MARUTI.NS",
    "TITAN":      "TITAN.NS",
    "ASIANPAINT": "ASIANPAINT.NS",
    "DRREDDY":    "DRREDDY.NS",
    "CIPLA":      "CIPLA.NS",
    "HINDALCO":   "HINDALCO.NS",
    "JSWSTEEL":   "JSWSTEEL.NS",
    "HEROMOTOCO": "HEROMOTOCO.NS",
    "EICHERMOT":  "EICHERMOT.NS",
    "TECHM":      "TECHM.NS",
    "ULTRACEMCO": "ULTRACEMCO.NS",
    "GRASIM":     "GRASIM.NS",
    "COALINDIA":  "COALINDIA.NS",
    "BPCL":       "BPCL.NS",
    "ONGC":       "ONGC.NS",
    "INDUSINDBK": "INDUSINDBK.NS",
    "APOLLOHOSP": "APOLLOHOSP.NS",
    "TATACONSUM": "TATACONSUM.NS",
    "NESTLEIND":  "NESTLEIND.NS",
    "BEL":        "BEL.NS",
    "HDFCLIFE":   "HDFCLIFE.NS",
    "SBILIFE":    "SBILIFE.NS",
    "BAJAJ-AUTO": "BAJAJ-AUTO.NS",
    "HINDZINC":   "HINDZINC.NS",
    "VEDL":       "VEDL.NS",
    "NMDC":       "NMDC.NS",
    "BANKBARODA": "BANKBARODA.NS",
    "PNB":        "PNB.NS",
    "CANBK":      "CANBK.NS",
    "SIEMENS":    "SIEMENS.NS",
    "ABB":        "ABB.NS",
    "PIDILITIND": "PIDILITIND.NS",
    "DMART":      "DMART.NS",
    "ZOMATO":     "ZOMATO.NS",
    "PAYTM":      "PAYTM.NS",
    "NYKAA":      "NYKAA.NS",
}

STOCK_DATA_DIR = os.path.join(os.path.dirname(__file__), "data", "stocks")

# Strategy constants (mirrors index strategy)
SHORT_OFFSET_STEPS = 2    # strike steps OTM for the sold legs
LONG_OFFSET_STEPS = 4     # strike steps OTM for the protective legs
PROFIT_TARGET_PCT = 0.50  # exit when cost-to-close drops to 50% of entry credit
SL_MULTIPLE = 2.0         # exit when cost-to-close reaches 2x entry credit


# ── Stock price data ──────────────────────────────────────────────────────────

def _fetch_yahoo(yahoo_symbol: str) -> list:
    url = ("https://query1.finance.yahoo.com/v8/finance/chart/" +
           urllib.parse.quote(yahoo_symbol) + "?" +
           urllib.parse.urlencode({"range": "3y", "interval": "1d"}))
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        body = json.loads(resp.read())
    result = body["chart"]["result"]
    if not result:
        return []
    r = result[0]
    ts = r["timestamp"]
    q = r["indicators"]["quote"][0]
    candles = []
    for i, t in enumerate(ts):
        c = q["close"][i]
        if c is None:
            continue
        candles.append({
            "t": t,
            "o": q["open"][i] or c,
            "h": q["high"][i] or c,
            "l": q["low"][i] or c,
            "c": c,
        })
    return candles


def load_stock_candles(nse_sym: str, yahoo_sym: str,
                       refresh: bool = False) -> list:
    cache = os.path.join(STOCK_DATA_DIR, f"{nse_sym}_1d.json")
    if not refresh and os.path.exists(cache):
        with open(cache) as f:
            return json.load(f)
    candles = _fetch_yahoo(yahoo_sym)
    os.makedirs(STOCK_DATA_DIR, exist_ok=True)
    with open(cache, "w") as f:
        json.dump(candles, f)
    return candles


def _epoch_to_date_str(ts: int) -> str:
    """UTC epoch → IST date string 'YYYY-MM-DD' (IST = UTC+5:30)."""
    return datetime.utcfromtimestamp(ts + 19800).strftime("%Y-%m-%d")


def build_price_adx_lookup(candles: list) -> tuple[dict, dict]:
    """Returns ({date_str: close}, {date_str: adx_value}) from daily candles."""
    highs = [c["h"] for c in candles]
    lows = [c["l"] for c in candles]
    closes = [c["c"] for c in candles]
    adx14 = adx_series(highs, lows, closes, 14)
    price_lookup = {}
    adx_lookup = {}
    for i, c in enumerate(candles):
        ds = _epoch_to_date_str(c["t"])
        price_lookup[ds] = c["c"]
        if adx14[i] is not None:
            adx_lookup[ds] = adx14[i]
    return price_lookup, adx_lookup


# ── Condor helpers ────────────────────────────────────────────────────────────

def _infer_strike_step(strikes: list) -> float:
    """Infer strike step from the minimum gap between adjacent strikes."""
    if len(strikes) < 2:
        return 0.0
    diffs = [strikes[i + 1] - strikes[i] for i in range(len(strikes) - 1)]
    return min(diffs)


def _find_atm_and_step(conn, symbol, trade_date, expiry, spot):
    """
    Finds ATM strike (closest to spot in Bhavcopy) and the strike step.
    Returns (atm, step) or (None, None) if insufficient data.
    """
    ce_strikes = db_mod.available_strikes(conn, symbol, trade_date, expiry, "CE")
    pe_strikes = db_mod.available_strikes(conn, symbol, trade_date, expiry, "PE")
    all_strikes = sorted(set(ce_strikes) | set(pe_strikes))
    if len(all_strikes) < 5:
        return None, None
    atm = min(all_strikes, key=lambda s: abs(s - spot))
    step = _infer_strike_step(all_strikes)
    return atm, step


def _find_expiry(conn, symbol, trade_date: str, min_dte: int, max_dte: int):
    """Finds expiry with DTE in [min_dte, max_dte]. Prefers shortest DTE."""
    td = datetime.strptime(trade_date, "%Y-%m-%d").date()
    expiries = db_mod.available_expiries(conn, symbol, trade_date)
    candidates = []
    for exp_str in expiries:
        exp_date = datetime.strptime(exp_str, "%Y-%m-%d").date()
        dte = (exp_date - td).days
        if min_dte <= dte <= max_dte:
            candidates.append((dte, exp_str))
    if not candidates:
        return None, None
    candidates.sort()
    return candidates[0][1], candidates[0][0]


def _get_condor_prices(conn, symbol, trade_date, expiry, strikes):
    """Returns (sp, lp, sc, lc) settle prices or None if any is missing."""
    sp = db_mod.get_settle(conn, symbol, trade_date, expiry, "PE", strikes["sp"])
    lp = db_mod.get_settle(conn, symbol, trade_date, expiry, "PE", strikes["lp"])
    sc = db_mod.get_settle(conn, symbol, trade_date, expiry, "CE", strikes["sc"])
    lc = db_mod.get_settle(conn, symbol, trade_date, expiry, "CE", strikes["lc"])
    if any(x is None for x in (sp, lp, sc, lc)):
        return None
    return sp, lp, sc, lc


# ── Main backtest ─────────────────────────────────────────────────────────────

def run(adx_threshold: float = 18.0,
        min_dte: int = 2,
        max_dte: int = 7,
        min_oi: int = 1000,
        refresh_prices: bool = False,
        verbose: bool = True) -> dict:

    # Load Bhavcopy database
    if verbose:
        print("Connecting to Bhavcopy database...")
    conn = db_mod.connect()
    all_dates = db_mod.trading_dates(conn)
    if verbose:
        print(f"  {len(all_dates)} trading days in database "
              f"({all_dates[0]} → {all_dates[-1]})")

    # Load stock price + ADX data
    if verbose:
        print("Loading stock price data from Yahoo Finance...")
    stock_price = {}   # {symbol: {date_str: close}}
    stock_adx = {}     # {symbol: {date_str: adx_val}}
    for nse_sym, yahoo_sym in sorted(UNIVERSE.items()):
        try:
            candles = load_stock_candles(nse_sym, yahoo_sym, refresh=refresh_prices)
            if len(candles) >= 20:
                price_lk, adx_lk = build_price_adx_lookup(candles)
                stock_price[nse_sym] = price_lk
                stock_adx[nse_sym] = adx_lk
        except Exception as e:
            if verbose:
                print(f"  {nse_sym}: {e}")
    if verbose:
        print(f"  {len(stock_adx)} stocks loaded")

    # Map date→index for fast "next date" lookup
    date_to_idx = {d: i for i, d in enumerate(all_dates)}

    trades = []

    for trade_date in all_dates:
        bhavcopy_symbols = set(db_mod.symbols_on_date(conn, trade_date))

        for symbol in sorted(UNIVERSE.keys()):
            # Must have bhavcopy data, price data, and ADX data
            if symbol not in bhavcopy_symbols:
                continue
            if symbol not in stock_adx:
                continue
            adx_val = stock_adx[symbol].get(trade_date)
            if adx_val is None or adx_val >= adx_threshold:
                continue  # trending or no data — skip

            spot = stock_price[symbol].get(trade_date)
            if spot is None:
                continue

            # Find a suitable near-expiry
            expiry, dte = _find_expiry(conn, symbol, trade_date, min_dte, max_dte)
            if expiry is None:
                continue

            # Determine ATM and strike step from Bhavcopy
            atm, step = _find_atm_and_step(conn, symbol, trade_date, expiry, spot)
            if atm is None or step <= 0:
                continue

            # Build iron condor strikes
            strikes = {
                "sp": atm - SHORT_OFFSET_STEPS * step,
                "lp": atm - LONG_OFFSET_STEPS * step,
                "sc": atm + SHORT_OFFSET_STEPS * step,
                "lc": atm + LONG_OFFSET_STEPS * step,
            }

            # Entry prices from Bhavcopy settle
            entry_prices = _get_condor_prices(conn, symbol, trade_date, expiry, strikes)
            if entry_prices is None:
                continue
            sp_e, lp_e, sc_e, lc_e = entry_prices
            entry_credit = (sp_e - lp_e) + (sc_e - lc_e)
            if entry_credit <= 0:
                continue

            # Liquidity filter on the short legs (the legs with most risk)
            sp_oi = db_mod.get_open_interest(
                conn, symbol, trade_date, expiry, "PE", strikes["sp"])
            sc_oi = db_mod.get_open_interest(
                conn, symbol, trade_date, expiry, "CE", strikes["sc"])
            if sp_oi < min_oi or sc_oi < min_oi:
                continue

            # Max loss per share (for reference / capital sizing)
            width = (LONG_OFFSET_STEPS - SHORT_OFFSET_STEPS) * step
            max_loss_per_share = width - entry_credit
            if max_loss_per_share <= 0:
                continue

            # Exit loop: check each subsequent Bhavcopy day until profit target,
            # stop-loss, or expiry. Hold overnight is the default (daily Bhavcopy).
            exit_cost = None
            exit_date = None
            exit_reason = "EXPIRY"

            start_idx = date_to_idx.get(trade_date, -1) + 1
            for future_date in all_dates[start_idx:]:
                prices_now = _get_condor_prices(
                    conn, symbol, future_date, expiry, strikes)
                if prices_now is None:
                    # No option data for this date — may be past expiry
                    if future_date >= expiry:
                        # Options expired — settle at intrinsic (data gone = worth ~0)
                        exit_cost = 0.0
                        exit_date = future_date
                        exit_reason = "EXPIRY_ZERO"
                    continue

                sp_n, lp_n, sc_n, lc_n = prices_now
                cost_now = (sp_n - lp_n) + (sc_n - lc_n)

                # Update running exit (EOD hold default)
                exit_cost = cost_now
                exit_date = future_date
                exit_reason = "EOD_HOLD"

                if cost_now <= entry_credit * (1 - PROFIT_TARGET_PCT):
                    exit_reason = "PROFIT_TARGET"
                    break
                if cost_now >= entry_credit * SL_MULTIPLE:
                    exit_reason = "SL"
                    break
                if future_date >= expiry:
                    exit_reason = "EXPIRY"
                    break

            if exit_cost is None:
                continue  # no exit found — skip

            pnl_per_share = entry_credit - exit_cost

            trades.append({
                "entry_date":       trade_date,
                "exit_date":        exit_date,
                "symbol":           symbol,
                "expiry":           expiry,
                "dte_at_entry":     dte,
                "spot":             spot,
                "atm":              atm,
                "step":             step,
                "strikes":          strikes,
                "adx":              round(adx_val, 2),
                "entry_credit":     round(entry_credit, 2),
                "exit_cost":        round(exit_cost, 2),
                "pnl_per_share":    round(pnl_per_share, 2),
                "max_loss_per_share": round(max_loss_per_share, 2),
                "short_put_oi":     sp_oi,
                "short_call_oi":    sc_oi,
                "exit_reason":      exit_reason,
            })

    conn.close()
    return {"trades": trades, "all_dates": all_dates}


# ── Summary ───────────────────────────────────────────────────────────────────

def summarize(result: dict, dump: bool = False):
    trades = result["trades"]
    all_dates = result["all_dates"]
    n = len(trades)

    print("\n" + "=" * 55)
    print("  STOCK IRON CONDOR BACKTEST — Nifty 50 F&O Universe")
    print("=" * 55)
    print(f"  Trading days in Bhavcopy: {len(all_dates)}")
    print(f"  ({all_dates[0]} → {all_dates[-1]})")
    print(f"  Total trades:             {n}")

    if n == 0:
        print("  No trades — check filters (--min-oi, --adx-threshold, --min-dte)")
        return

    wins = [t for t in trades if t["pnl_per_share"] > 0]
    losses = [t for t in trades if t["pnl_per_share"] <= 0]
    total_pnl = sum(t["pnl_per_share"] for t in trades)
    avg_credit = sum(t["entry_credit"] for t in trades) / n
    avg_pnl = total_pnl / n

    num_months = len(all_dates) / 21
    trades_pm = n / num_months if num_months > 0 else 0

    print(f"  Win rate:                 {len(wins)/n*100:.1f}%  "
          f"({len(wins)}W / {len(losses)}L)")
    print(f"  Avg entry credit:         ₹{avg_credit:.2f}/share")
    print(f"  Avg P&L per trade:        ₹{avg_pnl:.2f}/share")
    print(f"  Total P&L (all trades):   ₹{total_pnl:.2f}/share-sum")
    print(f"  Trades per month:         {trades_pm:.1f}")

    # Exit reason breakdown
    reasons = {}
    for t in trades:
        reasons[t["exit_reason"]] = reasons.get(t["exit_reason"], 0) + 1
    print(f"\n  Exit reasons:")
    for r, cnt in sorted(reasons.items(), key=lambda x: -x[1]):
        print(f"    {r:20s}: {cnt:4d}  ({cnt/n*100:.0f}%)")

    # DTE breakdown
    dte_groups = {}
    for t in trades:
        dte_groups.setdefault(t["dte_at_entry"], []).append(t["pnl_per_share"])
    print(f"\n  Results by DTE at entry:")
    for dte in sorted(dte_groups):
        pnls = dte_groups[dte]
        w = sum(1 for p in pnls if p > 0)
        print(f"    DTE {dte}: {len(pnls):3d} trades, "
              f"{w/len(pnls)*100:.0f}% WR, "
              f"avg ₹{sum(pnls)/len(pnls):.2f}/share")

    # Per-stock breakdown (top 20 by trade count)
    by_sym = {}
    for t in trades:
        by_sym.setdefault(t["symbol"], []).append(t)
    print(f"\n  Per-stock (top 20 by trade count):")
    print(f"  {'Symbol':12s}  {'Trades':>6}  {'WR':>6}  {'Avg P&L/sh':>11}  {'Total P&L/sh':>13}")
    print(f"  {'-'*12}  {'-'*6}  {'-'*6}  {'-'*11}  {'-'*13}")
    for sym, sym_trades in sorted(by_sym.items(),
                                   key=lambda x: -len(x[1]))[:20]:
        w = sum(1 for t in sym_trades if t["pnl_per_share"] > 0)
        tp = sum(t["pnl_per_share"] for t in sym_trades)
        ap = tp / len(sym_trades)
        print(f"  {sym:12s}  {len(sym_trades):6d}  "
              f"{w/len(sym_trades)*100:5.0f}%  "
              f"  ₹{ap:+8.2f}  ₹{tp:+12.2f}")

    if dump:
        print(f"\n  All trades:")
        print(f"  {'Entry':10}  {'Symbol':12}  {'Expiry':10}  "
              f"{'DTE':>3}  {'ADX':>5}  {'Credit':>7}  {'Exit$':>7}  "
              f"{'P&L/sh':>8}  {'Reason'}")
        for t in trades:
            print(f"  {t['entry_date']}  {t['symbol']:12}  {t['expiry']}  "
                  f"{t['dte_at_entry']:3d}  {t['adx']:5.1f}  "
                  f"₹{t['entry_credit']:6.2f}  ₹{t['exit_cost']:6.2f}  "
                  f"₹{t['pnl_per_share']:+7.2f}  {t['exit_reason']}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Stock iron condor backtest using NSE Bhavcopy prices")
    ap.add_argument("--adx-threshold", type=float, default=18.0,
                    help="Max ADX to qualify as range-bound (default 18)")
    ap.add_argument("--min-dte", type=int, default=2,
                    help="Min days to expiry at entry (default 2)")
    ap.add_argument("--max-dte", type=int, default=7,
                    help="Max days to expiry at entry (default 7)")
    ap.add_argument("--min-oi", type=int, default=1000,
                    help="Min open interest on short legs (default 1000)")
    ap.add_argument("--refresh-prices", action="store_true",
                    help="Re-fetch stock price data from Yahoo Finance")
    ap.add_argument("--dump", action="store_true",
                    help="Print every individual trade")
    args = ap.parse_args()

    result = run(
        adx_threshold=args.adx_threshold,
        min_dte=args.min_dte,
        max_dte=args.max_dte,
        min_oi=args.min_oi,
        refresh_prices=args.refresh_prices,
    )
    summarize(result, dump=args.dump)
