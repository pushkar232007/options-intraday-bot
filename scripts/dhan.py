#!/usr/bin/env python3
"""
Thin CLI wrapper around the DhanHQ v2 API (sandbox by default).

IMPORTANT - verify before first real use: the endpoint paths and request/response
shapes below are written from general knowledge of the DhanHQ v2 API and have NOT been
tested against a live sandbox (no credentials were available while writing this). Before
relying on this script, get real DHAN_CLIENT_ID/DHAN_ACCESS_TOKEN sandbox credentials and
cross-check every endpoint against https://dhanhq.co/docs/v2/ - fix any path/field
mismatches you find there, that source is authoritative, this file is not.

Usage:
  python3 scripts/dhan.py funds
  python3 scripts/dhan.py positions
  python3 scripts/dhan.py option-chain NIFTY <expiry YYYY-MM-DD>
  python3 scripts/dhan.py quote NIFTY
  python3 scripts/dhan.py place-spread --instrument NIFTY --expiry 2026-07-02 \\
      --short-put 24500 --long-put 24400 --short-call 24700 --long-call 24800 --lots 1
  python3 scripts/dhan.py square-off-all
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error

BASE_URL = os.environ.get("DHAN_BASE_URL", "https://sandbox.dhan.co")  # verify against current docs
API_PREFIX = "/v2"


def _headers():
    client_id = os.environ.get("DHAN_CLIENT_ID")
    access_token = os.environ.get("DHAN_ACCESS_TOKEN")
    if not client_id or not access_token:
        sys.exit("Missing DHAN_CLIENT_ID / DHAN_ACCESS_TOKEN environment variables.")
    return {
        "Content-Type": "application/json",
        "access-token": access_token,
        "client-id": client_id,
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


def cmd_option_chain(args):
    body = {"UnderlyingScrip": args.instrument, "Expiry": args.expiry}
    print(json.dumps(_request("POST", "/optionchain", body), indent=2))


def cmd_quote(args):
    body = {"NSE_EQ": [args.instrument]}  # segment/key shape - verify against docs
    print(json.dumps(_request("POST", "/marketfeed/quote", body), indent=2))


def _place_leg(instrument, expiry, strike, option_type, transaction_type, lots):
    body = {
        "transactionType": transaction_type,       # "BUY" | "SELL"
        "exchangeSegment": "NSE_FNO",
        "productType": "INTRADAY",
        "orderType": "MARKET",
        "validity": "DAY",
        "tradingSymbol": f"{instrument}-{expiry}-{strike}-{option_type}",  # verify exact symbol format
        "quantity": lots,
    }
    return _request("POST", "/orders", body)


def cmd_place_spread(args):
    """Places all 4 legs of an iron condor. NOT atomic - if a later leg fails, you can be
    left with a partial position. Check `positions` immediately after and square off
    manually (or via square-off-all) if any leg failed."""
    legs = [
        ("PE", "SELL", args.short_put),
        ("PE", "BUY", args.long_put),
        ("CE", "SELL", args.short_call),
        ("CE", "BUY", args.long_call),
    ]
    results = []
    for option_type, txn, strike in legs:
        res = _place_leg(args.instrument, args.expiry, strike, option_type, txn, args.lots)
        results.append(res)
        print(f"{txn} {args.instrument} {strike}{option_type}: {json.dumps(res)}")
    return results


def cmd_square_off_all(args):
    positions = _request("GET", "/positions")
    for pos in positions if isinstance(positions, list) else positions.get("data", []):
        qty = pos.get("netQty") or pos.get("quantity") or 0
        if not qty:
            continue
        txn = "SELL" if qty > 0 else "BUY"
        body = {
            "transactionType": txn,
            "exchangeSegment": pos.get("exchangeSegment", "NSE_FNO"),
            "productType": "INTRADAY",
            "orderType": "MARKET",
            "validity": "DAY",
            "tradingSymbol": pos.get("tradingSymbol"),
            "quantity": abs(qty),
        }
        res = _request("POST", "/orders", body)
        print(f"square-off {pos.get('tradingSymbol')}: {json.dumps(res)}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="command", required=True)

    sub.add_parser("funds").set_defaults(func=cmd_funds)
    sub.add_parser("positions").set_defaults(func=cmd_positions)
    sub.add_parser("orders").set_defaults(func=cmd_orders)

    p = sub.add_parser("option-chain")
    p.add_argument("instrument")
    p.add_argument("expiry")
    p.set_defaults(func=cmd_option_chain)

    p = sub.add_parser("quote")
    p.add_argument("instrument")
    p.set_defaults(func=cmd_quote)

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

    args = ap.parse_args()
    args.func(args)
