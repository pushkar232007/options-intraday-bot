# Trade Log

Format per entry: `YYYY-MM-DD HH:MM IST | INSTRUMENT | DTE | action | strikes | credit/debit | qty | reason`

Log every trade placed, closed, or skipped (and why) — including a skipped trade when a guardrail
blocked it. Keep entries short (1-3 lines). Tail the last ~20 entries when reading this file in a
routine; don't re-read the whole history every time.

**Always include DTE-at-entry**, especially for BANKNIFTY — it's the unvalidated instrument (see
memory/strategy.md and memory/signals-learnings.md) and its results must be assessable separately
from NIFTY/SENSEX, which needs DTE visible per trade, not just instrument name.

---

## 2026-07-01 intraday-monitor (~12:36 IST) — NIFTY IRON CONDOR OPENED (paper position #1, broker best-effort DH-905 rejected)

`2026-07-01 12:36 IST | NIFTY | 6 | OPEN (paper) | IC SP23950/LP23850/SC24150/LC24250 | net credit 72.01/unit | 2 lots (130 qty) | ADX 16.18 range-bound, cleared all guardrails`
- **First trade executed under the portfolio-first restructure.** Unlike the ~09:34/~11:43 blocked
  attempts today, the paper position is now written to portfolio.md as the source of truth and the
  broker order is best-effort only — DH-905 no longer prevents the paper trade.
- **Positions to manage first:** none open in portfolio.md → nothing for the 50%/2x exit rules to
  act on. (Broker `orders` still only shows the expired 2026-06-25 sid=71472 artifact — not a
  strategy position, ignored.)
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 100000 --day-pnl 0` → False).
- **Setup — NIFTY QUALIFIED:** scan spot ~24,034 **ADX(14) 16.21, re-confirmed 16.18** (well clear
  of 18 gate, not a boundary flicker). BANKNIFTY ADX 23.67 (no), SENSEX ADX 20.8 (no). India VIX 13.43.
- **Strikes (step 50, ATM 24050):** short 23950PE/24150CE (2 OTM), long 23850PE/24250CE (4 OTM),
  width 100. Legs (est, DTE 6): SP 115.83 + SC 124.75 − LP 80.10 − LC 88.47 = **net credit 72.01/unit**.
- **Sized (2 lots):** `size-spread --capital 100000 --width 100 --credit 72.01 --lot-size 65` → 2 lots.
  Max loss 2×(100−72.01)×65 = **₹3,639 ≤ 5% cap (₹5,000)**. Expiry 2026-07-07 (**6 DTE**, nearest NIFTY
  weekly, within validated DTE 1-6). Credit collected 72.01×130 = ₹9,361.
- **Broker (best-effort):** `place-spread` → **DH-905 Input_Exception** (sandbox OMS still doesn't
  recognize current NIFTY weekly securityIds — same frozen-instrument blocker as ~11:43). **Broker
  status: REJECTED. Paper position NOT unwound** — portfolio.md is source of truth in TRADING_MODE: paper.
- **Exit levels for next monitor run:** PROFIT_TARGET cost-to-close ≤ 36.01/unit, SL ≥ 144.02/unit,
  else forced EOD square-off. Telegram sent (paper position opened + broker rejected).

## 2026-07-01 intraday-monitor (~11:43 IST) — NIFTY QUALIFIED & SIZED, but ENTRY BLOCKED by NEW sandbox blocker (DH-905, unknown securityIds)

`2026-07-01 11:43 IST | NIFTY | 6 | ENTRY REJECTED (sandbox OMS rejects contract, DH-905) | IC 23800/23900/24100/24200 | est net credit 72.02 | intended 2 lots (130 qty) | all 4 legs DH-905 input-validation reject`
- **Positions to manage:** none. Only TRADED orders are the two 2026-06-29 artifact BUYs (sid=71472,
  NIFTY-Jun2026-24000-CE, expired 2026-06-25) — no strategy exit rule applies. Zero bot positions open.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 100000 --day-pnl 0` → tripped=False).
- **Fresh setup — NIFTY QUALIFIED:** scan NIFTY spot ~23,992–23,998 **ADX(14) 16.08 (re-confirmed
  twice, well clear of the 18 gate — not a boundary flicker)** → range-bound. BANKNIFTY ADX 21.39 (no),
  SENSEX ADX 18.55 (no). India VIX ~13.45. First clean qualifier in days.
- **Sized OK (2 lots):** IC short 23900PE/24100CE, long 23800PE/24200CE (2/4 strikes OTM, step 50),
  width 100, est net credit ₹72.02/unit (110.73+129.13 short − 76.62+91.22 long), lot 65.
  `risk.py size-spread --capital 100000 --width 100 --credit 72.02 --lot-size 65` → 2 lots;
  max loss 2×(100−72.02)×65 = ₹3,637 ≤ 5% cap (₹5,000). Expiry **2026-07-07 (6 DTE**; nearest listed —
  NIFTY weeklies are Tue, today is Wed 07-01, so 07-07 is the closest; within validated DTE 1-6).
- **BLOCKED at placement — NEW distinct failure, DH-905 (not the morning's DH-906 margin issue):**
  `place-spread` failed on its first (long-put BUY) leg with **Dhan 400 DH-905 "Input_Exception:
  Missing required fields, bad values for parameters."** Isolated it: a single `place-order` on every
  one of the four 07-07 NIFTY securityIds (44613/44617/44633/44640, all valid in Dhan's published
  instrument master, re-confirmed after `--refresh`) fails DH-905 for **both BUY and SELL**. By
  contrast a `place-order` on the expired artifact sid=71472 passes input validation and reaches the
  RMS margin check (DH-906 fund-limit reject). **Conclusion: the Dhan sandbox OMS does not recognize
  the newly-listed NIFTY 2026-07-07 contract securityIds — its tradable instrument universe appears
  frozen/stale and excludes recently-listed expiries.** This is a *deeper* blocker than the margin one:
  even with margin freed and the place-spread leg-ordering fix (long legs first, already in dhan.py)
  in place, these contracts can't be traded until the sandbox refreshes its instrument set.
- **Verified 0 legs filled** — clean failure at input validation, no partial/naked position left on
  (re-checked `orders`: only the two 2026-06-29 artifact BUYs are TRADED; nothing new today). During
  isolation a stray BUY on the expired sid=71472 was placed and cleanly REJECTED (Fund Limit), 0 filled.
- **Action needed (flagged via Telegram + routine push):** two stacked sandbox blockers now prevent
  trading valid setups — (1) DH-906 margin locked by the un-clearable expired sid=71472 artifact
  (`availableBalance` ₹65,301, `utilizedAmount` ₹934,698), and (2) DH-905 sandbox OMS doesn't know the
  current NIFTY weekly contracts. **A full Dhan sandbox account reset (fresh instrument set + margin
  restored to ₹1,00,000 free) is required** before any qualifying setup can actually execute. Margin
  top-up alone will NOT fix (2). Logged so the next routine doesn't re-derive from scratch.

## 2026-07-01 intraday-monitor (~later, mid-session) — SKIP (no setup clears gate; margin blocker persists)

`2026-07-01 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX not cleanly <18`
- **Positions to manage:** none. Only net TRADED position is the expired-2026-06-25 sandbox
  artifact sid=71472 (NIFTY-Jun2026-24000-CE, +130 long) — no strategy exit rule applies. Zero bot
  trades open. Nothing for the 50%/2x exit rules to act on.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 100000 --day-pnl 0` →
  tripped=False; day P&L ₹0).
- **Fresh-setup check — SENSEX flickered at the gate, did not clear on re-confirm:** scan read
  NIFTY spot 23,992.85 ADX 18.22 (no), BANKNIFTY 57,793.3 ADX 24.05 (no), SENSEX 76,931.22 ADX
  ~18.0 — `range_bound: true` (raw just under 18). Re-confirmed SENSEX directly per the "re-confirm
  ADX before acting" rule → **raw ADX 18.05, NOT below the 18 gate.** ADX is oscillating right on
  the 18.0 boundary intraday; the binding re-check reads above it. NIFTY re-check 18.22, also above.
  India VIX 13.52 (low-vol backdrop, but ADX is the binding constraint). **No entry** — not cleanly
  range-bound; don't force a trade on a boundary flicker.
- **Margin blocker still unresolved (context, not the reason for skip):** `funds` still shows
  availableBalance ₹65,301.12, utilizedAmount ₹934,698 locked by the un-clearable expired sid=71472
  artifact. So even had SENSEX cleared the gate, `place-spread` would again hit DH-906 as it did at
  ~09:34 today. No sandbox reset/top-up has happened yet — flag remains open for the human.
- **No Telegram** (no trade placed/closed, no circuit-breaker trip).

## 2026-07-01 intraday-monitor (~09:34 IST) — first qualifying setup, but ENTRY BLOCKED by sandbox margin

`2026-07-01 09:34 IST | SENSEX | 1 | ENTRY REJECTED (insufficient sandbox margin) | IC 76200/76400/76800/77000 | est net credit 116.98 | intended 3 lots (60 qty) | DH-906 order rejected`
- **Positions to manage:** none. Only net TRADED position is the expired-2026-06-25 sandbox
  artifact sid=71472 (NIFTY-Jun2026-24000-CE, +130 long) — no strategy exit rule applies.
- **Circuit breaker:** not tripped (day P&L ₹0, capital ₹1,00,000).
- **Fresh setup — SENSEX QUALIFIED (first time in days):** scan NIFTY spot 23,929.9 ADX 18.58
  (no), BANKNIFTY 57,554 ADX 31.52 (no), **SENSEX spot 76,580–76,600 ADX(14) 17.09 → range-bound,
  below the 18 gate.** India VIX 13.94. Re-confirmed ADX 17.09 before acting.
- **Sized OK:** IC short 76400PE/76800CE, long 76200PE/77000CE (2/4 strikes OTM, step 100),
  width 200, est net credit ₹116.98/unit, lot size 20. `risk.py size-spread` → 3 lots; max loss
  3×(200−116.98)×20 = ₹4,981 ≤ 5% cap (₹5,000). Expiry 2026-07-02 (1 DTE; nearest listed, within
  validated DTE 1-6, closest to the ~2-DTE preference — 8-DTE 07-09 is outside tested range).
- **BLOCKED at placement:** `place-spread` → **Dhan 400 DH-906 "Transaction has Failed"** on the
  first leg. Root cause: sandbox `availableBalance` is only **₹65,301** (`utilizedAmount` ₹934,698
  of the ~₹10L sandbox notional is locked by the leftover expired sid=71472 test-artifact
  positions, whose closing SELLs keep getting REJECTED "Fund Limit Insufficient" and can't be
  cleared — contract expired 2026-06-25). `place-spread` places legs sequentially leading with the
  naked short-put SELL, whose standalone naked margin far exceeds ₹65,301 → rejected. **Verified 0
  SENSEX legs filled — clean failure on leg 1, no partial/naked position left on.** No-trade.
- **Action needed (flagged via Telegram + routine push):** this is an execution blocker, not a
  strategy skip — a valid setup could not be traded because the sandbox account's margin is locked
  by an un-clearable artifact. Two fixes to consider before the next qualifying setup: (a) reset/
  top-up the Dhan sandbox account so `availableBalance` reflects the intended ₹1,00,000 free, and/
  or (b) make `place-spread` place the protective long (BUY) legs first, or use a margin-benefit
  basket, so a defined-risk condor isn't margined as a naked short at leg 1. Logged here so the
  next routine doesn't re-derive this from scratch.

## 2026-06-30 EOD square-off (final, ~15:15 IST)

`2026-06-30 EOD IST | — | — | NO-OP (no strategy positions) | nothing to close`
- **Square-off run:** `square-off-all` placed one closing SELL on the only net-open account
  position (sid=71472, NIFTY-Jun2026-24000-CE, +130 long) → order 72260630107081 REJECTED
  ("Fund Limit Insufficient", expired contract drvExpiryDate 2026-06-25), confirmed via
  `order-status`. Same known 2026-06-29 sandbox test artifact — clean terminal rejection, not a
  stuck order; it will lapse on its own, no Telegram escalation warranted.
- **Strategy positions to carry/close:** none. Zero bot trades placed today — all three
  instruments SKIP'd at ADX>18 the entire session (NIFTY/BANKNIFTY/SENSEX never crossed below the
  18 gate; India VIX ~13.3 low-vol but ADX was the binding constraint). Carry-forward 3-condition
  test N/A — nothing held.
- **Final state (from `orders`):** cash ₹1,00,000 (paper), all-time realized P&L ₹0, today's P&L ₹0.
- **Note:** EOD routine fired several times today (~11:40, ~11:57, and again now); all no-ops since
  there were never any strategy positions. Schedule drift flagged in earlier entries — worth a cron
  check if unintended, but harmless on a no-trade day.

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

## 2026-06-30 intraday-monitor (~14:32 IST)

`2026-06-30 ~14:32 IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no setup) | ADX>18 all three`
- **Positions to manage:** none. Only net TRADED position is sid=71472 (NIFTY-Jun2026-24000-CE,
  +130 long) — the expired-2026-06-25 single-leg sandbox test artifact (strategy never buys naked/
  single-leg), no exit rule applies. Zero bot trades in log.
- **Circuit breaker:** not tripped (day P&L ₹0, capital ₹1,00,000).
- **Fresh-setup check:** no qualifying ADX<18 setup. Scan — NIFTY spot 23,936 ADX 21.82;
  BANKNIFTY 57,702 ADX 29.38; SENSEX 76,539 ADX 20.2. All trending, all above the 18 gate.
  India VIX 13.38 (low-vol backdrop, but the ADX gate is the binding constraint). NIFTY/SENSEX
  have eased toward the gate vs the 25.x earlier reads but neither has crossed below 18. No entry —
  selectivity working as designed. ~45 min to EOD square-off window; unlikely to qualify today.

## 2026-06-30 intraday-monitor (~13:32 IST)

`2026-06-30 ~13:32 IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no setup) | ADX>18 all three`
- **Positions to manage:** none. Only net TRADED position is sid=71472 (NIFTY-Jun2026-24000-CE,
  +130 long) — the expired-2026-06-25 single-leg sandbox test artifact (strategy never buys naked/
  single-leg), no exit rule applies. Zero bot trades in log.
- **Circuit breaker:** not tripped (day P&L ₹0, capital ₹1,00,000).
- **Fresh-setup check:** no qualifying ADX<18 setup. Scan — NIFTY spot 23,937 ADX 25.26;
  BANKNIFTY 57,658 ADX 28.7; SENSEX 76,675 ADX 25.08. All trending, all above the 18 gate.
  India VIX 13.36 (low-vol backdrop, but the ADX gate is the binding constraint). No entry —
  selectivity working as designed. NIFTY remains well above the gate (was 19.5 pre-market).
