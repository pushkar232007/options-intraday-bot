Force-close or carry-forward every open position at end of day (~3:15-3:20 PM IST).

1. Read all open positions from memory/portfolio.md "Open Paper Positions" table. **While
   TRADING_MODE: paper, this is the only source that matters — do NOT rely on
   `python3 scripts/dhan.py square-off-all` to discover what's open (broker may be broken).**

2. For each open position, estimate the current value using `python3 scripts/market_data.py
   estimate-premium <X> <strike> <CE|PE> --dte <days remaining>` for each of the 4 legs.
   Current unrealized P&L = entry credit (from trade-log.md) - cost-to-close now.

3. **Carry-forward decision** (make this autonomously — no need to message Pushkar for
   straightforward cases):

   **Carry forward if ALL THREE are true:**
   - Position is currently in profit (cost-to-close < entry credit)
   - Original thesis looks intact — ADX was <18 at entry and nothing has broken the setup
     (no large directional move, no spike in VIX suggesting regime change)
   - You will tighten the stop to breakeven (entry credit) before holding — this is
     non-negotiable. Log the new stop clearly in trade-log.md.

   **Always close at EOD if ANY of these apply:**
   - Position is at a loss (cost-to-close >= entry credit) — don't carry forward losers
   - ADX has moved above 18 or a clear trend/reversal is showing — thesis broken
   - DTE = 0 or 1 (expiry today or tomorrow) — gamma risk too high to hold overnight
   - Profit is tiny (< 10% of entry credit) — not worth the overnight gap risk for ₹30

   **When in doubt: close it.** Protecting capital is more important than squeezing extra P&L.

4. For every position being **closed**:
   - **TRADING_MODE: paper**: move the row from "Open Paper Positions" to "Closed Paper
     Positions" in portfolio.md with exit date, cost-to-close, realized P&L = entry credit -
     cost-to-close, reason (PROFIT_TARGET / SL / EOD_SQUAREOFF). Also attempt broker close
     via `python3 scripts/dhan.py place-order` for each leg — broker result is logged but
     does NOT affect the paper close.
   - **TRADING_MODE: live**: place market closing orders via dhan.py, poll until TRADED, then
     update portfolio.md with the real exit price.

5. For every position being **carried forward**:
   - Update portfolio.md: note "CARRIED FORWARD", new tightened stop level, reason.
   - Log in trade-log.md: current unrealized P&L, why carrying forward, new stop.

6. Update portfolio.md: update "Today's P&L" and "Cash (tracked virtual)" for closed trades.

7. Always send an EOD Telegram summary via `python3 scripts/telegram.py` with:
   - Date and time
   - Each position closed: instrument, realized P&L, reason
   - Each position carried forward: instrument, unrealized P&L, new stop level
   - Total day P&L, cumulative P&L, capital remaining
