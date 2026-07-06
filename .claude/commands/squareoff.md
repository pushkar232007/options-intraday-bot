EOD square-off — force-close index positions; stock condors carry forward unless an exit
trigger fired.

1. Read memory/portfolio.md "Open Paper Positions" table and memory/strategy.md exit rules.

---

## INDEX positions (NIFTY / BANKNIFTY / SENSEX)

Index condors are intraday by design. Force-close every index position at EOD unless ALL
three carry-forward conditions are met (rare, should almost never happen):
  - Currently in profit (cost-to-close < entry credit)
  - ADX still <18 and no large directional move / VIX spike since entry
  - Stop will be tightened to breakeven before holding overnight (log this explicitly)

For each index position being closed:
  - TRADING_MODE: paper: remove from "Open Paper Positions", add to "Closed Paper Positions"
    with exit date, cost-to-close, realized P&L = entry credit - cost-to-close, reason
    EOD_SQUAREOFF (or CARRY_FORWARD if held). Attempt broker close via
    `python3 scripts/dhan.py place-order` — broker result is logged but does NOT affect paper close.
  - TRADING_MODE: live: place market closing orders via dhan.py, poll until TRADED, update portfolio.md.

---

## STOCK positions (Nifty 50 F&O symbols)

Stock condors are multi-day trades by design (DTE 2-7, held until target/SL/expiry). **Do NOT
force-close stock positions at EOD.** The 92.4% WR in the backtest came from holding across
multiple days — closing intraday breaks the strategy entirely.

For each stock position, estimate the current cost-to-close:
  `python3 scripts/market_data.py estimate-premium <SYMBOL> <strike> <CE|PE> --dte <days remaining>`
  for each of the 4 legs. Cost-to-close = buy-back short legs - sell long legs.

Close the stock position NOW only if one of these triggers has fired:
  - cost-to-close ≤ 25% of entry credit → close, reason: PROFIT_TARGET
  - cost-to-close ≥ 2.5x entry credit → close, reason: SL
  - Expiry date = today → close, reason: EXPIRY (this is the only EOD-forced close for stocks)
  - Earnings announcement within 5 days of expiry discovered post-entry → close, reason: EARNINGS_RISK

Otherwise → carry forward. Update portfolio.md to note current unrealized P&L and expected
remaining DTE. No tightened-stop requirement for stocks — the 2.5x SL is already the stop,
and theta is the edge; artificially tightening it mid-hold introduces the same false-exit problem
the sweep showed when using 1.0-1.5x SL multiples.

---

## After processing all positions

2. Update portfolio.md: update "Today's P&L" and "Cash (tracked virtual)" for any closed trades.

3. Always send an EOD Telegram summary via `python3 scripts/telegram.py` with:
   - Date
   - Index positions: each closed (instrument, realized P&L, reason) or carried (instrument, unrealized P&L)
   - Stock positions: each closed (trigger reason + P&L) or carried forward (symbol, DTE remaining, unrealized P&L)
   - Total day P&L, cumulative P&L, capital remaining
   Keep it to 5-7 lines.

4. Before finishing: commit and push all memory/ changes to main.
