#!/usr/bin/env python3
"""
Thin CLI wrapper around the DhanHQ v2 API.

Verified 2026-06-29 against a real Dhan Sandbox account (funds/positions/orders/order
placement all tested end-to-end and working as written below). Two things that are NOT
covered by the free sandbox, confirmed by testing (404s on every market-data path tried):
  - Option chain (/v2/optionchain, /v2/optionchain/expirylist)
  - Market quotes (/v2/marketfeed/ltp, /v2/marketfeed/quote)
These need the separate paid Data API subscription (~Rs499/month) tied to a real account -
sandbox only simulates order/fund/position management, not market data. So `option-chain`
and `quote` below will 404 against the sandbox; they're written for when you go live with a
Data API subscription, but UNTESTED - re-verify then.

Known sandbox quirk: `/v2/positions` returned `[]` even immediately after a trade filled
(`/v2/orders` showed `orderStatus: "TRADED"` for the same order). Don't assume `positions`
reflects reality in sandbox - cross-check against `orders` if something looks off.

Usage:
  python3 scripts/dhan.py funds
  python3 scripts/dhan.py positions
  python3 scripts/dhan.py orders
  python3 scripts/dhan.py lookup NIFTY 2026-06-30 24000 CE      # find a contract's securityId
  python3 scripts/dhan.py place-order --security-id 71472 --txn BUY --qty 65
  python3 scripts/dhan.py place-spread --instrument NIFTY --expiry 2026-06-30 \\
      --short-put 23900 --long-put 23800 --short-call 24100 --long-call 24200 --lots 1
  python3 scripts/dhan.py square-off-all
"""
import argparse
import csv
import io
import json
import os
import sys
import urllib.request
import urllib.error

BASE_URL = os.environ.get("DHAN_BASE_URL", "https://sandbox.dhan.co")
API_PREFIX = "/v2"

# Verified 2026-06-29 against Dhan's published instrument master
# (https://images.dhan.co/api-data/api-scrip-master-detailed.csv). The index itself (for
# spot-level reference) uses segment IDX_I; option contracts use NSE_FNO/BSE_FNO with their
# own per-contract securityId looked up via `lookup` below - these don't change.
INDEX_SECURITY_ID = {"NIFTY": 13, "BANKNIFTY": 25, "SENSEX": 51}
INDEX_SEGMENT = "IDX_I"

SCRIP_MASTER_URL = "https://images.dhan.co/api-data/api-scrip-master-detailed.csv"
SCRIP_MASTER_CACHE = os.path.join(os.path.dirname(__file__), ".scrip_master_cache.csv")


def _client_id():
    client_id = os.environ.get("DHAN_CLIENT_ID")
    if not client_id:
        sys.exit("Missing DHAN_CLIENT_ID environment variable.")
    return client_id


def _headers():
    access_token = os.environ.get("DHAN_ACCESS_TOKEN")
    if not access_token:
        sys.exit("Missing DHAN_ACCESS_TOKEN environment variable.")
    return {
        "Content-Type": "application/json",
        "access-token": access_token,
        "client-id": _client_id(),
    }


def _request(method, path, body=None):
    url = BASE_URL + API_PREFIX + path
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=_headers(), method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read() or b"{}")
    except urllib.error.HTTPError as e:
        sys.exit(f"Dhan API error {e.code}: {e.read().decode()}")


def cmd_funds(args):
    print(json.dumps(_request("GET", "/fundlimit"), indent=2))


def cmd_positions(args):
    print(json.dumps(_request("GET", "/positions"), indent=2))


def cmd_orders(args):
    print(json.dumps(_request("GET", "/orders"), indent=2))


def cmd_order_status(args):
    print(json.dumps(_request("GET", f"/orders/{args.order_id}"), indent=2))


def _load_scrip_master(refresh=False):
    if refresh or not os.path.exists(SCRIP_MASTER_CACHE):
        req = urllib.request.Request(SCRIP_MASTER_URL)
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read()
        with open(SCRIP_MASTER_CACHE, "wb") as f:
            f.write(raw)
    with open(SCRIP_MASTER_CACHE, newline="") as f:
        return list(csv.DictReader(f))


def find_security_id(underlying, expiry, strike, option_type, refresh=False):
    """underlying: NIFTY/BANKNIFTY/SENSEX. expiry: YYYY-MM-DD. strike: number. option_type: CE/PE."""
    rows = _load_scrip_master(refresh=refresh)
    for row in rows:
        if (row["UNDERLYING_SYMBOL"] == underlying and row["INSTRUMENT"] == "OPTIDX"
                and row["SM_EXPIRY_DATE"] == expiry and row["OPTION_TYPE"] == option_type
                and abs(float(row["STRIKE_PRICE"]) - float(strike)) < 0.01):
            return row["SECURITY_ID"], row["EXCH_ID"], float(row["LOT_SIZE"])
    return None, None, None


def cmd_lookup(args):
    security_id, exch, lot_size = find_security_id(
        args.underlying, args.expiry, args.strike, args.option_type, refresh=args.refresh)
    if security_id is None:
        sys.exit(f"No contract found for {args.underlying} {args.expiry} {args.strike}{args.option_type}. "
                  "Try --refresh to re-download the instrument master, or double-check the expiry date exists.")
    print(json.dumps({"securityId": security_id, "exchange": exch, "lotSize": lot_size}))


def _exchange_segment(exch):
    return "NSE_FNO" if exch == "NSE" else "BSE_FNO"


def _place_order(security_id, exchange_segment, transaction_type, qty):
    body = {
        "dhanClientId": _client_id(),
        "transactionType": transaction_type,  # "BUY" | "SELL"
        "exchangeSegment": exchange_segment,
        "productType": "INTRADAY",
        "orderType": "MARKET",
        "validity": "DAY",
        "securityId": str(security_id),
        "quantity": int(qty),
    }
    return _request("POST", "/orders", body)


def cmd_place_order(args):
    res = _place_order(args.security_id, args.exchange_segment, args.txn, args.qty)
    print(json.dumps(res))


def cmd_place_spread(args):
    """Places all 4 legs of an iron condor. NOT atomic - if a later leg fails, you can be
    left with a partial position. Check `orders` immediately after (not `positions` - see
    the sandbox quirk noted at the top of this file) and square off manually if any leg failed."""
    legs = [("PE", "SELL", args.short_put), ("PE", "BUY", args.long_put),
            ("CE", "SELL", args.short_call), ("CE", "BUY", args.long_call)]
    results = []
    for option_type, txn, strike in legs:
        security_id, exch, lot_size = find_security_id(args.instrument, args.expiry, strike, option_type)
        if security_id is None:
            print(f"SKIPPED {txn} {args.instrument} {strike}{option_type}: no matching contract found")
            results.append(None)
            continue
        qty = args.lots * int(lot_size)
        res = _place_order(security_id, _exchange_segment(exch), txn, qty)
        results.append(res)
        print(f"{txn} {args.instrument} {strike}{option_type} (qty {qty}): {json.dumps(res)}")
    return results


def cmd_square_off_all(args):
    """Closes every open position by reversing it. Relies on `orders` (filled BUY/SELL net
    per securityId) rather than `positions`, since `positions` was empty in sandbox testing
    even right after a fill - re-verify this is still necessary once live."""
    orders = _request("GET", "/orders")
    net_qty = {}
    meta = {}
    for o in orders:
        if o.get("orderStatus") != "TRADED":
            continue
        sid = o["securityId"]
        qty = int(o.get("filledQty", o.get("quantity", 0)))
        sign = 1 if o["transactionType"] == "BUY" else -1
        net_qty[sid] = net_qty.get(sid, 0) + sign * qty
        meta[sid] = o["exchangeSegment"]
    for sid, qty in net_qty.items():
        if qty == 0:
            continue
        txn = "SELL" if qty > 0 else "BUY"
        res = _place_order(sid, meta[sid], txn, abs(qty))
        print(f"square-off securityId={sid} qty={abs(qty)} via {txn}: {json.dumps(res)}")


def cmd_option_chain(args):
    """UNTESTED against sandbox - confirmed 404 there. Needs a live account + Data API
    subscription. Re-verify the request/response shape against https://dhanhq.co/docs/v2/
    once you have that, before trusting this."""
    scrip = INDEX_SECURITY_ID.get(args.instrument)
    if scrip is None:
        sys.exit(f"Unknown instrument {args.instrument!r} - expected NIFTY/BANKNIFTY/SENSEX.")
    body = {"UnderlyingScrip": scrip, "UnderlyingSeg": INDEX_SEGMENT, "Expiry": args.expiry}
    print(json.dumps(_request("POST", "/optionchain", body), indent=2))


def cmd_quote(args):
    """UNTESTED against sandbox - confirmed 404 there. See cmd_option_chain's note."""
    scrip = INDEX_SECURITY_ID.get(args.instrument)
    if scrip is None:
        sys.exit(f"Unknown instrument {args.instrument!r} - expected NIFTY/BANKNIFTY/SENSEX.")
    body = {INDEX_SEGMENT: [scrip]}
    print(json.dumps(_request("POST", "/marketfeed/quote", body), indent=2))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="command", required=True)

    sub.add_parser("funds").set_defaults(func=cmd_funds)
    sub.add_parser("positions").set_defaults(func=cmd_positions)
    sub.add_parser("orders").set_defaults(func=cmd_orders)

    p = sub.add_parser("order-status")
    p.add_argument("order_id")
    p.set_defaults(func=cmd_order_status)

    p = sub.add_parser("lookup")
    p.add_argument("underlying")
    p.add_argument("expiry")
    p.add_argument("strike", type=float)
    p.add_argument("option_type", choices=["CE", "PE"])
    p.add_argument("--refresh", action="store_true", help="re-download the instrument master")
    p.set_defaults(func=cmd_lookup)

    p = sub.add_parser("place-order")
    p.add_argument("--security-id", required=True)
    p.add_argument("--exchange-segment", default="NSE_FNO")
    p.add_argument("--txn", required=True, choices=["BUY", "SELL"])
    p.add_argument("--qty", type=int, required=True)
    p.set_defaults(func=cmd_place_order)

    p = sub.add_parser("place-spread")
    p.add_argument("--instrument", required=True)
    p.add_argument("--expiry", required=True)
    p.add_argument("--short-put", type=float, required=True)
    p.add_argument("--long-put", type=float, required=True)
    p.add_argument("--short-call", type=float, required=True)
    p.add_argument("--long-call", type=float, required=True)
    p.add_argument("--lots", type=int, default=1)
    p.set_defaults(func=cmd_place_spread)

    sub.add_parser("square-off-all").set_defaults(func=cmd_square_off_all)

    p = sub.add_parser("option-chain")
    p.add_argument("instrument")
    p.add_argument("expiry")
    p.set_defaults(func=cmd_option_chain)

    p = sub.add_parser("quote")
    p.add_argument("instrument")
    p.set_defaults(func=cmd_quote)

    args = ap.parse_args()
    args.func(args)
