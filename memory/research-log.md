# Research Log

Daily notes on option-chain conditions: ADX/trend reading, India VIX level, PCR, OI buildup by
strike, anything news-driven that might affect the day. Keep entries short. Tail the last 2-3
entries when reading this file in a routine.

---

## 2026-07-22 (intraday-monitor addendum, latest-2) — all three indices still trending, board firmed a touch further (ADX 34/33/41); no setup; flat, nothing to manage

Fresh `scan` (VIX **12.9**, down from 13.12): NIFTY spot 24,038.25 ADX **34.02** → `range_bound: false`, BANKNIFTY spot 57,284.4 ADX **32.8** → `range_bound: false`, SENSEX spot 76,894.62 ADX **40.98** → `range_bound: false`. Unchanged-to-firmer vs the prior addendum (NIFTY 34.3→34.02 flat, BANKNIFTY 29.12→32.8, SENSEX 37.45→40.98) on a slightly firmer spot (NIFTY 24,004→24,038, BANKNIFTY 57,244→57,284, SENSEX 76,868→76,895) — the trend regime is holding and if anything deepening, none anywhere near the 18 gate to even re-check. BANKNIFTY, the deeply range-bound pre-market standout (ADX 9.73), remains fully unwound (9.73→20.4→29.12→32.8). **No enterable index setup.** Stocks unchanged (22 morning qualifiers still earnings-blocked into Jul 30 monthly, DTE 8, peak Q1; daily ADX static, no mid-day re-scan). Broker `orders` shows only the stale sid=71472 Jun artifact (filledQty 65, expired 2026-06-25) — no strategy legs; confirmed FLAT. `/monitor` a no-op (0 open positions). No trade placed. **Git clean:** on read, local HEAD and `origin/main` both at 081469c after `git fetch origin main` — prior memory on `main`, no stranding.

---

## 2026-07-22 (intraday-monitor addendum, latest) — whole board firmed FURTHER into trend (ADX 34/29/37); BANKNIFTY fully unwound its pre-market 9.73; no setup; flat, nothing to manage

Fresh `scan` (VIX **13.12**, up from 13.01): NIFTY spot 24,004.35 ADX **34.3** → `range_bound: false`, BANKNIFTY spot 57,243.7 ADX **29.12** → `range_bound: false`, SENSEX spot 76,868.18 ADX **37.45** → `range_bound: false`. All three firmed further from the prior intraday read (NIFTY 27.53→34.3, BANKNIFTY 20.4→29.12, SENSEX 31.1→37.45) as spot drifted lower across the board (NIFTY 24,020→24,004, BANKNIFTY 57,266→57,244, SENSEX 77,099→76,868) — a directional down-move, the opposite of the range-bound regime this strategy trades, none anywhere near the 18 gate to even re-check. BANKNIFTY, the deeply range-bound pre-market standout (ADX 9.73), has now fully unwound (9.73→20.4→29.12) — the recurring gate-hugger/"firms away" pattern, a large swing. **No enterable index setup.** Stocks unchanged (22 morning qualifiers still earnings-blocked into Jul 30 monthly, DTE 8, peak Q1; daily ADX static, no mid-day re-scan). Flat, 0 open positions, `/monitor` a no-op. No trade placed. **Git clean:** on read, local HEAD and `origin/main` both at 164272d after `git fetch origin main` — prior memory on `main`, no stranding.

---

## 2026-07-22 (intraday-monitor addendum) — pre-market's BANKNIFTY candidate firmed away at the open (ADX 9.73→20.4); all three indices now trending; no setup; flat, nothing to manage

Fresh open `scan` (VIX **13.01**, up from 12.6 pre-market): NIFTY spot 24,020.05 ADX **27.53** → `range_bound: false`, BANKNIFTY spot 57,265.55 ADX **20.4** → `range_bound: false`, SENSEX spot 77,099.33 ADX **31.1** → `range_bound: false`. **The pre-market standout — BANKNIFTY, deeply range-bound at ADX 9.73 with Jul 28 at DTE 6 (both gates flagged as aligning) — did NOT hold**: ADX firmed all the way back above the 18 gate to 20.4 as spot dropped ~570 pts (57,835→57,266) into the open. Same "gate-hugger firms away rather than settling below" pattern seen repeatedly this month (07-13/07-14/07-17/07-21), just a much larger swing here. NIFTY firmed too (pre-market 18.67→27.53); SENSEX unchanged-trending (26.01→31.1). **No enterable index setup** — none below 18. Would-be BANKNIFTY entry (2nd-ever) does not fire; DTE 6 was in-window but the ADX gate is not met. Stocks unchanged (22 morning qualifiers still earnings-blocked into Jul 30 monthly, DTE 8, peak Q1; daily ADX static, no re-scan). Flat, 0 open positions, `/monitor` a no-op. No trade placed.

---

## 2026-07-22 — pre-market scan: BANKNIFTY the standout (deeply range-bound + DTE 6, genuine open candidate); NIFTY a gate-hugger; SENSEX trending; 22 stock qualifiers still earnings-blocked

India VIX **12.6** (low — the low-vol backdrop credit spreads like). Draft only, no trade placed per protocol. Fresh `scan`:

- **NIFTY** — spot 24,187.7, ADX(14) **18.67** → trending, but only a hair above the 18 gate. Classic gate-hugger — worth an open re-check once the opening range prints; it could settle <18. No draft entry yet.
- **BANKNIFTY** — spot 57,835.35, ADX(14) **9.73** → **deeply range-bound ✓** and, crucially, its only listed expiry (Jul 28 monthly) is now at **DTE 6**, inside the ≤7-DTE near-expiry data-gathering window. **This is a genuine open-entry candidate** — the same both-gates-aligned setup that fired yesterday for Position F (which closed +₹8.40, flat/noise as expected). Flat into today → no one-per-instrument block. Candidate strikes (2/4 OTM off spot 57,835, step 100, lot 30): SP57600 / LP57400 / SC58100 / LC58300 (verify sid/lot fresh via `dhan.py lookup BANKNIFTY 2026-07-28 <strike> <CE|PE>` at the open; yesterday Jul 28 = sid 61887 lot 30). Index → intraday-only, would force-close at EOD. Tag DTE-at-entry **6** and assess separately from NIFTY/SENSEX per the BANKNIFTY carve-out. Expect drift-to-flat, not clean decay (the re-backtest's "29 of 31 trades drift to EOD with tiny P&L" pattern; two live points now — Position F +₹8.40 — consistent with it).
- **SENSEX** — spot 77,470.11, ADX(14) **26.01** → clearly trending. No entry.

**Stocks:** 22 qualifiers (HEROMOTOCO 10.43, ULTRACEMCO 11.2, HDFCLIFE 11.75, RELIANCE 11.94, SBIN 12.01, BEL 12.25, HINDUNILVR 12.25, JSWSTEEL 12.27, EICHERMOT 12.3, ADANIPORTS 12.6, COALINDIA 12.75, BPCL 13.74, POWERGRID 14.19, GRASIM 15.19, PNB 15.26, NESTLEIND 15.67, MARUTI 15.73, INFY 15.75, CANBK 16.71, TECHM 16.83, ASIANPAINT 16.87, KOTAKBANK 17.03; TATAMOTORS errored). Only in-range stock expiry is the **Jul 30 monthly (DTE 8)** — still squarely inside Q1 earnings season, so the earnings guardrail remains the binding constraint and the standing operating rule holds: **all 22 earnings-blocked pending Pushkar's steer** (enter-after-report name-by-name vs hold-through vs stand-aside). Note some names likely reported by now (Jul 22) — RELIANCE, HDFCLIFE, TECHM, JSWSTEEL, ULTRACEMCO, INFY would be name-by-name post-earnings candidates IF Pushkar picks (a). Log for awareness, no re-alert.

**Conclusion:** BANKNIFTY is the one clean draft candidate to carry into the open (deeply range-bound, DTE 6, flat book) — re-check ADX<18 holds at the open, then enter per guardrails with SL placed at entry. NIFTY a gate-hugger to re-check; SENSEX out. Stocks stand aside on earnings. **Git clean:** on read, local HEAD and `origin/main` both at 1d4f644 after `git fetch origin main` — prior memory on `main`, no stranding.

---

## 2026-07-21 (intraday-monitor addendum, latest-5) — Positions E (NIFTY) & F (BANKNIFTY) both held (neither PT/SL, both ~flat, combined +₹22.45); NIFTY/SENSEX trending, BANKNIFTY range-bound but one-per-instrument-blocked; no new trade

Fresh `scan` (VIX **12.7**): NIFTY spot 24,158.45 ADX **23.39** → trending (eased from the 24.69 latest-4 read, still ≥18; also holds Position E), BANKNIFTY 57,835.7 ADX **11.11** → `range_bound: true` (deepened; but already holds Position F → one-per-instrument skip), SENSEX 77,416.25 ADX **31.55** → trending. **Position E (NIFTY Jul 28, DTE 7) managed:** last 1h candle 24,154.3–24,180.5; cost-to-close (BS, IV 12.7) current 72.80 / high 72.63 / low 72.85 → worst 72.85 < SL 146.30 AND best 72.63 > PT 36.58 → stays OPEN, ~flat (+₹22.75 unrealized), pinned mid-range between the 24150/24350 shorts. **Position F (BANKNIFTY Jul 28, DTE 7) managed:** last 1h candle 57,824.1–57,917.35; cost-to-close current 153.56 / high 153.68 / low 153.56 → worst 153.68 < SL 307.10 AND best 153.56 > PT 76.78 → stays OPEN, ~flat (−₹0.30 unrealized), pinned mid-range between the 57700/58100 shorts. No new index entry (NIFTY/SENSEX trending; BANKNIFTY range-bound but one-per-instrument-blocked). Stocks unchanged (20 morning qualifiers still earnings-blocked into Jul 30, DTE 9; daily ADX static, no re-scan). Both positions force-close at EOD (index intraday-only). No trade placed or closed.

---

## 2026-07-21 (intraday-monitor addendum, latest-3) — Positions E (NIFTY) & F (BANKNIFTY) both held (neither PT/SL, both ~flat, combined +₹37.20); NIFTY/SENSEX trending, BANKNIFTY range-bound but one-per-instrument-blocked; no new trade

Fresh `scan` (VIX **12.65**): NIFTY spot 24,187.2 ADX **24.66** → trending (firmed from the 21.92 latest-2 read; also holds Position E), BANKNIFTY 57,969.7 ADX **16.06** → `range_bound: true` (but already holds Position F → one-per-instrument skip), SENSEX 77,456.23 ADX **33.17** → trending. **Position E (NIFTY Jul 28, DTE 7) managed:** last 1h candle 24,169.8–24,188.15; cost-to-close (BS, IV 12.65) current 72.49 / high 72.49 / low 72.61 → worst 72.61 < SL 146.30 AND best 72.49 > PT 36.58 → stays OPEN, ~flat (+₹42.90 unrealized), pinned mid-range between the 24150/24350 shorts. **Position F (BANKNIFTY Jul 28, DTE 7) managed:** last 1h candle 57,873.6–57,978.15; cost-to-close current 153.74 / high 153.78 / low 153.39 → worst 153.78 < SL 307.10 AND best 153.39 > PT 76.78 → stays OPEN, ~flat (−₹5.70 unrealized), pinned mid-range between the 57700/58100 shorts. No new index entry (NIFTY/SENSEX trending; BANKNIFTY range-bound but one-per-instrument-blocked). Stocks unchanged (20 morning qualifiers still earnings-blocked into Jul 30, DTE 9; daily ADX static, no re-scan). Both positions force-close at EOD (index intraday-only). No trade placed or closed.

---

## 2026-07-21 (intraday-monitor addendum, latest-2) — BANKNIFTY cleared BOTH gates for the first time (ADX 17.7<18 + DTE 7); OPENED Position F (FIRST BANKNIFTY entry ever); Position E held (~flat +₹32.50); NIFTY/SENSEX trending

Fresh `scan` (VIX **12.69**): NIFTY spot 24,173.3 ADX **21.92** → trending (firmed above the gate from the 15.67 latest read, and already holds Position E), BANKNIFTY 57,882.05 ADX **17.7** → `range_bound: true` ✓ (re-confirmed 17.7), SENSEX 77,452.18 ADX **29.64** → trending. **BANKNIFTY is the only qualifier — and crucially, for the first time it ALSO clears DTE:** its only listed expiry is the Jul 28 monthly (sid 61887 lot 30; no Jul 23 weekly), now at **DTE 7**, inside the ≤7-DTE near-expiry data-gathering window (every prior day it sat at DTE 11-15 and was skipped on DTE grounds). No open BANKNIFTY position → **entered per the BANKNIFTY carve-out.** **Position F (BANKNIFTY Jul 28, DTE 7):** SP57700/LP57500/SC58100/LC58300, 1 lot (30), net credit 153.55/unit (₹4,606.50), PT ≤76.78 / SL ≥307.10, max loss ₹1,393.50 — index intraday-only, force-close at EOD. Broker DH-905 rejected (paper authoritative). Trade Telegram sent. **Position E (NIFTY Jul 28, DTE 7) managed:** last 1h candle 24,166.65–24,188.7; cost-to-close (BS, IV 12.69) current 72.65 / high 72.56 / low 72.71 → worst 72.71 < SL 146.30 AND best 72.56 > PT 36.58 → stays OPEN, ~flat (+₹32.50 unrealized), pinned mid-range between the 24150/24350 shorts. NIFTY/SENSEX no entry (both trending). Stocks unchanged (20 morning qualifiers still earnings-blocked into Jul 30, DTE 9). Both positions force-close at EOD.

---

## 2026-07-21 (intraday-monitor addendum, latest) — Position E held (neither PT/SL, ~flat +₹16.25); NIFTY range-bound again but one-per-instrument-blocked; BANKNIFTY/SENSEX trending; no new trade

Fresh `scan` (VIX **12.86**): NIFTY spot 24,189.3 ADX **15.67** → `range_bound: true` (firmed a touch from the 11.46 entry read, still well below the gate), BANKNIFTY 57,954.0 ADX **22.57** → trending, SENSEX 77,529.27 ADX **23.74** → trending. **Position E (NIFTY Jul 28, DTE 7) managed:** last 1h candle 24,185.5–24,214.7; cost-to-close (BS, IV 12.86, DTE 7) current 72.90 / high 72.82 / low 72.91 → worst 72.91 < SL 146.30 AND best 72.82 > PT 36.58 → stays OPEN, ~flat (+₹16.25 unrealized), NIFTY pinned mid-range between the 24150/24350 shorts. No new index entry (NIFTY qualifies on ADX but already holds Position E → one-per-instrument; BANKNIFTY/SENSEX trending). Stocks unchanged (20 morning qualifiers still earnings-blocked into Jul 30, DTE 9). Position E force-closes at EOD (index intraday-only). No trade placed or closed.

---

## 2026-07-21 (intraday-monitor addendum) — NIFTY dropped deeply range-bound (ADX 11.46<18); OPENED Position E (NIFTY iron condor, Jul 28 DTE 7); SENSEX gate-hugger firmed back above 18; BANKNIFTY trending

Fresh `scan` + `adx NIFTY` re-check (VIX **12.89**): NIFTY spot 24,227.6 ADX **11.46** → `range_bound: true` ✓ — deeply range-bound, only index qualifier. BANKNIFTY 57,996.5 ADX **22.75** → trending; SENSEX 77,722.5 ADX **19.63** → trending — the pre-market SENSEX gate-hugger (17.34) firmed back above 18 once the opening range printed (recurring 07-13/07-14/07-17 pattern), so its Jul 23 DTE-2 candidate is off the table. **Entered 1 NIFTY iron condor (Position E):** expiry decision — Jul 21 is 0-DTE today (verified listed, sid 57348), Jul 23 does NOT exist (lookup returned no contract), Jul 28 = DTE 7 (sid 63947 lot 65); took **Jul 28 (DTE 7)** not the 0-DTE per the avoid-same-day-expiry guardrail + 07-14 house precedent. SP24150/LP24050/SC24350/LC24450, 1 lot, net credit 73.15/unit (₹4,754.75), PT ≤36.58 / SL ≥146.30, max loss ₹1,745.25 — index intraday-only, force-close at EOD. Broker DH-905 rejected (paper authoritative). Stocks unchanged (20 morning qualifiers still earnings-blocked into Jul 30, DTE 9; daily ADX static, no re-scan). Trade Telegram sent (msg 302).

---

## 2026-07-21 (pre-market scan) — REGIME SHIFT: NIFTY (9.77) & SENSEX (17.34) range-bound; SENSEX Jul 23 (DTE 2) is the clean open candidate, NIFTY expiry-caveated; 20 stock qualifiers still earnings-blocked into Jul 30

India VIX **12.98** (low — the quiet backdrop credit spreads like). After a week+ of all-trending
sessions (07-20 board 32.35/42.35/38.73), the chop is back: **two of three indices read range-bound
at the pre-market board**, NIFTY deeply so — the softest index read since 07-17.

- **NIFTY** — spot 24,238.5, ADX(14) **9.77** → range-bound ✓ (deeply; collapsed from the 07-20
  pre-market 32.35). Qualifies clean on ADX, BUT expiry-caveated: nearest listed weekly is **today's
  Jul 21 = 0-DTE (expiry day)** — same-day gamma/liquidity risk, guardrail says avoid 0-DTE if the
  chain looks thin; **Jul 23 does not exist**, so the next weekly is **Jul 28 (DTE 7)**, on the far
  side of the preferred ~2-DTE sweet spot. At the open, either accept the 0-DTE (intraday-only, closed
  same day, so never held to expiry — but expiry-day execution cost is real) or take Jul 28 (DTE 7),
  or skip NIFTY today. Don't reflexively sell the 0-DTE.
- **BANKNIFTY** — spot 57,945.0, ADX(14) **19.08** → trending (just above the 18 gate). No entry;
  DTE-blocked anyway (monthly-only, no near-expiry weekly).
- **SENSEX** — spot 77,708.52, ADX(14) **17.34** → range-bound ✓ (gate-hugger, just under 18).
  Nearest weekly **Jul 23 (DTE 2)** confirmed listed (sid 835690, BSE, lot 20) — right on the
  preferred ~2-DTE sweet spot. **Best index candidate for the open**, but re-check ADX<18 once the
  opening range prints — SENSEX has repeatedly firmed back above 18 at the open this month
  (07-13/07-14/07-17 gate-hugger pattern), so confirm before entering.

**Index candidate strikes (2/4 OTM off spot, for the open routine to refine):**
- **SENSEX** (step 100, spot 77,708) — SP77500 / LP77300 / SC77900 / LC78100, Jul 23 (DTE 2).
- **NIFTY** (step 50, spot 24,238) — SP24150 / LP24050 / SC24350 / LC24450, Jul 28 (DTE 7) or the
  0-DTE Jul 21 if execution looks clean.
Known sandbox blockers (DH-905/DH-906) may reject broker orders — portfolio.md-first, broker best-effort.

**Stock scan — 20 qualifying (ADX<18 daily), lowest-first:** HEROMOTOCO 10.35, ULTRACEMCO 11.33,
JSWSTEEL 11.63, SBIN 11.66, ADANIPORTS 12.27, HDFCLIFE 12.48, EICHERMOT 12.83, RELIANCE 12.88,
HINDUNILVR 13.28, COALINDIA 13.43, BEL 13.47, PNB 13.52, BPCL 13.82, TECHM 14.03, POWERGRID 14.79,
MARUTI 15.12, GRASIM 16.23, INFY 16.96, CANBK 17.35, KOTAKBANK 17.82 (spots/hist_vol in scan
output; TATAMOTORS errored — no data). Two new vs 07-20: CANBK, KOTAKBANK. Neither blocklisted name
(AXISBANK/BHARTIARTL) qualifies. **All 20 remain earnings-blocked:** only in-range stock expiry is
the **Jul 30 monthly (DTE 9)**, and Q1 (June-qtr) season runs ~Jul 16–Aug 8 — SBIN/MARUTI ~Jul 31
sit within 5 days of expiry (hard-banned outright); the rest mostly report during the hold. Per the
standing earnings guardrail (an *affirmative* clear is required) → **skip all 20 on earnings.**
**Note for the open routine:** several names have now likely reported (HDFCLIFE/TECHM ~Jul 16,
JSWSTEEL ~Jul 18, ULTRACEMCO ~Jul 21, RELIANCE ~mid-late Jul) and could become genuine name-by-name
post-earnings candidates for the ~9-day hold into Jul 30 **IF Pushkar picks enter-after-report** —
verify each name's report date is actually behind us before considering it. Absent that steer, still
log-and-skip. Same reference reasoning as the 2026-07-07 signals-learnings entry; no re-alerting.

**Conclusion:** genuine index setup forming for the first time in days — SENSEX Jul 23 (DTE 2) is a
clean open-entry candidate, NIFTY qualifies but is expiry-caveated (0-DTE today / Jul 28 DTE 7).
Draft only — no order placed per pre-market protocol. **Re-check ADX at market-open once the opening
range prints** (SENSEX especially, being a gate-hugger). Stocks remain log-and-skip on earnings.
Flat — 0 open positions, nothing to manage.

---

## 2026-07-20 (intraday-monitor addendum, latest-5) — Position D held (neither PT/SL, ~flat +₹40.95); NIFTY range-bound again but one-per-instrument-blocked; BANKNIFTY/SENSEX trending; no new trade

Fresh `scan` (VIX **12.99**): NIFTY spot 24,229.65 ADX **12.03** → `range_bound: true` (eased further from the 14.12 latest-4 read), BANKNIFTY 58,004.75 ADX **22.57** → trending, SENSEX 77,780.71 ADX **18.93** → trending (just above the gate). **Position D (NIFTY Jul 21, DTE 1) managed:** last 1h candle 24,232.75–24,259.1; cost-to-close (BS, IV 12.99, DTE 1) current 37.88 / high 40.24 / low 38.06 → worst 40.24 < SL 77.02 AND best 37.88 > PT 19.26 → stays OPEN, ~flat (+₹40.95 unrealized, now slightly green), NIFTY pinned mid-range between the 24100/24300 shorts. No new index entry (NIFTY qualifies on ADX but already holds Position D → one-per-instrument; BANKNIFTY/SENSEX trending). Stocks unchanged (18 morning qualifiers still earnings-blocked into Jul 30, DTE 10). Position D force-closes at EOD (index intraday-only). No trade placed or closed.

---

## 2026-07-20 (intraday-monitor addendum, latest-4) — Position D held (neither PT/SL, ~flat); NIFTY range-bound again but one-per-instrument-blocked; BANKNIFTY/SENSEX trending; no new trade

Fresh `scan` (VIX **13.21**): NIFTY spot 24,244.4 ADX **14.12** → `range_bound: true` (eased further from the 16.38 latest-3 read), BANKNIFTY 57,863.95 ADX **21.9** → trending, SENSEX 77,674.53 ADX **25.85** → trending. **Position D (NIFTY Jul 21, DTE 1) managed:** last 1h candle 24,212.4–24,250.05; cost-to-close (BS, IV 13.21, DTE 1) current 39.49 / high 40.06 / low 37.93 → worst 40.06 < SL 77.02 AND best 37.93 > PT 19.26 → stays OPEN, ~flat (−₹63.70 unrealized), NIFTY pinned mid-range between the 24100/24300 shorts. No new index entry (NIFTY qualifies on ADX but already holds Position D → one-per-instrument; BANKNIFTY/SENSEX trending). Stocks unchanged (18 morning qualifiers still earnings-blocked into Jul 30, DTE 10). Position D force-closes at EOD (index intraday-only). No trade placed or closed.

---

## 2026-07-20 (pre-market scan) — all three indices trending HARD (ADX 32-42), no index setup; 18 stock qualifiers still earnings-blocked into Jul 30

India VIX **13.15** (low — the quiet backdrop credit spreads like), but the ADX<18 entry gate is
met on no index; all three read clearly trending, none near the gate to re-check at the open:

- **NIFTY** — spot 24,334.3, ADX(14) **32.35** → trending. No entry.
- **BANKNIFTY** — spot 58,521.4, ADX(14) **42.35** → trending. No entry.
- **SENSEX** — spot 78,151.45, ADX(14) **38.73** → trending. No entry.

The directional up-move regime that held all of 07-17 (EOD board 29.1/38.08/35.75) firmed further
over the weekend into 07-20 — all three ADX higher, spot ticking up (NIFTY 24,293→24,334, BANKNIFTY
58,388→58,521, SENSEX 78,080→78,151). No index iron-condor setup; none anywhere near the 18 gate to
even re-check at the open. This is the regime the strategy is not built for.

**Stock scan — 18 qualifying (ADX<18 daily), lowest-first:** SBIN 10.36, ULTRACEMCO 10.65,
HEROMOTOCO 10.72, JSWSTEEL 11.79, PNB 11.90, HDFCLIFE 12.60, ADANIPORTS 12.67, EICHERMOT 12.70,
BPCL 12.83, RELIANCE 12.99, HINDUNILVR 13.46, TECHM 13.96, BEL 14.01, COALINDIA 14.10, POWERGRID
14.80, MARUTI 15.33, GRASIM 16.62, INFY 17.84 (spots/hist_vol in scan output; TATAMOTORS errored —
no data). Neither blocklisted name (AXISBANK/BHARTIARTL) qualifies. **All 18 remain earnings-blocked,
unchanged from prior days:** the only in-range stock expiry is the **Jul 30 monthly (DTE 10)**, and
Q1 (June-qtr) earnings season runs ~Jul 16–Aug 8 — entering now means holding a short-vol condor
straight through essentially every name's result (SBIN/MARUTI ~Jul 31 within 5 days of expiry =
hard-banned; the rest report during the hold). Per the standing earnings guardrail (an *affirmative*
clear is required and none can be given this cycle) → **skip all 18 on earnings.** Same reference
reasoning as the 2026-07-07 signals-learnings entry; no re-alerting. Awaiting Pushkar's steer
(enter-after-report name-by-name vs authorize hold-through-earnings vs stand aside this cycle).

**Conclusion:** no index setup (all trending, none near 18), no stock setup (all earnings-blocked).
No-trade day by default. Draft only — no order placed per pre-market protocol. If any index settles
<18 once the opening range prints, re-check at the open, but none is close enough today to expect it.
No positions open, nothing to manage — flat into today.

---

## 2026-07-20 (intraday-monitor addendum, latest-3) — Position D held (neither PT/SL hit, ~flat); NIFTY range-bound again but one-per-instrument-blocked; BANKNIFTY/SENSEX trending; no new trade

Fresh `scan` (VIX **13.43**): NIFTY spot 24,167.15 ADX **16.38** → `range_bound: true` (still below the gate, eased from the 17.18 entry read), BANKNIFTY 57,622.6 ADX **27.41** → trending, SENSEX 77,595.55 ADX **26.14** → trending. **Position D (NIFTY Jul 21) managed:** last 1h candle 24,166.5–24,199.9; cost-to-close (BS, IV 13.43, DTE 1) worst 39.17 < SL 77.02 and best 38.47 > PT 19.26 → stays OPEN, ~flat (−₹40.30 unrealized), NIFTY pinned mid-range between the 24100/24300 shorts. No new index entry (NIFTY qualifies on ADX but already holds Position D → one-per-instrument; BANKNIFTY/SENSEX trending). Stocks unchanged (18 morning qualifiers still earnings-blocked into Jul 30, DTE 10). Position D force-closes at EOD (index intraday-only). No trade placed or closed.

---

## 2026-07-20 (intraday-monitor addendum, latest-2) — NIFTY dropped INTO range-bound (ADX 17.18<18); OPENED Position D (NIFTY iron condor); BANKNIFTY/SENSEX still trending

Fresh `scan` + `adx NIFTY` re-check (VIX **13.35**): NIFTY spot 24,209.3 ADX **17.18** → `range_bound: true` ✓ — dropped below the 18 gate for the first time this session after easing steadily all day (pre-market 32.35 → 27.59 → 21.19 → **17.18**). BANKNIFTY 57,652.5 ADX **30.44** and SENSEX 77,673.29 ADX **26.74** both still trending. **Entered 1 NIFTY iron condor (Position D):** Jul 21 (DTE 1, nearest weekly) SP24100/LP24000/SC24300/LC24400, 1 lot, net credit 38.51/unit (₹2,503.15), PT ≤19.26 / SL ≥77.02, max loss ₹3,996.85 — index intraday-only, force-close at EOD. Broker DH-905 rejected (paper authoritative). Stocks unchanged (18 morning qualifiers still earnings-blocked into Jul 30, DTE 10). Trade Telegram sent.

---

## 2026-07-20 (intraday-monitor addendum, latest) — all three indices still trending; NIFTY eased further toward the gate but still ~3 pts above; no setup; flat, nothing to manage

Fresh `scan` (VIX **13.41**): NIFTY spot 24,216.45 ADX **21.19** → `range_bound: false`, BANKNIFTY 57,740.55 ADX **33.26** → `range_bound: false`, SENSEX 77,650.87 ADX **31.5** → `range_bound: false`. NIFTY eased further vs the prior addendum (27.59→21.19) as spot ticked up (24,188→24,216); BANKNIFTY/SENSEX eased marginally too (38.28→33.26, 35.1→31.5) — NIFTY is the closest to the gate but still ~3 pts above 18, no re-check trigger. The directional up-move regime is holding, none qualifies. **No index setup.** Stocks unchanged (18 morning qualifiers still earnings-blocked into Jul 30, DTE 10; daily ADX static, no re-scan). Flat, 0 open positions, nothing to manage. No trade placed.

---

## 2026-07-20 (intraday-monitor addendum) — all three indices still trending; NIFTY eased off pre-market but none near the gate; no setup; flat, nothing to manage

Fresh `scan` (VIX **13.55**): NIFTY spot 24,188.35 ADX **27.59** → `range_bound: false`, BANKNIFTY 57,677.15 ADX **38.28** → `range_bound: false`, SENSEX 77,613.8 ADX **35.1** → `range_bound: false`. NIFTY eased vs the pre-market board (32.35→27.59) on a modest spot pullback (24,334→24,188); BANKNIFTY/SENSEX eased marginally too (42.35→38.28, 38.73→35.1) — the directional up-move regime is holding, none anywhere near the 18 gate to even re-check. **No index setup.** Stocks unchanged (18 morning qualifiers still earnings-blocked into Jul 30, DTE 10; daily ADX static, no re-scan). Flat, 0 open positions, nothing to manage. No trade placed.

---

## 2026-07-17 (intraday-monitor addendum, latest-5) — all three indices still trending; board near-unchanged on a firmer spot; no setup; flat, nothing to manage

Fresh `scan` (VIX **13.18**): NIFTY spot 24,292.7 ADX **29.1** → `range_bound: false`, BANKNIFTY 58,388.25 ADX **38.08** → `range_bound: false`, SENSEX 78,080.24 ADX **35.75** → `range_bound: false`. Near-unchanged vs the prior addendum (NIFTY 30.25→29.1, BANKNIFTY 35.06→38.08, SENSEX 39.44→35.75) with spot ticking a touch firmer (NIFTY 24,273→24,293, BANKNIFTY 58,090→58,388, SENSEX 77,985→78,080) — the directional up-move regime is holding into the close, none anywhere near the 18 gate. **No index setup.** Stocks unchanged (17 morning qualifiers still earnings-blocked into Jul 30; daily ADX static, no re-scan). Flat, 0 open positions, nothing to manage. No trade placed.

---

## 2026-07-17 (intraday-monitor addendum, latest-4) — all three indices still trending; SENSEX firmed to 39.44, NIFTY/BANKNIFTY eased marginally; no setup; flat, nothing to manage

Fresh `scan` (VIX **13.21**): NIFTY spot 24,273.05 ADX **30.25** → `range_bound: false`, BANKNIFTY 58,090.15 ADX **35.06** → `range_bound: false`, SENSEX 77,984.98 ADX **39.44** → `range_bound: false`. NIFTY/BANKNIFTY eased marginally vs the prior addendum (NIFTY 30.92→30.25, BANKNIFTY 38.08→35.06) while SENSEX firmed further (36.87→39.44), spot near-flat — the directional up-move regime is holding into the close, none anywhere near the 18 gate. **No index setup.** Stocks unchanged (17 morning qualifiers still earnings-blocked into Jul 30; daily ADX static, no re-scan). Flat, 0 open positions, nothing to manage. No trade placed.

---

## 2026-07-17 (intraday-monitor addendum, latest-3) — all three indices firmed further into trend; BANKNIFTY firmed hardest; no setup; flat, nothing to manage

Fresh `scan` (VIX **13.29**): NIFTY spot 24,279.95 ADX **30.92** → `range_bound: false`, BANKNIFTY 58,085.15 ADX **38.08** → `range_bound: false`, SENSEX 77,970.14 ADX **36.87** → `range_bound: false`. Firmed further vs the prior addendum (NIFTY 26.86→30.92, BANKNIFTY 33.8→38.08, SENSEX 32.05→36.87) with spot near-flat-to-firmer — the directional up-move regime is holding and deepening, none anywhere near the 18 gate. **No index setup.** Stocks unchanged (17 morning qualifiers still earnings-blocked into Jul 30; daily ADX static, no re-scan). Flat, 0 open positions, nothing to manage. No trade placed.

---

## 2026-07-17 (intraday-monitor addendum, latest-2) — all three indices still trending; BANKNIFTY firmed hard; no setup; flat, nothing to manage

Fresh `scan` (VIX **13.28**): NIFTY spot 24,247.85 ADX **26.86** → `range_bound: false`, BANKNIFTY 58,047.75 ADX **33.8** → `range_bound: false`, SENSEX 77,889.71 ADX **32.05** → `range_bound: false`. Unchanged-to-firmer vs the prior addendum (NIFTY 24.18→26.86, BANKNIFTY 26.13→33.8, SENSEX 27.7→32.05) with spot near-flat — the directional up-move regime is holding, none near the 18 gate. **No index setup.** Stocks unchanged (17 morning qualifiers still earnings-blocked into Jul 30; daily ADX static, no re-scan). Flat, 0 open positions, nothing to manage. No trade placed.

---

## 2026-07-17 (intraday-monitor addendum, latest) — whole board firmed FURTHER into trend; even BANKNIFTY no longer range-bound; no setup; flat, nothing to manage

Fresh open `scan` (VIX **13.28**, up from 13.03): NIFTY spot 24,272.55 ADX **24.18** → `range_bound: false`, BANKNIFTY 58,121.95 ADX **26.13** → `range_bound: false`, SENSEX 77,910.74 ADX **27.7** → `range_bound: false`. All three firmed further from the gate vs the first-intraday read (NIFTY 18.47→24.18, BANKNIFTY 16.17→26.13, SENSEX 20.46→27.7) on a directional up-move (NIFTY spot +68, BANKNIFTY +244, SENSEX +284). BANKNIFTY — range-bound earlier but DTE-blocked (Jul 28 monthly, DTE 11) — has now firmed clear of the ADX gate too, so the DTE-block is moot this run. **No index setup**, none near the 18 gate. Stocks unchanged (17 morning qualifiers still earnings-blocked into Jul 30; daily ADX static, no re-scan). Flat, 0 open positions, nothing to manage. No trade placed.

---

## 2026-07-17 (intraday-monitor addendum) — pre-market's range-bound board firmed away from the gate at the open; only BANKNIFTY range-bound (DTE-blocked); no index setup

Fresh open `scan` (VIX **13.03**, up from 12.88 pre-market): NIFTY spot 24,204.65 ADX **18.47** → `range_bound: false`, BANKNIFTY 57,877.65 ADX **16.17** → `range_bound: true`, SENSEX 77,626.4 ADX **20.46** → `range_bound: false`. The pre-market REGIME SHIFT (all three <18: NIFTY 16.40 / SENSEX 17.87) did **not** hold — NIFTY and SENSEX both firmed back above the 18 gate as spot ticked up ~130 pts / ~440 pts once the opening range printed (same "gate-hugger firms away rather than settling below" pattern seen 07-13/07-14). **No enterable index setup:** NIFTY/SENSEX now trending; BANKNIFTY qualifies on ADX (16.17) but only Jul 28 monthly (**DTE 11**) is listed, far outside its ≤7-DTE near-expiry window → DTE-blocked as always. Stocks unchanged (17 morning qualifiers still earnings-blocked into Jul 30; daily ADX static, no re-scan). Flat, 0 open positions, nothing to manage. No trade placed.

---

## 2026-07-17 — pre-market scan: REGIME SHIFT — all three indices range-bound; NIFTY & SENSEX are clean open candidates; stocks still earnings-blocked

India VIX **12.88** (low — the low-vol backdrop credit spreads like). After ~a week of all-trending
sessions (indices clustered mid-20s ADX), the chop regime is back: **all three indices read
range-bound at the pre-market board** — first time all three qualify together in over a week.

- **NIFTY** — spot 24,072.75, ADX(14) **16.40** → range-bound ✓. Clean iron-condor candidate.
- **BANKNIFTY** — spot 57,582.25, ADX(14) **10.68** → range-bound ✓ (deeply so), BUT only the
  Jul 28 monthly is listed = **DTE 11**, far outside its ≤7-DTE near-expiry data-gathering window →
  **skip on DTE grounds** (same structural block as every prior day; monthly-only, no weeklies).
- **SENSEX** — spot 77,186.87, ADX(14) **17.87** → range-bound ✓ (just under the 18 gate — a
  gate-hugger, re-check at the open since it could firm back above 18 like 07-13/07-14 did).

**Index conclusion:** NIFTY (16.40) and SENSEX (17.87) are the two candidate iron-condor setups to
carry into the market-open routine — but SENSEX is right at the gate, so confirm ADX<18 once the
opening range prints before entering. BANKNIFTY qualifies on ADX yet again but stays DTE-blocked.
Draft only, no trade placed per pre-market protocol. Candidate strikes (2/4 OTM off spot, for the
open routine to refine): **NIFTY** (step 50) SP24000 / LP23900 / SC24150 / LC24250, nearest weekly
~Jul 21 (DTE ~4; verify listing at open, prefer ~2 DTE if a nearer one exists); **SENSEX** (step 100)
SP77000 / LP76800 / SC77400 / LC77600, nearest weekly ~Jul 21–23 (confirm via `dhan.py lookup` at open).
Known sandbox blockers (DH-905/DH-906) may reject broker orders — portfolio.md-first, broker best-effort.

**Stock scan:** 17 qualifiers, ADX 11.05–16.17 (most range-bound first): SBIN 11.05, ULTRACEMCO 11.09,
HEROMOTOCO 11.15, TECHM 12.02, BPCL 12.35, PNB 12.80, JSWSTEEL 12.86, ADANIPORTS 12.89, BEL 13.60,
RELIANCE 13.63, HDFCLIFE 13.74, EICHERMOT 14.03, COALINDIA 14.26, HINDUNILVR 14.32, POWERGRID 14.40,
GRASIM 16.02, MARUTI 16.17 (TATAMOTORS errored — data fetch fail, not a signal). **All 17 remain
earnings-blocked, unchanged from prior days:** the only in-range stock expiry is the **Jul 30 monthly
(DTE 13)**, and Q1 (June-qtr) earnings season runs ~Jul 16–Aug 8 — entering now means holding a
short-vol condor straight through essentially every name's result (SBIN/MARUTI ~Jul 31 within 5 days
of expiry = hard-banned; others report during the hold). Per the standing earnings guardrail (an
*affirmative* clear is required and none can be given this cycle) → **skip all 17 on earnings**. Same
reference reasoning as the 2026-07-07 signals-learnings entry; no re-alerting. No positions open,
nothing to manage — flat into today.

---

## 2026-07-16 (intraday-monitor addendum, latest-5) — NIFTY & BANKNIFTY still range-bound; Position C held (flat); no new entry available

Fresh `scan` (VIX **12.9**): NIFTY spot 24,087.45 ADX **16.55** → `range_bound: true`, BANKNIFTY
57,533.2 ADX **14.32** → `range_bound: true`, SENSEX 77,334.65 ADX **19.87** → trending. NIFTY and
BANKNIFTY both hold below the 18 gate (NIFTY 14.46→16.55, BANKNIFTY 10.87→14.32) at a quiet VIX 12.9 —
but **no new entry available**: NIFTY already holds Position C (one-per-instrument); BANKNIFTY qualifies
on ADX but only Jul 28 monthly (DTE 12) is listed, far outside its ≤7-DTE near-expiry window; SENSEX
still trending. **Position C (NIFTY Jul 21) managed** vs last 1h candle (24,079.7–24,111.9): cost-to-close
68.06 (worst 68.15 < SL 137.58, best 68.05 > PT 34.40) → stays OPEN, ~flat (+₹47.45), pinned mid-range.
Stocks unchanged (17 morning qualifiers still earnings-blocked into Jul 30; daily ADX static, no re-scan).
No trade placed. Position C force-closes at EOD.

---

## 2026-07-16 (intraday-monitor addendum, latest-4) — NIFTY & BANKNIFTY still range-bound; Position C held (flat); no new entry available

Fresh `scan` (VIX **12.95**): NIFTY spot 24,086.6 ADX **14.46** → `range_bound: true`, BANKNIFTY
57,491.55 ADX **10.87** → `range_bound: true`, SENSEX 77,386.6 ADX **23.26** → trending. NIFTY and
BANKNIFTY both softened further below the 18 gate (NIFTY 17.03→14.46, BANKNIFTY 12.28→10.87) at a
quiet VIX 12.95 — but **no new entry available**: NIFTY already holds Position C (one-per-instrument);
BANKNIFTY qualifies on ADX but only Jul 28 monthly (DTE 12) is listed, far outside its ≤7-DTE
near-expiry window; SENSEX still trending. **Position C (NIFTY Jul 21) managed** vs last 1h candle
(24,079.85–24,122.2): cost-to-close 68.18 (worst 68.34 < SL 137.58, best 68.17 > PT 34.40) → stays
OPEN, ~flat (+₹39.65), pinned mid-range. Stocks unchanged (17 morning qualifiers still earnings-blocked
into Jul 30; daily ADX static, no re-scan). No trade placed. Position C force-closes at EOD.

---

## 2026-07-16 (intraday-monitor addendum, latest-3) — NIFTY & BANKNIFTY still range-bound; Position C held (flat); no new entry available

Fresh `scan` (VIX **12.8**): NIFTY spot 24,146.85 ADX **17.03** → `range_bound: true`, BANKNIFTY
57,651.45 ADX **12.28** → `range_bound: true`, SENSEX 77,432.79 ADX **25.81** → trending. NIFTY and
BANKNIFTY both hold below the 18 gate (NIFTY 17.96→17.03, BANKNIFTY 15.08→12.28) at a quiet VIX 12.8 —
but **no new entry available**: NIFTY already holds Position C (one-per-instrument); BANKNIFTY qualifies
on ADX but only Jul 28 monthly (DTE 12) is listed, far outside its ≤7-DTE near-expiry window; SENSEX
still trending. **Position C (NIFTY Jul 21) managed** vs last 1h candle (24,131.95–24,163.45): cost-to-close
68.29 (worst 68.56 < SL 137.58, best 68.11 > PT 34.40) → stays OPEN, ~flat (+₹32.50), pinned mid-range.
Stocks unchanged (17 morning qualifiers still earnings-blocked into Jul 30; daily ADX static, no re-scan).
No trade placed. Position C force-closes at EOD.

---

## 2026-07-16 (intraday-monitor addendum, latest-2) — NIFTY & BANKNIFTY now range-bound; Position C held (flat); no new entry available

Fresh `scan` (VIX **12.82**): NIFTY spot 24,152.7 ADX **17.96** → `range_bound: true`, BANKNIFTY
57,683.5 ADX **15.08** → `range_bound: true`, SENSEX 77,506.74 ADX **27.02** → trending. Two
indices dropped through the 18 gate vs this morning (NIFTY 22.45→17.96, BANKNIFTY 19.78→15.08) as
VIX eased to 12.82 — but **no new entry available**: NIFTY already holds Position C (one-per-instrument);
BANKNIFTY qualifies on ADX but only Jul 28 monthly (DTE 12) is listed, far outside its ≤7-DTE
near-expiry window; SENSEX still trending. **Position C (NIFTY Jul 21) managed** vs last 1h candle
(24,142.1–24,163.5): cost-to-close 68.43 (worst 68.61 < SL 137.58, best 68.27 > PT 34.40) → stays
OPEN, ~flat (+₹23), pinned mid-range. Stocks unchanged (17 morning qualifiers still earnings-blocked
into Jul 30; daily ADX static, no re-scan). No trade placed. Position C force-closes at EOD.

---

## 2026-07-16 (intraday-monitor addendum) — all three indices still trending, no setup; flat, nothing to manage

Fresh `scan` (VIX **13.06**): NIFTY spot 24,105.05 ADX **22.45**, BANKNIFTY 57,641.05 ADX **19.78**,
SENSEX 77,385.28 ADX **24.57** — **all `range_bound: false` (≥18)**. ADX eased slightly off the
pre-market board (NIFTY 26.51→22.45, BANKNIFTY 23.28→19.78, SENSEX 24.31→24.57); BANKNIFTY is
closest at 19.78 but still ~2 pts above the 18 gate — no re-check trigger. **No index entry.**
Stocks unchanged (17 morning qualifiers still earnings-blocked into Jul 30; daily ADX static, no
re-scan). Flat, 0 open positions, nothing to manage. No trade placed.

---

## 2026-07-16 — pre-market scan: all three indices trending, no setup; 17 stock qualifiers still earnings-blocked

India VIX **13.27** (low — the low-vol backdrop credit spreads like), but the ADX<18 entry gate
isn't met on any index; all three read clearly trending, none near the gate to re-check at the open:

- **NIFTY** — spot 24,078.5, ADX(14) **26.51** → trending. No entry.
- **BANKNIFTY** — spot 57,757.85, ADX(14) **23.28** → trending. No entry.
- **SENSEX** — spot 77,185.43, ADX(14) **24.31** → trending. No entry.

Essentially unchanged from yesterday's EOD board (NIFTY 26.45 / BANKNIFTY 24.22 / SENSEX 24.93,
VIX 13.27) — the mid-20s trend regime that held all of 07-15 carried overnight into 07-16. No
index draft to carry into the open.

**Stock scan — 17 qualifying (ADX<18 daily), all earnings-blocked:** SBIN 11.12, ULTRACEMCO 11.48,
TECHM 11.64, HEROMOTOCO 11.69, BPCL 12.12, JSWSTEEL 12.98, PNB 13.31, BEL 13.34, HDFCLIFE 13.62,
POWERGRID 13.89, RELIANCE 13.90, ADANIPORTS 13.91, HINDUNILVR 14.14, EICHERMOT 14.42, COALINDIA
14.67, GRASIM 14.83, MARUTI 15.88 (spots/hist_vol in scan output). Nearest stock expiry is the
**July monthly 2026-07-30 (DTE 14)** — right inside peak Q1 earnings season (~Jul 16–Aug 8), so
essentially every name reports during the hold. Per the standing earnings guardrail + the 2026-07-07
learnings, no name affirmatively clears (SBIN/MARUTI ~Jul 31 within 5 days of expiry = banned
outright; the rest held blind through a pending result) → **all 17 skipped on earnings grounds**,
same as every day this cycle. (TATAMOTORS errored in the scan — data fetch, not a signal.) Awaiting
Pushkar's steer on enter-post-earnings-name-by-name vs stand-aside-this-cycle (flagged 07-07).

**Conclusion:** no index setup (all trending, none near 18), no stock setup (all earnings-blocked).
No-trade day by default. Draft only — no order placed per pre-market protocol. If any index settles
<18 once the opening range prints, re-check at the open, but none is close enough today to expect it.
No positions open, nothing to manage.

---

## 2026-07-15 (intraday-monitor addendum, latest-5) — indices still trending, ADX clustered mid-20s; no index setup

Fresh scan (VIX **13.35**): NIFTY spot 24,088.7 ADX **26.51**, BANKNIFTY 57,698.95 ADX **24.85**,
SENSEX 77,183.71 ADX **25.43** — **all `range_bound: false` (≥18)**. Essentially flat vs the prior
addendum (NIFTY 26.63→26.51, BANKNIFTY 25.42→24.85, SENSEX 27.86→25.43), spot near-unchanged (NIFTY
24,070→24,089, SENSEX 77,198→77,184) — the mild down-drift/trend regime is holding into the close,
none near the 18 gate to re-check. **No index entry.** Stocks unchanged (17 qualifiers still
earnings-blocked into Jul 30; daily ADX static, no re-scan). Flat, no positions to manage. No trade
placed.

---

## 2026-07-15 (intraday-monitor addendum, latest-4) — indices still trending, NIFTY firmed back up; no index setup

Fresh scan (VIX **13.48**): NIFTY spot 24,070.0 ADX **26.63**, BANKNIFTY 57,690.05 ADX **25.42**,
SENSEX 77,198.47 ADX **27.86** — **all `range_bound: false` (≥18)**. NIFTY firmed back up vs the prior
addendum (21.09→26.63), BANKNIFTY eased (26.18→25.42), SENSEX flat (28.13→27.86), spot ticking down on
all three (NIFTY 24,158→24,070, SENSEX 77,548→77,198) — a mild down-drift, still directional not
range-bound, none near the 18 gate to re-check. **No index entry.** Stocks unchanged (17 qualifiers
still earnings-blocked into Jul 30; daily ADX static, no re-scan). Flat, no positions to manage. No
trade placed.

---

## 2026-07-15 (intraday-monitor addendum, latest-3) — indices still trending, NIFTY/BANKNIFTY eased a touch; no index setup

Fresh scan (VIX **13.13**): NIFTY spot 24,157.55 ADX **21.09**, BANKNIFTY 57,983.9 ADX **26.18**,
SENSEX 77,548.28 ADX **28.13** — **all `range_bound: false` (≥18)**. NIFTY/BANKNIFTY ADX eased vs the
prior addendum (NIFTY 25.16→21.09, BANKNIFTY 33.02→26.18) while SENSEX firmed marginally (27.86→28.13),
spot essentially flat (NIFTY 24,207→24,158, SENSEX 77,539→77,548). NIFTY is closest at 21.09 but still
~3 pts above the 18 gate — no re-check trigger; the morning rally's directional up-move is still holding.
**No index entry.** Stocks unchanged (17 qualifiers still earnings-blocked into Jul 30; daily ADX static,
no re-scan). Flat, no positions to manage. No trade placed.

---

## 2026-07-15 (intraday-monitor addendum, latest-2) — indices holding the directional trend late-session; no index setup

Fresh scan (VIX **13.11**): NIFTY spot 24,207.35 ADX **25.16**, BANKNIFTY 58,071.75 ADX **33.02**,
SENSEX 77,538.72 ADX **27.86** — **all `range_bound: false` (≥18)**. NIFTY/SENSEX ADX eased slightly
vs the prior addendum (NIFTY 29.08→25.16, SENSEX 29.76→27.86) while BANKNIFTY firmed (32.45→33.02),
spot essentially flat (SENSEX 77,607→77,539) — the morning rally's directional up-move is still
holding, none near the 18 gate to re-check. **No index entry.** Stocks unchanged (17 qualifiers
still earnings-blocked into Jul 30; daily ADX static, no re-scan). Flat, no positions to manage.
No trade placed.

---

## 2026-07-15 (intraday-monitor addendum, latest) — indices holding the directional trend into the afternoon; no index setup

Fresh scan (VIX **13.06**): NIFTY spot 24,203.65 ADX **29.08**, BANKNIFTY 58,075.45 ADX **32.45**,
SENSEX 77,607.29 ADX **29.76** — **all `range_bound: false` (≥18)**. Essentially unchanged vs the
prior addendum (NIFTY 30.67→29.08, BANKNIFTY 30.78→32.45, SENSEX 26.77→29.76) with spot flat-to-firmer
(SENSEX 77,466→77,607) — the morning rally's directional up-move is holding, none near the 18 gate to
re-check. **No index entry.** Stocks unchanged (17 qualifiers still earnings-blocked into Jul 30; daily
ADX static, no re-scan). Flat, no positions to manage. No trade placed.

---

## 2026-07-15 (intraday-monitor addendum) — indices firmed further into trend on a rally; no index setup materialized

Fresh scan (VIX **13.29**, down from 13.75 pre-market): NIFTY spot 24,204.2 ADX **30.67**,
BANKNIFTY 58,086.15 ADX **30.78**, SENSEX 77,465.99 ADX **26.77** — **all `range_bound: false`
(≥18)**. Spot rallied off the morning lows on all three (NIFTY 24,052→24,204, BANKNIFTY
57,462→58,086, SENSEX 77,055→77,466) — a directional up-move, the opposite of the range-bound
regime this strategy trades; none near the 18 gate to even re-check. **No index entry.** Stocks
unchanged (17 qualifiers still earnings-blocked into Jul 30; daily ADX static, no re-scan). Flat,
no positions to manage. No trade placed.

---

## 2026-07-15 (pre-market scan) — all three indices trending again (ADX 27-32), no index setup; 17 stock qualifiers still earnings-blocked into Jul 30

India VIX **13.75** (low — quiet backdrop). Flat into today (−₹210.90 realized from reset;
0 open positions). Yesterday's soft pre-market board (all three <18) resolved into a mild
down-drift regime through the session and has now firmed back into clear trend overnight:

- **Indices — none qualify (all ADX≥18):** NIFTY spot 24,052.05 ADX(14) **31.70**;
  BANKNIFTY 57,462.3 ADX **28.19**; SENSEX 77,054.94 ADX **26.91**. All well above the 18 gate
  and higher than yesterday's EOD reads (30.75/29.39/26.01) — the compression that made 07-14
  pre-market look range-bound has fully unwound; spot drifted modestly lower (NIFTY 24,044→24,052
  flat, SENSEX 77,116→77,055). No index iron-condor setup on any of the three; none near the gate
  to even re-check at the open. This is the regime the strategy is not built for.
- **Stocks — 17 of ~50 qualify (ADX<18), lowest-first:** SBIN 11.20, ULTRACEMCO 11.60,
  TECHM 11.64, HEROMOTOCO 12.08, BPCL 12.12, JSWSTEEL 13.66, POWERGRID 13.66, HINDUNILVR 13.68,
  ADANIPORTS 13.91, RELIANCE 13.98, EICHERMOT 14.03, HDFCLIFE 14.10, PNB 14.17, BEL 14.23,
  GRASIM 14.70, COALINDIA 14.93, MARUTI 15.88. Neither blocklisted name (AXISBANK/BHARTIARTL)
  qualifies. (TATAMOTORS errored — no data, as always.) Roster ~stable vs 07-14.
- **Earnings blocker persists:** only in-range stock expiry is the **Jul 30 monthly (15 DTE)**;
  a Jul 15→Jul 30 hold spans Q1 (June-qtr) season, now in full swing (mid-Jul→early-Aug cluster:
  HDFCLIFE/TECHM ~Jul 16, JSWSTEEL ~Jul 18, ULTRACEMCO ~Jul 21, RELIANCE mid-late Jul,
  EICHERMOT/SBIN/MARUTI/ADANIPORTS ~Jul 31). No qualifier affirmatively clears → **all 17 skipped
  on earnings grounds.** Earliest name-by-name post-report candidates (HDFCLIFE/TECHM) land ~Jul 16
  IF Pushkar picks enter-after-report. Still awaiting Pushkar's steer (enter-after-report vs.
  authorize hold-through-earnings vs. stand aside this cycle).

**Conclusion:** no draft trade — draft-only routine, no order placed. Indices trending hard
(no ADX<18 read to even re-check at the open); stocks remain log-and-skip on earnings. No-trade
is the correct, guardrail-consistent outcome. Flat — no positions to manage.

---

## 2026-07-14 (intraday-monitor addendum) — pre-market's range-bound board firmed away from the gate at the open; no index setup materialized

Fresh open scan (VIX **13.73**, up from 13.28 pre-market): NIFTY spot 24,120.1 ADX **18.9**,
BANKNIFTY 57,573.75 ADX **18.6**, SENSEX 77,281.0 ADX **19.16** — **all `range_bound: false`
(≥18)**. The soft pre-market board (14.61/15.80/16.81) did not hold: ADX rose back through the 18
gate on all three as spot ticked down modestly (NIFTY 24,211→24,120, SENSEX 77,616→77,281) and
VIX firmed. SENSEX Jul 16 (DTE 2), flagged this morning as the clean open candidate, no longer
qualifies. **No index entry** — same "gate-hugger firms away rather than settling below" pattern
seen 07-13. Stocks unchanged (17 qualifiers still earnings-blocked into Jul 30; daily ADX static,
no re-scan). Flat, no positions to manage. No trade placed.

---

## 2026-07-14 (pre-market scan) — ALL THREE indices now range-bound (<18); SENSEX Jul 16 (DTE 2) is the clean open candidate; 17 stock qualifiers still earnings-blocked

India VIX **13.28** (low — quiet backdrop). Flat into today (−₹210.90 realized from reset after
yesterday's two EOD force-closes). The compression the last few days flagged has resolved: **all
three indices read range-bound this morning** — first time the whole index board qualifies since
the early-July sell-off.

- **Indices — all three qualify (ADX<18):** NIFTY spot 24,211.0 ADX(14) **14.61**; BANKNIFTY
  58,131.45 ADX **15.80**; SENSEX 77,616.4 ADX **16.81**. Big drop from 07-13 (NIFTY 19.84→14.61,
  SENSEX 18.89→16.81, BANKNIFTY 33.21→15.80) — the consolidation deepened. **Open re-check
  candidates once the opening range prints:**
  - **NIFTY:** today (07-14) is the Jul 14 weekly **expiry day (DTE 0)** — same-day gamma/liquidity
    risk, the guardrail says avoid expiry-day if the chain looks thin. Prefer the **Jul 21 weekly
    (DTE 7)** if entering NIFTY, or skip NIFTY today. Don't reflexively sell the 0-DTE.
  - **SENSEX:** **Jul 16 (DTE 2)** — the cleanest setup, right on the preferred ~2-DTE sweet spot.
    Best index candidate for the open.
  - **BANKNIFTY:** qualifies on ADX (15.80) but only the **Jul 28 monthly (DTE 14)** is available —
    far outside the ≤7-DTE near-expiry window, so it stays a log/skip on DTE grounds (same standing
    issue; trade only as the data-gathering carve-out if near-expiry). No new alert.
- **Stocks — 17 of ~50 qualify (ADX<18), lowest-first:** TECHM 9.61, SBIN 10.89, ULTRACEMCO 11.51,
  HEROMOTOCO 12.42, POWERGRID 12.97, HDFCLIFE 13.43, RELIANCE 13.87, PNB 13.88, BPCL 14.00,
  EICHERMOT 14.07, HINDUNILVR 14.17, BEL 14.58, ADANIPORTS 15.03, JSWSTEEL 15.15, MARUTI 15.40,
  COALINDIA 15.72, GRASIM 16.41. (ITC dropped out — now 18.51 trending; roster else ~stable vs
  07-13.) Neither blocklisted name (AXISBANK/BHARTIARTL) qualifies. TATAMOTORS errored (no data).
- **Earnings blocker persists:** only in-range stock expiry is the **Jul 30 monthly (16 DTE)**; a
  Jul 14→Jul 30 hold spans Q1 (June-qtr) season, now in full swing. Confirmed mid-Jul→early-Aug
  cluster (HDFCLIFE/TECHM ~Jul 16, JSWSTEEL ~Jul 18, ULTRACEMCO ~Jul 21, RELIANCE mid-late Jul,
  EICHERMOT/SBIN/MARUTI/ADANIPORTS ~Jul 31) means **no qualifier affirmatively clears → all 17
  skipped on earnings grounds.** Earliest name-by-name post-report candidates (HDFCLIFE/TECHM) land
  ~Jul 16 IF Pushkar picks enter-after-report. Still awaiting Pushkar's steer (enter-after-report
  vs. authorize hold-through-earnings vs. stand aside this cycle).

**Conclusion:** no draft trade — draft-only routine, no order placed. Index picture is the softest
in weeks: **SENSEX Jul 16 (DTE 2) is a genuine open-entry candidate**, NIFTY only if taken on the
Jul 21 weekly (avoid the 0-DTE), BANKNIFTY log/skip on DTE. **Re-check ADX at market-open once the
opening range prints.** Stocks remain log-and-skip on earnings. Flat — no positions to manage.

---

## 2026-07-13 (pre-market scan) — NIFTY & SENSEX at the 18 gate (closest yet); 18 stock qualifiers, earnings block intact

India VIX **12.25** (low — quiet backdrop credit spreads like). First trading day of the week.
After last week's sharp sell-off consolidated, the indices have compressed right down to the gate —
NIFTY and SENSEX are now the closest they've been to qualifying since the drop began:

- **Indices — none qualify yet, but two are on the threshold:** NIFTY spot 24,206.9 ADX(14) **19.84**;
  BANKNIFTY 58,045.9 ADX **33.21**; SENSEX 77,569.39 ADX **18.89**. NIFTY and SENSEX both sit just
  above the 18 gate (recovered ~0.7-1.4% off the 07-09 lows; the consolidation keeps dragging ADX
  down). **Genuine open re-check candidates:** if either settles <18 once the opening range prints,
  it's a live iron-condor setup — NIFTY nearest expiry Jul 14 (DTE ~1, thin/gamma-risk — prefer a
  later expiry if liquidity looks poor) and SENSEX Jul 16 (DTE ~3). BANKNIFTY (33.21) still trending
  hard, no setup. Do NOT skip the open re-check — this is the softest index read in over a week.
- **Stocks — 18 of ~50 qualify (ADX<18), lowest-first:** TECHM 9.55, SBIN 11.32, ULTRACEMCO 11.34,
  HEROMOTOCO 12.94, BPCL 13.36, POWERGRID 13.89, HINDUNILVR 14.31, EICHERMOT 14.43, HDFCLIFE 14.51,
  RELIANCE 14.75, GRASIM 14.86, JSWSTEEL 14.91, PNB 15.08, ADANIPORTS 15.49, COALINDIA 15.84,
  MARUTI 15.86, BEL 16.15, ITC 16.88. Neither blocklisted name (AXISBANK/BHARTIARTL) qualifies.
  (TATAMOTORS errored — no data, as before.) Roster ~stable vs 07-09; SBILIFE now trending (20.34).
- **Earnings blocker persists:** only in-range stock expiry is the **Jul 30 monthly (17 DTE)**; a
  Jul 13→Jul 30 hold spans Q1 (June-qtr) season, now underway (TCS reported ~Jul 9-12, not a
  qualifier). Per the operating rule, an earnings-clean entry needs the name to have already
  reported or to report >5 days after Jul 30. As of Jul 13 the confirmed mid-Jul→early-Aug cluster
  (HDFCLIFE/TECHM ~Jul 16, JSWSTEEL ~Jul 18, ULTRACEMCO ~Jul 21, RELIANCE mid-late Jul,
  EICHERMOT/SBIN/MARUTI/ADANIPORTS ~Jul 31) still means **no qualifier affirmatively clears → all
  18 skipped on earnings grounds.** Earliest name-by-name post-report candidates (HDFCLIFE/TECHM)
  land ~Jul 16 — re-evaluate then IF Pushkar picks the enter-after-report option. Still awaiting
  Pushkar's steer (enter-after-report vs. authorize hold-through-earnings vs. stand aside this cycle).

**Conclusion:** no draft trade — draft-only routine, no order placed. But the index picture is the
softest in over a week: NIFTY (19.84) and SENSEX (18.89) are both a whisker above the gate, so an
index iron-condor setup could genuinely appear at the open. **Re-check ADX at market-open once the
opening range prints.** Stocks remain log-and-skip on earnings. No positions open, nothing to manage.

---

## 2026-07-09 (pre-market re-scan) — indices' ADX eased sharply but still all trending; 18 stock qualifiers, earnings block intact

Second pre-market scan of the day (fresh data snapshot). Picture unchanged in substance — no index
setup, stocks earnings-blocked — but the numbers moved notably vs. the earlier 07-09 read below:

- **India VIX 13.28** (down from 14.68 earlier today — the mild risk-off drift has partly unwound;
  low-vol backdrop restored).
- **Indices — all three still trending (≥18), but ADX collapsed off the earlier highs:** NIFTY spot
  24,030.45 ADX(14) **22.84** (was 52.98); BANKNIFTY 57,212.6 ADX **20.29** (was 46.93); SENSEX
  77,054.6 ADX **24.71** (was 53.45). Spot bounced ~0.6-0.8% off the earlier read (NIFTY 23,882→24,030,
  SENSEX 76,504→77,055, BANKNIFTY 56,743→57,213) — the sharp one-day sell-off is consolidating, which
  is exactly what drags ADX down. **None qualifies yet** (all above the 18 gate), but BANKNIFTY (20.29)
  and NIFTY (22.84) are now within striking distance — worth a re-check at market-open once the opening
  range prints, in case one settles below 18 intraday. SENSEX (24.71) still clearly trending.
- **Stocks — 18 of ~50 qualify (ADX<18), lowest-first:** TECHM 9.49, SBIN 12.04, ULTRACEMCO 12.17,
  HEROMOTOCO 12.91, POWERGRID 13.12, BPCL 13.17, HDFCLIFE 14.43, GRASIM 14.69, COALINDIA 14.94,
  EICHERMOT 14.94, HINDUNILVR 15.44, RELIANCE 15.45, ITC 15.78, JSWSTEEL 15.84, PNB 15.98, MARUTI 16.25,
  BEL 16.72, ADANIPORTS 16.86. Change vs. earlier scan: **SBILIFE dropped out** (now trending, ADX 18.25).
  Neither blocklisted name (AXISBANK/BHARTIARTL) qualifies. (TATAMOTORS errored — no data, as before.)
- **Earnings blocker persists (unchanged):** only in-range stock expiry is the **Jul 30 monthly (21 DTE)**;
  a Jul 9→Jul 30 hold spans Q1 (June-qtr) season, now underway (TCS today, runs to ~Aug 8). Per the
  operating rule, an earnings-clean entry needs the name to have already reported (none this early) or to
  report >5 days after Jul 30. Confirmed cluster (from 07-07/08 research): HDFCLIFE/TECHM ~Jul 16,
  JSWSTEEL ~Jul 18, ULTRACEMCO ~Jul 21, RELIANCE mid-late Jul, EICHERMOT/SBIN/MARUTI/ADANIPORTS ~Jul 31.
  **No qualifier affirmatively clears → all 18 skipped on earnings grounds.** Still awaiting Pushkar's
  steer (enter-after-report name-by-name vs. authorize hold-through-earnings vs. stand aside this cycle).

**Conclusion:** no draft to carry into market-open, but the index picture is softening — BANKNIFTY/NIFTY
ADX has fallen from the low-50s/mid-40s to ~20-23 as the sell-off consolidates, so an index setup could
plausibly appear if the chop deepens. Re-check ADX at the open. Stocks remain log-and-skip on earnings.
No positions open, nothing to manage. Draft-only routine — no trade placed.

---

## 2026-07-09 — pre-market scan: all three indices trending HARD, no index setup; 19 stock qualifiers still earnings-blocked

India VIX **14.68** (up from 12.34 on 07-08 — mild risk-off drift continues, but still a low-vol
backdrop overall). Fourth-plus consecutive session with **no index qualifier** — and today the
indices aren't just above the gate, they're strongly trending:

- **Indices — all three trending, no setup:** NIFTY spot 23,882.05 ADX(14) **52.98**; BANKNIFTY
  56,742.6 ADX **46.93**; SENSEX 76,503.6 ADX **53.45**. All ≫18. Spot slipped further from 07-08
  (NIFTY 24,196→23,882, ~-1.3%; SENSEX 77,608→76,504, ~-1.4%; BANKNIFTY 57,762→56,743, ~-1.8%) —
  the directional sell-off that began 07-08 is intact and ADX has surged, confirming trend not chop.
  No iron-condor entry on any index — this is exactly the regime the strategy is not built for.
- **Stocks — 19 of ~50 qualify (ADX(14) daily <18), sorted lowest-first:** TECHM 10.15, SBIN 11.47,
  ULTRACEMCO 12.99, HEROMOTOCO 13.08, POWERGRID 13.37, HDFCLIFE 13.45, BPCL 13.71, PNB 14.46,
  ITC 14.62, GRASIM 14.84, RELIANCE 15.26, COALINDIA 15.32, EICHERMOT 15.63, HINDUNILVR 15.76,
  ADANIPORTS 15.77, JSWSTEEL 16.64, MARUTI 17.04, SBILIFE 17.26, BEL 17.96. Neither blocklisted
  name (AXISBANK/BHARTIARTL) qualifies. (TATAMOTORS errored — no data, same as 07-08.)
- **Earnings blocker persists (unchanged from 07-07/07-08):** only in-range stock expiry is the
  **Jul 30 monthly (21 DTE)**; a Jul 9→Jul 30 hold spans Q1 (June-qtr) earnings season, which kicks
  off **today (07-09) with TCS** and runs to ~Aug 8. Per the operating rule in signals-learnings,
  an earnings-clean entry requires the name to have already reported (none have this early in the
  cycle) or to report >5 days after Jul 30. From 07-07/07-08 research the mid-Jul→early-Aug cluster
  is confirmed (ULTRACEMCO ~Jul 21, JSWSTEEL ~Jul 18, EICHERMOT ~Jul 31, ADANIPORTS ~Jul 31/Aug 1,
  SBIN ~Jul 31, MARUTI ~Jul 31, RELIANCE mid-late Jul, HDFCLIFE ~Jul 16, TECHM ~Jul 16) — every
  qualifier is either mid-hold or within 5 days of expiry. **No name affirmatively clears → all 19
  skipped on earnings grounds.** Still awaiting Pushkar's steer (enter-after-report name-by-name vs.
  authorize hold-through-earnings vs. stand aside on stocks this cycle).

**Conclusion:** no draft to carry into market-open. Indices strongly trending (no ADX<18 read to
even re-check at the open) and every stock qualifier is earnings-blocked into the Jul 30 monthly.
No-trade is the correct, guardrail-consistent outcome. No positions open, nothing to manage. As
names begin reporting later this month, the earliest post-earnings candidates (HDFCLIFE/TECHM
~Jul 16) could become enterable name-by-name IF Pushkar picks option (a) — until then, log-and-skip.

---

## 2026-07-08 (intraday-monitor — no pre-market ran today, this is the day's scan)

India VIX **12.34** (still low). No pre-market routine fired for 07-08, so this intraday run did the day's first scan.

- **Indices — all three trending, no setup:** NIFTY spot 24,195.95 ADX(14) **38.98**; BANKNIFTY 57,762.4 ADX **32.37**; SENSEX 77,608.36 ADX **36.07**. All ≫18 gate. Spot ticked down slightly from 07-07 EOD but ADX firmly trending. No index qualifier.
- **Stocks — 18 of ~50 qualify (ADX(14) daily <18), fresh scan:** TECHM 10.15, SBIN 10.97, ULTRACEMCO 12.37, HEROMOTOCO 12.73, POWERGRID 13.06, HDFCLIFE 13.28, BPCL 13.71, PNB 13.92, ITC 14.49, EICHERMOT 14.87, RELIANCE 15.02, COALINDIA 15.32, ADANIPORTS 15.59, HINDUNILVR 15.73, JSWSTEEL 15.95, GRASIM 15.97, SBILIFE 17.26, MARUTI 17.91. Neither blocklisted name (AXISBANK/BHARTIARTL) qualifies. (TATAMOTORS errored — no data.)
- **Earnings blocker persists (unchanged from 07-07):** only in-range stock expiry is the Jul 30 monthly (22 DTE); a Jul 8→Jul 30 hold spans Q1 (June-qtr) season (starts Jul 9 w/ TCS). Earnings-clean requires reporting before today (none) or >5 days after Jul 30 (after ~Aug 4). Fresh web check on this-day's top uncovered candidates confirms the mid-Jul-to-early-Aug cluster: ULTRACEMCO ~Jul 21, JSW Steel ~Jul 18, EICHERMOT ~Jul 31, ADANIPORTS ~Jul 31/Aug 1, HEROMOTOCO late-Jul/early-Aug — all either mid-hold or within 5d of expiry. Combined with 07-07's dates, **no name affirmatively clears** → all 18 skipped. Still awaiting Pushkar's steer (enter-after-report vs hold-through-earnings).

---

## 2026-07-07 (intraday-monitor addendum) — earnings-calendar research: Jul 30 stock expiry collides with Q1 season

Re-evaluated the 18 stock qualifiers under the new DTE 2-30 cap. The binding constraint flipped
from DTE to **earnings**. The only in-range stock expiry is the July monthly **2026-07-30** (23 DTE);
entering now holds through Q1 (June-qtr) results season (~Jul 16–Aug 8). Web-researched dates
(approximate — forward-dated sources conflate FY labels, so treat as directional):
- **SBIN ~Jul 31, MARUTI Jul 31** → within 5 days of the Jul 30 expiry → **banned** by the earnings
  guardrail (pre-earnings IV ramp hits the final near-expiry days).
- **COALINDIA** — trading window closed Jul 1, 2026, result imminent (mid-late July).
- **TECHM ~Jul 16, HDFCLIFE ~Jul 16, RELIANCE** mid-late July → condor held straight through the gap.
- Could not affirmatively clear a single one of the 18 → **all skipped** (see trade-log / signals-learnings).
Context anchors: HDFC Bank & ICICI confirmed Jul 18, 2026; TCS ~Jul 10-12 (none are qualifiers).
**Actionable:** the clean path is to enter each name **after it reports** (earnings behind us) for the
remaining DTE into Jul 30 — pending Pushkar's steer on whether to instead hold through earnings per
the DTE 2-30 backtest (which was on Bhavcopy that included earnings gaps).

---

## 2026-07-07 — pre-market scan: all three indices trending; 18 stocks range-bound (no index setup)

India VIX **11.82** (very low — extends the ~11.8-13.7 low-vol regime; the backdrop credit spreads
like, but ADX is the binding gate and it's failing on every index). Grind-up continues: NIFTY
24,270→24,430, SENSEX 77,763→78,285 vs yesterday — ADX rising with the one-way drift.

- **NIFTY** — spot 24,430.35, ADX(14) **30.61** → trending. No entry.
- **BANKNIFTY** — spot 58,291.5, ADX(14) **27.55** → trending. No entry. (Climbed out of the ~12-13
  range-bound reads of 07-03/07-06; no longer a qualifier, and DTE would block it anyway — July
  monthly 2026-07-28 only.)
- **SENSEX** — spot 78,285.07, ADX(14) **30.34** → clearly trending. No entry.

**INDEX CONCLUSION:** no qualifying index setup — all three trending hard (ADX ~27-31), none near
the 18 gate. Fourth-plus consecutive session with the indices grinding up and out of range-bound.
No index draft to carry into market-open. No positions open, nothing to manage.

**STOCK SCAN — 18 of ~50 qualify (ADX(14) daily < 18)**, sorted most range-bound first. Neither
blocklisted name (AXISBANK, BHARTIARTL) qualifies. Noted for any /trade call intraday:

| Stock | ADX | hist_vol% | spot | Stock | ADX | hist_vol% | spot |
|---|---|---|---|---|---|---|---|
| TECHM | 10.96 | 34.43 | 1406.5 | RELIANCE | 14.87 | 16.60 | 1321.3 |
| SBIN | 11.62 | 14.93 | 1037.7 | CANBK | 15.77 | 26.28 | 126.46 |
| PNB | 11.87 | 19.22 | 104.29 | MARUTI | 15.92 | 25.50 | 14456.0 |
| HEROMOTOCO | 12.40 | 19.56 | 4944.4 | BANKBARODA | 16.13 | 30.04 | 249.95 |
| ULTRACEMCO | 13.31 | 18.87 | 11661.0 | EICHERMOT | 16.21 | 25.89 | 7471.5 |
| SBILIFE | 13.39 | 17.28 | 1787.7 | TITAN | 16.70 | 23.96 | 4484.4 |
| ITC | 13.55 | 17.82 | 288.25 | HINDUNILVR | 17.62 | 20.67 | 2202.0 |
| POWERGRID | 14.11 | 18.46 | 285.4 | (TATAMOTORS errored — no data) | | | |
| HDFCLIFE | 14.41 | 21.40 | 564.2 | | | | |
| COALINDIA | 14.47 | 21.20 | 432.35 | | | | |
| BPCL | 14.58 | 29.19 | 308.15 | | | | |

**Earnings check (per guardrail: avoid results within 5 days of expiry):** Q1 FY26 season kicks off
**Thu Jul 9 with TCS** (not a qualifier — trending, ADX 22.93), then HCLTech Jul 13, Infosys Jul 23.
**None of the 18 qualifiers report this week (Jul 6-10).** TECHM is the only IT name in the list and
Tech Mahindra reports late July, outside the window — but re-confirm its exact date before any TECHM
/trade, given its high hist_vol (34.4%) already prices in some event risk. Banks/FMCG/auto names
(SBIN, ITC, RELIANCE, MARUTI, etc.) report late-July onward, so a near-expiry (≤7 DTE) condor placed
this week generally clears the earnings buffer — but verify each name's date at /trade time.

**Reminder for /trade:** per strategy.md hard guardrail, stock options remain gated ("no individual
stock options until this file says otherwise") pending a real paper track record — these qualifiers
are logged for situational awareness / a possible future /trade, not an authorization to open one
without the guardrail being lifted. Look up strike step + lot size fresh via `dhan.py lookup`, use
`hist_vol_pct` (not VIX) for premium estimates, and confirm short-leg OI > 1,000. Draft-only routine
— no trade placed.

---

## 2026-07-06 — pre-market scan: two trending, BANKNIFTY range-bound but DTE-blocked, no setup

India VIX **11.8** (very low — the low-vol backdrop credit spreads like, extending the ~11.8-13.7
low-vol regime of the past week). ADX<18 entry gate met on only one instrument, and that one fails
on DTE:

- **NIFTY** — spot 24,270.85, ADX(14) 23.51 → trending. No entry. (Drifted up ~400 pts off last
  week's ~23,865; ADX rising with the grind.)
- **BANKNIFTY** — spot 57,938.5, ADX(14) 12.75 → range_bound (only ADX qualifier). But nearest
  expiry is the July monthly 2026-07-28 (~22 DTE, no weeklies) — far outside the ≤7-DTE near-expiry
  window that is BANKNIFTY's sole rationale. Skip on DTE grounds, same as 07-03.
- **SENSEX** — spot 77,763.91, ADX(14) 26.5 → clearly trending. No entry.

**Conclusion:** no qualifying setup. NIFTY/SENSEX both trending; BANKNIFTY range-bound but
DTE-blocked. No draft to carry into market-open. NIFTY (23.51) is the closest of the two trenders —
worth a re-check at the open once the opening range prints, in case ADX settles below 18 intraday,
though it's well above threshold now. No positions open, nothing to manage. Draft-only routine, no
trade placed.

---

## 2026-07-03 — pre-market scan: only BANKNIFTY range-bound (NIFTY & SENSEX trending)

India VIX **12.29** (low — even lower than yesterday's 13.24, the kind of quiet backdrop credit
spreads like). The ADX<18 gate is met on only one of three today, and it's the non-validated one:

- **NIFTY** — spot 24,175.70, ADX(14) **22.92** → trending. No entry. (Yesterday's slow grind up
  to 24,175 lifted ADX above threshold; it's no longer range-bound.)
- **BANKNIFTY** — spot 58,031.65, ADX(14) **12.70** → range-bound ✓. Qualifies for entry.
- **SENSEX** — spot 77,502.12, ADX(14) **29.00** → clearly trending. No entry. (Yesterday's drift
  to 77,511 has pushed ADX sharply up; not a setup today.)

**Conclusion:** the only qualifying instrument is **BANKNIFTY**, which per strategy.md is the
*non-validated, data-gathering* instrument (monthly expiry only, no weekly). Trade it in paper mode
per the guardrail, tagging the entry with its DTE-at-entry, but keep it out of the NIFTY/SENSEX
win-rate figure. Draft only — no trade in pre-market per protocol. At the open, re-check ADX once
the opening range prints, confirm BANKNIFTY's current monthly expiry + per-leg securityIds via
`dhan.py lookup`, and note the DTE (monthly cycle means DTE is likely well above the ~2-day
preference — flag if it's far out, since signals-learnings shows long-dated BANKNIFTY barely moves
intraday and rarely hits profit target/stop, so expect incidental EOD drift, not a clean decay).
Candidate strikes (2/4 OTM off spot 58,031, step 100, lot 30): short put 57800 / long put 57600 /
short call 58200 / long call 58400. Known sandbox blockers (DH-905/DH-906) may reject the broker
order — portfolio.md-first, broker best-effort. No positions open, nothing to manage.

---

## 2026-07-02 — pre-market scan: NIFTY & SENSEX range-bound (first qualifying setups in days)

India VIX **13.24** (low — the low-vol backdrop credit spreads like). After three consecutive
all-trending sessions, the ADX<18 gate is finally met on two of three instruments:

- **NIFTY** — spot 24,005.85, ADX(14) **13.49** → range-bound ✓. Qualifies for iron-condor entry.
- **BANKNIFTY** — spot 58,033.05, ADX(14) 24.58 → trending. No entry.
- **SENSEX** — spot 76,922.64, ADX(14) **13.89** → range-bound ✓. Qualifies for iron-condor entry.

**Conclusion:** NIFTY and SENSEX both read clearly range-bound (ADX well below 18) with a low VIX
backdrop — two candidate iron-condor setups to carry into the market-open routine. Draft only, no
trade placed in pre-market per protocol. At the open, re-check ADX once the opening range prints,
then evaluate each against the guardrails (2/4-strike condor, ~2 DTE preferred, ≤5% capital risk,
stop-loss placed with entry). Note the known sandbox blockers (DH-905/DH-906) may reject broker
orders — portfolio.md-first, broker best-effort per the current process. No positions open.
Candidate strikes (2/4 OTM off spot, for open-routine reference): NIFTY ~23900/23800 P /
24100/24200 C (step 50); SENSEX ~76800/76600 P / 77100/77300 C (step 100).

---

## 2026-07-01 — pre-market scan: all three trending, no setup

India VIX **13.6** (low — the low-vol backdrop credit spreads like), but the ADX<18 entry gate
isn't met anywhere; every instrument reads trending:

- **NIFTY** — spot 23,865.75, ADX(14) 20.23 → not range-bound. No entry.
- **BANKNIFTY** — spot 57,542.9, ADX(14) 30.42 → clearly trending. No entry.
- **SENSEX** — spot 76,478.67, ADX(14) 19.98 → just above threshold, trending. No entry.

**Conclusion:** no instrument reads range-bound; none qualify for the iron-condor entry. No draft
to carry into market-open. SENSEX (19.98) and NIFTY (20.23) are closest — worth a re-check at the
open once the opening range prints, since ADX can settle below 18 intraday. No positions open,
nothing to manage. (Second consecutive session with all three trending; VIX has sat low ~13.6-13.7.)

---

## 2026-06-30 — pre-market scan (egress restored): all three trending, no setup

Egress is working again — the Yahoo Finance block from the earlier run today (see entry below)
has cleared; `scripts/market_data.py scan` returned clean data. India VIX **13.67** (low, the
kind of low-vol backdrop credit spreads like). But the ADX<18 entry gate isn't met anywhere:

- **NIFTY** — spot 23,897, ADX(14) 19.5 → not range-bound (just above the 18 threshold). No entry.
- **BANKNIFTY** — spot 57,703.5, ADX(14) 27.7 → clearly trending. No entry.
- **SENSEX** — spot 76,626.2, ADX(14) 22.8 → trending. No entry.

**Conclusion:** no instrument reads range-bound; none qualify for the iron-condor entry. No draft
to carry into market-open. NIFTY is closest (19.5) — worth re-checking at the open once the
opening range prints, since ADX can settle below 18 intraday. No positions open, nothing to manage.

---

## 2026-06-30 — pre-market scan BLOCKED: egress policy denies Yahoo Finance (and Telegram)

No scan data today. `python3 scripts/market_data.py scan` failed before returning any
spot/ADX/VIX numbers — the cloud environment's network egress policy is rejecting the data host.

- `query1.finance.yahoo.com:443` → 403 on CONNECT (policy denial), confirmed in the agent proxy's
  `recentRelayFailures`. This is the sole market-data source (Dhan sandbox 404s on all
  chain/quote endpoints, see signals-learnings), so with it blocked there is **no spot price, no
  ADX(14), no India VIX for any of NIFTY / BANKNIFTY / SENSEX.**
- `api.telegram.org:443` → also 403 on CONNECT. The Telegram notify channel is blocked too, so
  this couldn't be reported via `scripts/telegram.py` — flagged via the routine push channel instead.
- Per `/root/.ccr/README.md`, a policy 403/407 must NOT be retried or routed around — it's an org
  egress-policy decision, not a transient error or a script bug. Fix is on the environment side:
  allow `query1.finance.yahoo.com` (and `api.telegram.org`) in the session's network policy, or
  switch the environment to a more permissive policy. See
  https://code.claude.com/docs/en/claude-code-on-the-web for network-policy options.

**Conclusion: no setups assessed, no draft. No-trade by default — there is no data to evaluate
the ADX<18 entry condition against. Nothing to carry into the market-open routine until egress is
fixed.** (No positions are open, so nothing to manage either.)
