Force-close every open position at end of day.

1. Read all open positions from memory/portfolio.md "Open Paper Positions" table. **While
   TRADING_MODE: paper, this is the only source that matters — do NOT rely on
   `python3 scripts/dhan.py square-off-all` to discover what's open (broker may be broken).**
2. For each open paper position, estimate the cost-to-close at current prices:
   `python3 scripts/market_data.py estimate-premium <X> <strike> <CE|PE> --dte <days remaining>`
   for each of the 4 legs. Realized P&L = entry credit (from trade-log.md) - cost-to-close.
3. Check carry-forward conditions (all 3 must be true to NOT square off):
   - Position is currently in unrealized profit (cost-to-close < entry credit)
   - Original setup thesis still intact (ADX still < 18, no reversal signal)
   - You are willing to tighten stop before holding overnight
   If ANY position qualifies for carry-forward, message the human via scripts/telegram.py and
   wait for confirmation — do not decide alone.
4. For every position NOT carried forward:
   - **TRADING_MODE: paper**: move the row from "Open Paper Positions" to "Closed Paper
     Positions" in portfolio.md with exit date, cost-to-close, realized P&L, reason: `EOD_SQUAREOFF`.
     Also attempt broker close via `python3 scripts/dhan.py place-order` for each leg —
     broker result is logged but does NOT affect the paper close.
   - **TRADING_MODE: live**: place market closing orders via dhan.py, poll until TRADED, then
     update portfolio.md.
5. Update portfolio.md: clear "Open Paper Positions", add to realized P&L total, update "Today's
   P&L" and "Cash (tracked virtual)".
6. Log the day's final state to memory/trade-log.md: all closed trades with entry credit,
   cost-to-close, realized P&L, reason.
7. Always send an EOD Telegram summary via `python3 scripts/telegram.py` with: date, positions
   closed, total day P&L, cumulative P&L, capital remaining.
