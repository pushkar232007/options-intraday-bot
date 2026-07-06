Check every open position against the exit rules in memory/strategy.md.

1. Read open positions from memory/portfolio.md "Open Paper Positions" table. **While
   TRADING_MODE: paper, this is the source of truth — do NOT rely on `python3 scripts/dhan.py
   orders` to discover open positions (broker may be broken/sandbox). When TRADING_MODE: live,
   cross-check portfolio.md against `dhan.py orders` and flag any discrepancy.**
2. For each open spread in portfolio.md, estimate the current cost-to-close:
   `python3 scripts/market_data.py estimate-premium <X> <strike> <CE|PE> --dte <days remaining>`
   for each of the 4 legs. Cost-to-close = (short put + short call premiums to BUY back) -
   (long put + long call premiums to SELL). Compare against the entry credit logged in
   memory/trade-log.md using the correct thresholds per instrument type:

   **Index trades (NIFTY / BANKNIFTY / SENSEX):**
   - Cost-to-close <= 50% of entry credit → close now, reason: `PROFIT_TARGET`
   - Cost-to-close >= 2.0x entry credit → close now, reason: `SL`

   **Stock trades (any Nifty 50 F&O symbol):**
   - Cost-to-close <= 25% of entry credit → close now, reason: `PROFIT_TARGET`
   - Cost-to-close >= 2.5x entry credit → close now, reason: `SL`

   Otherwise → leave open, note current unrealized P&L in memory/trade-log.md if
   meaningfully closer to either threshold than last check.
3. To close a paper position:
   - **TRADING_MODE: paper**: remove the row from portfolio.md "Open Paper Positions" table,
     add a row to "Closed Paper Positions" with: exit date, exit credit (cost-to-close from
     step 2), realized P&L = entry credit - cost-to-close, reason. Also try the broker close
     for completeness (`python3 scripts/dhan.py place-order`) but broker success/failure does
     NOT affect the paper close.
   - **TRADING_MODE: live**: place the closing order via dhan.py, poll order-status until
     TRADED, then update portfolio.md with the real exit price.
4. Log every close (or non-action with reason) to memory/trade-log.md.
5. Send a Telegram notification via `python3 scripts/telegram.py` only if a position was
   actually closed (triggered PROFIT_TARGET or SL). Include instrument, realized P&L, reason.
