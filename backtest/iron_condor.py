"""
Iron condor pricing helper: sell a near-OTM put + near-OTM call, buy further-OTM legs
on each side to cap risk. Profits from time decay / low movement, the opposite bet
from naked buying. Net credit received at entry; P&L = entry credit - cost to close
the package later (smaller cost-to-close = more profit, same logic as buying low/
selling high but inverted since you sold first).
"""
from bs_pricer import bs_price


def build_condor(spot, step, short_offset_steps, long_offset_steps):
    """Returns dict of the 4 strikes for a symmetric iron condor around spot."""
    atm = round(spot / step) * step
    return dict(
        short_put=atm - short_offset_steps * step,
        long_put=atm - long_offset_steps * step,
        short_call=atm + short_offset_steps * step,
        long_call=atm + long_offset_steps * step,
    )


def condor_net_value(strikes, spot, dte, iv):
    """Cost to ENTER the condor as a seller = net credit received (positive).
    Same formula gives cost to EXIT/close it later (what you'd have to pay to buy
    it back) - just evaluate at the later spot/dte/iv."""
    short_put_prem = bs_price(spot, strikes["short_put"], dte, iv, "PE")
    long_put_prem = bs_price(spot, strikes["long_put"], dte, iv, "PE")
    short_call_prem = bs_price(spot, strikes["short_call"], dte, iv, "CE")
    long_call_prem = bs_price(spot, strikes["long_call"], dte, iv, "CE")
    net = (short_put_prem - long_put_prem) + (short_call_prem - long_call_prem)
    return net
