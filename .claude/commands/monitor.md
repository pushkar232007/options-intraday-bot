Check every open position against the exit rules in memory/strategy.md.

1. Read open positions from memory/portfolio.md "Open Paper Positions" table. **While
   TRADING_MODE: paper, this is the source of truth — do NOT rely on `python3 scripts/dhan.py
   orders` to discover open positions (broker may be broken/sandbox). When TRADING_MODE: live,
   cross-check portfolio.md against `dhan.py orders` and flag any discrepancy.**

2. For each open spread in portfolio.md, detect whether SL or target was breached at ANY point
   during the last hourly candle (not just the current price). This simulates real broker
   behaviour — a live account would have filled the exit the moment the threshold was crossed,
   regardless of when the hourly routine ran.

   **Step A — get the last completed 1h candle range for the underlying:**
   ```
   python3 scripts/market_data.py spot-range <INSTRUMENT>
   ```
   Returns `candle_high` and `candle_low` for the candle that just completed.

   **Step B — estimate cost-to-close at three spot prices** (for each of the 4 legs):
   ```
   python3 scripts/market_data.py estimate-premium <X> <strike> <CE|PE> --dte <days_remaining> [--iv <iv_pct>]
   python3 scripts/market_data.py estimate-premium <X> <strike> <CE|PE> --dte <days_remaining> --spot <candle_high> [--iv <iv_pct>]
   python3 scripts/market_data.py estimate-premium <X> <strike> <CE|PE> --dte <days_remaining> --spot <candle_low>  [--iv <iv_pct>]
   ```
   Cost-to-close at each spot = (short CE premium + short PE premium to BUY back)
                               − (long CE premium + long PE premium to SELL)

   **Step C — determine worst and best case:**
   ```
   worst_cost = max(cost_at_current, cost_at_candle_high, cost_at_candle_low)
   best_cost  = min(cost_at_current, cost_at_candle_high, cost_at_candle_low)
   ```

   **Step D — apply exit thresholds per instrument type:**

   *Index trades (NIFTY / BANKNIFTY / SENSEX):*
   - If `worst_cost >= 2.0 × entry_credit` → SL was hit during this candle.
     Record exit at exactly `2.0 × entry_credit` (the SL trigger price, not worst_cost).
     Reason: `SL`
   - Else if `best_cost <= 0.50 × entry_credit` → profit target was hit.
     Record exit at exactly `0.50 × entry_credit`.
     Reason: `PROFIT_TARGET`
   - Else → leave open, note current unrealized P&L in trade-log.md if meaningfully closer
     to either threshold than at last check.

   *Stock trades (any Nifty 50 F&O symbol):*
   - If `worst_cost >= 2.5 × entry_credit` → SL was hit.
     Record exit at exactly `2.5 × entry_credit`.
     Reason: `SL`
   - Else if `best_cost <= 0.25 × entry_credit` → profit target was hit.
     Record exit at exactly `0.25 × entry_credit`.
     Reason: `PROFIT_TARGET`
   - Else → carry forward (normal for multi-day stock condors). Note unrealized P&L.

   Recording at the trigger price (not worst_cost / best_cost) is intentional — it simulates
   the fill a real broker would have made at the SL/target level, not at the extreme intraday
   move. This keeps paper P&L aligned with what live trading would actually show.

3. To close a paper position:
   - **TRADING_MODE: paper**: remove the row from portfolio.md "Open Paper Positions" table,
     add a row to "Closed Paper Positions" with: exit date, exit credit (trigger price from
     step 2), realized P&L = entry credit - exit credit, reason. Also try the broker close
     for completeness (`python3 scripts/dhan.py place-order`) but broker success/failure does
     NOT affect the paper close.
   - **TRADING_MODE: live**: place the closing order via dhan.py, poll order-status until
     TRADED, then update portfolio.md with the real exit price.

4. Log every close (or non-action with reason) to memory/trade-log.md.

5. Send a Telegram notification via `python3 scripts/telegram.py` only if a position was
   actually closed (triggered PROFIT_TARGET or SL). Include instrument, realized P&L, reason.
