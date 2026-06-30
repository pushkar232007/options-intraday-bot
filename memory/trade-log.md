# Trade Log

Format per entry: `YYYY-MM-DD HH:MM IST | INSTRUMENT | DTE | action | strikes | credit/debit | qty | reason`

Log every trade placed, closed, or skipped (and why) — including a skipped trade when a guardrail
blocked it. Keep entries short (1-3 lines). Tail the last ~20 entries when reading this file in a
routine; don't re-read the whole history every time.

**Always include DTE-at-entry**, especially for BANKNIFTY — it's the unvalidated instrument (see
memory/strategy.md and memory/signals-learnings.md) and its results must be assessable separately
from NIFTY/SENSEX, which needs DTE visible per trade, not just instrument name.

---

## 2026-06-30 intraday-monitor

`2026-06-30 ~intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no setup) | ADX>18 all three`
- **Positions to manage:** none. The only TRADED orders in the Dhan account (sid=71472,
  NIFTY-Jun2026-24000-CE, net +130 long) are leftover sandbox end-to-end test artifacts from
  2026-06-29 — a single naked CALL leg (strategy never buys naked / never single-leg), with all
  matching closing SELLs stuck in TRANSIT (the exact quirk documented in strategy.md L95-104), on a
  contract that expired 2026-06-25. Not a strategy position; trade-log shows zero bot trades. Cost-
  to-close estimate N/A (expired contract). Nothing for the 50%/2x exit rules to act on.
- **Circuit breaker:** not tripped (day P&L ₹0, capital ₹1,00,000).
- **Fresh-setup check:** no qualifying ADX<18 setup. Scan — NIFTY spot 23,958 ADX 23.88;
  BANKNIFTY 57,817 ADX 24.5; SENSEX 76,716 ADX 22.28. All trending, all above the 18 gate. NIFTY
  drifted further from the threshold vs the 19.5 pre-market read, not toward it. India VIX 13.31.
  No entry — selectivity working as designed.

## 2026-06-30 intraday-monitor (~12:32 IST)

`2026-06-30 ~12:32 IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no setup) | ADX>18 all three`
- **Positions to manage:** none. Only TRADED net position is sid=71472 (NIFTY-Jun2026-24000-CE,
  +130 long), the expired-2026-06-25 sandbox test artifact — not a strategy position, no exit rule
  applies. Zero bot trades in log.
- **Circuit breaker:** not tripped (day P&L ₹0, capital ₹1,00,000).
- **Fresh-setup check:** no qualifying ADX<18 setup. Scan — NIFTY spot 23,916 ADX 24.39;
  BANKNIFTY 57,643 ADX 24.67; SENSEX 76,633 ADX 24.68. All trending. India VIX 13.42. NIFTY now
  further from the gate than the 19.5 pre-market read (and the 23.88 earlier-intraday read). No entry.

## 2026-06-30 EOD square-off

`2026-06-30 EOD IST | — | — | NO-OP (no strategy positions) | nothing to close`
- **Square-off run:** `square-off-all` placed one closing SELL on the only net-open account
  position (sid=71472, NIFTY-Jun2026-24000-CE, +130 long) → order 72260630105081 REJECTED
  ("Fund Limit Insufficient", expired contract drvExpiryDate 2026-06-25). This is the known
  2026-06-29 sandbox test artifact (2 TRADED BUYs of 65 + 3 stuck TRANSIT SELLs, all same expired
  contract), NOT a strategy position. Clean terminal rejection, not a stuck order — it will lapse
  on its own, no Telegram escalation warranted.
- **Strategy positions to carry/close:** none. Zero bot trades placed today (all three instruments
  SKIP'd at ADX>18 all day). Carry-forward 3-condition test N/A — nothing held.
- **Final state (from `orders`):** cash ₹1,00,000 (paper), all-time realized P&L ₹0, today's P&L ₹0.

## 2026-06-30 EOD square-off (re-fire, ~11:57 AM IST)

`2026-06-30 ~11:57 IST | — | — | NO-OP (re-verified, no strategy positions) | nothing to close`
- **Why this entry exists:** the EOD routine fired again at ~11:57 AM IST — the *second* premature
  fire today (first was ~11:40 AM, commit 6a0f39b). The routine's documented schedule is `45 9 *
  * 1-5` = 3:15 PM IST (routines/eod-squareoff.md), so both of today's EOD fires ran ~3.5h early,
  mid-session. Likely a manual/test trigger or a misconfigured platform schedule — worth checking
  the cron if unintended. Harmless today (no positions to mishandle), but a real EOD at noon would
  miss any afternoon entry, so flag it.
- **Re-verified broker state:** ran `square-off-all` again → one closing SELL on sid=71472
  (NIFTY-Jun2026-24000-CE, +130 long) → order 72260630106081 REJECTED ("Fund Limit Insufficient",
  expired contract drvExpiryDate 2026-06-25). Same known sandbox test artifact, clean terminal
  rejection (not stuck TRANSIT) — will lapse on its own, no escalation. Confirmed via `order-status`.
- **Strategy positions:** none (zero bot trades today; all three SKIP'd at ADX>18). Carry-forward
  test N/A. Final state unchanged: cash ₹1,00,000, all-time realized P&L ₹0, today's P&L ₹0.
