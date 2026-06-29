"""
Black-Scholes option pricer used to *simulate* option premiums from real underlying
price + real India VIX, since real historical option-chain premiums aren't freely
available. This is an approximation: real options have skew/smile, bid-ask spread,
and liquidity effects this model ignores. Good enough to sanity-check whether the
entry/exit signal logic has any edge at all before trusting it with real premium data
from Dhan's live option chain.
"""
import math


def _norm_cdf(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0


def bs_price(spot, strike, days_to_expiry, iv_pct, option_type, r=0.06):
    """iv_pct: annualized IV in percent (e.g. India VIX value, ~13.5 means 13.5%)."""
    t = max(days_to_expiry, 0.25) / 365.0  # floor so same-day-expiry doesn't divide by ~0
    sigma = max(iv_pct, 1.0) / 100.0
    d1 = (math.log(spot / strike) + (r + sigma ** 2 / 2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)
    if option_type == "CE":
        price = spot * _norm_cdf(d1) - strike * math.exp(-r * t) * _norm_cdf(d2)
    elif option_type == "PE":
        price = strike * math.exp(-r * t) * _norm_cdf(-d2) - spot * _norm_cdf(-d1)
    else:
        raise ValueError("option_type must be CE or PE")
    return max(price, 0.05)  # options don't trade at exactly 0


def atm_strike(spot, step):
    return round(spot / step) * step


STRIKE_STEP = {"NIFTY": 50, "BANKNIFTY": 100, "SENSEX": 100}
# Verified 2026-06-29 against Dhan's published instrument master (api-scrip-master-detailed.csv) -
# these were guesses before (75/35/20) and were wrong for NIFTY/BANKNIFTY. Re-verify periodically;
# lot sizes get revised by the exchange from time to time.
LOT_SIZE = {"NIFTY": 65, "BANKNIFTY": 30, "SENSEX": 20}
