# Trade Log

Format per entry: `YYYY-MM-DD HH:MM IST | INSTRUMENT | DTE | action | strikes | credit/debit | qty | reason`

Log every trade placed, closed, or skipped (and why) — including a skipped trade when a guardrail
blocked it. Keep entries short (1-3 lines). Tail the last ~20 entries when reading this file in a
routine; don't re-read the whole history every time.

**Always include DTE-at-entry**, especially for BANKNIFTY — it's the unvalidated instrument (see
memory/strategy.md and memory/signals-learnings.md) and its results must be assessable separately
from NIFTY/SENSEX, which needs DTE visible per trade, not just instrument name.

---

## 2026-07-15 intraday-monitor — flat; NO index qualifier (all three trending, ADX 30.67/30.78/26.77, VIX 13.29); 17 stock qualifiers still ALL earnings-blocked

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier; complex firmed further into trend on a rally:** fresh `market_data.py scan` (VIX **13.29**) — NIFTY spot 24,204.2 ADX **30.67**, BANKNIFTY spot 58,086.15 ADX **30.78**, SENSEX spot 77,465.99 ADX **26.77**. All `range_bound: false` (≥18) → **no ADX qualifier**. ADX rose vs the pre-market read (NIFTY 31.70→30.67 ~flat high, BANKNIFTY 28.19→30.78, SENSEX 26.91→26.77) while spot rallied off the morning lows (NIFTY 24,052→24,204, BANKNIFTY 57,462→58,086, SENSEX 77,055→77,466) — a directional up-move, the opposite of the range-bound setup this strategy trades. None near the 18 gate. No entry.
  `2026-07-15 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 30.67/30.78/26.77 all ≥18, VIX 13.29 | — | — | indices trending on a directional rally, none near the 18 gate. No entry.`
- **Stock fresh-setup check — unchanged; morning's 17 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks per protocol). This morning's 17 qualifiers (SBIN 11.20 … MARUTI 15.88) are DTE-clear (Jul 30 monthly, 15 DTE) but a Jul 15→Jul 30 hold spans peak Q1 season — none affirmatively earnings-clear. No re-alert — steer still pending from Pushkar.
  `2026-07-15 intraday IST | STOCKS (17 qualifiers) | 15 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 17 but none earnings-clear. No entry.`
- **Git:** on read, local HEAD and `origin/main` both at 17539f8 (07-15 pre-market commit) after `git fetch origin main` — prior memory on `main`, no stranding. Clean fast-forward for this run's commit.
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no trade Telegram (per protocol).
- **Nothing contradicted backtest expectations** — indices trending on a directional move is the stand-aside regime; stock earnings collision is a recurring calendar constraint. No new signals-learnings entry needed.

---

## 2026-07-14 EOD square-off — flat all day; NO positions to close or carry; NO trade placed. Day realized ₹0; cumulative −₹210.90; capital ₹3,99,789.10

**Positions to process:** none — entered 07-14 flat (0 open paper positions) after yesterday's EOD force-close of both index condors, and every 07-14 intraday-monitor run (7 checks) found no qualifying setup, so nothing opened today. No index position to force-close, no stock condor to carry forward — the square-off is a clean no-op on positions.
- **Index side:** all three indices spent the entire session trending above the 18 gate — the soft pre-market board (NIFTY 14.61 / BANKNIFTY 15.80 / SENSEX 16.81) firmed away from 18 at the open and kept firming, ending the day at ADX 30.75 / 29.39 / 26.01 (VIX 13.85, latest-4 scan). Never the range-bound setup this strategy trades → no index entry all day, hence nothing to square off.
- **Stock side:** the day's 17 stock qualifiers (TECHM 9.61 … GRASIM 16.41, all ADX<18, Jul 30 monthly / 16 DTE) stayed blocked all day on the peak-Q1 earnings collision — none affirmatively earnings-clear. No stock condor was ever opened, so nothing to carry forward.
  `2026-07-14 EOD IST | ALL | — | NO-OP (flat, nothing to close/carry) | 0 open positions all day; no qualifying entry (indices ADX≥18 all session, 17 stock qualifiers earnings-blocked) | — | — | clean flat EOD.`
- **Day totals:** 0 trades closed today → **day realized ₹0**. Cumulative from reset unchanged at **−₹210.90** (yesterday's NIFTY −₹175.50 + SENSEX −₹35.40). Capital **₹3,99,789.10**. Flat into 07-15.
- **Broker:** no action (flat, nothing to place or close). **EOD Telegram summary sent** (always sent on the square-off run per protocol).
- **Nothing contradicted backtest expectations** — a full-session stand-aside (indices trending off the gate + stock earnings-season block) is an expected no-trade regime, not a thesis break. No new signals-learnings entry.

---

## 2026-07-14 intraday-monitor (latest-4) — flat; NO index qualifier (all three firmed FURTHER from the gate, ADX 30.75/29.39/26.01, VIX 13.85); 17 stock qualifiers still ALL earnings-blocked

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier; complex firmed further into the trend:** fresh `market_data.py scan` (VIX **13.85**) — NIFTY spot 24,043.6 ADX **30.75**, BANKNIFTY spot 57,400.05 ADX **29.39**, SENSEX spot 77,115.65 ADX **26.01**. All `range_bound: false` (≥18) → **no ADX qualifier**. ADX rose further from the prior addendum (NIFTY 26.24→30.75, BANKNIFTY 26.67→29.39, SENSEX 23.64→26.01) with spot flat-to-marginally-lower (NIFTY 24,070→24,044, SENSEX 77,215→77,116) — the soft pre-market board (14.61/15.80/16.81) has decisively and durably resolved into the mild down-drift/trend regime all session, the opposite of the range-bound setup this strategy trades. No entry.
  `2026-07-14 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 30.75/29.39/26.01 all ≥18, VIX 13.85 | — | — | pre-market range-bound board firmed away from 18 and kept firming all session. No entry.`
- **Stock fresh-setup check — unchanged; morning's 17 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks per protocol). This morning's 17 qualifiers (TECHM 9.61 … GRASIM 16.41) are DTE-clear (Jul 30 monthly, 16 DTE) but collide with peak Q1 season — none affirmatively earnings-clear. No re-alert — steer still pending from Pushkar.
  `2026-07-14 intraday IST | STOCKS (17 qualifiers) | 16 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 17 but none earnings-clear. No entry.`
- **Git:** on read, local HEAD and `origin/main` both at 9d6ed12 (the latest-3 commit) after `git fetch origin main` — prior run's memory is on `main`, no stranding. Clean fast-forward for this run's commit.
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no trade Telegram (per protocol).
- **Nothing contradicted backtest expectations** — indices firming off the 18 gate into a mild trend is the stand-aside regime; stock earnings collision is a recurring calendar constraint. No new signals-learnings entry needed.

---

## 2026-07-14 intraday-monitor (latest-3) — flat; NO index qualifier (all three still trending, ADX 26.24/26.67/23.64, VIX 13.66); 17 stock qualifiers still ALL earnings-blocked

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier; complex still holding the mild trend:** fresh `market_data.py scan` (VIX **13.66**) — NIFTY spot 24,069.85 ADX **26.24**, BANKNIFTY spot 57,416.25 ADX **26.67**, SENSEX spot 77,214.9 ADX **23.64**. All `range_bound: false` (≥18) → **no ADX qualifier**. Essentially unchanged from the prior addendum (NIFTY 25.75→26.24, BANKNIFTY 27.11→26.67, SENSEX 23.36→23.64) with spot flat-to-marginally-higher (NIFTY 24,066→24,070, SENSEX 77,152→77,215) — the soft pre-market board (14.61/15.80/16.81) stayed decisively resolved into the mild down-drift/trend regime all session, never the range-bound setup this strategy trades. No entry.
  `2026-07-14 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 26.24/26.67/23.64 all ≥18, VIX 13.66 | — | — | pre-market range-bound board firmed away from 18 and held trending all session. No entry.`
- **Stock fresh-setup check — unchanged; morning's 17 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks per protocol). This morning's 17 qualifiers (TECHM 9.61 … GRASIM 16.41) are DTE-clear (Jul 30 monthly, 16 DTE) but collide with peak Q1 season — none affirmatively earnings-clear. No re-alert — steer still pending from Pushkar.
  `2026-07-14 intraday IST | STOCKS (17 qualifiers) | 16 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 17 but none earnings-clear. No entry.`
- **Git:** on read, local HEAD, `origin/main`, and the fetched remote all agreed at d03dc17 (the latest-2 commit) — prior run's memory is on `main`, no stranding. Clean fast-forward for this run's commit.
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no trade Telegram (per protocol).
- **Nothing contradicted backtest expectations** — indices holding above the 18 gate in a mild trend is the stand-aside regime; stock earnings collision is a recurring calendar constraint. No new signals-learnings entry needed.

---

## 2026-07-14 intraday-monitor (latest-2) — flat; NO index qualifier (all three still trending, ADX 25.75/27.11/23.36, VIX 13.64); 17 stock qualifiers still ALL earnings-blocked

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier; complex firmed further into the mild trend:** fresh `market_data.py scan` (VIX **13.64**) — NIFTY spot 24,065.85 ADX **25.75**, BANKNIFTY spot 57,422.55 ADX **27.11**, SENSEX spot 77,151.71 ADX **23.36**. All `range_bound: false` (≥18) → **no ADX qualifier**. ADX ticked back up from the prior addendum (NIFTY 21.74→25.75, BANKNIFTY 23.43→27.11, SENSEX 21.81→23.36) as spot drifted a touch lower (NIFTY 24,123→24,066, SENSEX 77,325→77,152) — the soft pre-market board (14.61/15.80/16.81) has stayed decisively resolved into the mild down-drift regime all session, never the range-bound setup this strategy trades. No entry.
  `2026-07-14 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 25.75/27.11/23.36 all ≥18, VIX 13.64 | — | — | pre-market range-bound board firmed away from 18 and held trending all session. No entry.`
- **Stock fresh-setup check — unchanged; morning's 17 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks per protocol). This morning's 17 qualifiers (TECHM 9.61 … GRASIM 16.41) are DTE-clear (Jul 30 monthly, 16 DTE) but collide with peak Q1 season — none affirmatively earnings-clear. No re-alert — steer still pending from Pushkar.
  `2026-07-14 intraday IST | STOCKS (17 qualifiers) | 16 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 17 but none earnings-clear. No entry.`
- **Git note (checked, no problem — false alarm avoided):** on read, the local `origin/main` tracking ref appeared stale at the 07-09 EOD commit (018860d) while local HEAD carried all 07-13/07-14 work — looked at first like the CLAUDE.md "memory stranded off `main`" failure mode. Investigated before alerting: the push of this run's commit reported `4d82e11..08514af`, proving the **real** remote `main` was already at 4d82e11 (the 07-14 "latest" commit, which contains all prior 07-13/07-14 work) — i.e. `main` was fully current; only this session's local tracking ref was stale (never fetched after clone). My push was a normal clean fast-forward adding just this run's commit. **No stranding, no infra problem, no notification warranted.** Going forward: `git fetch origin main` before comparing, so a stale tracking ref isn't mistaken for a stranded `main`.
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no trade Telegram (per protocol).
- **Nothing contradicted backtest expectations** — indices holding above the 18 gate in a mild trend is the stand-aside regime; stock earnings collision is a recurring calendar constraint. No new signals-learnings entry needed.

---

## 2026-07-14 intraday-monitor (latest) — flat; NO index qualifier (all three still trending, ADX 21.74/23.43/21.81, VIX 13.47); 17 stock qualifiers still ALL earnings-blocked

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier; complex holding the mild down-drift regime:** fresh `market_data.py scan` (VIX **13.47**) — NIFTY spot 24,122.7 ADX **21.74**, BANKNIFTY spot 57,591.35 ADX **23.43**, SENSEX spot 77,324.61 ADX **21.81**. All `range_bound: false` (≥18) → **no ADX qualifier**. ADX eased slightly off the prior addendum's peak (NIFTY 23.59→21.74, BANKNIFTY 25.38→23.43, SENSEX 23.96→21.81) as spot ticked marginally back up (NIFTY 24,093→24,123, SENSEX 77,113→77,325), but all three remain clearly above the 18 gate — the soft pre-market board (14.61/15.80/16.81) has stayed resolved into a mild down-drift regime all session, never the range-bound setup this strategy trades. No entry.
  `2026-07-14 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 21.74/23.43/21.81 all ≥18, VIX 13.47 | — | — | pre-market range-bound board firmed away from 18 and held there all session. No entry.`
- **Stock fresh-setup check — unchanged; morning's 17 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks per protocol). This morning's 17 qualifiers (TECHM 9.61 … GRASIM 16.41) are DTE-clear (Jul 30 monthly, 16 DTE) but collide with peak Q1 season — none affirmatively earnings-clear. No re-alert — steer still pending from Pushkar.
  `2026-07-14 intraday IST | STOCKS (17 qualifiers) | 16 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 17 but none earnings-clear. No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram (per protocol).
- **Nothing contradicted backtest expectations** — indices holding above the 18 gate in a mild trend is the stand-aside regime; stock earnings collision is a recurring calendar constraint. No new signals-learnings entry needed.

---

## 2026-07-14 intraday-monitor (later) — flat; NO index qualifier (all three firmed FURTHER from the gate, ADX 23.59/25.38/23.96, VIX 13.71); 17 stock qualifiers still ALL earnings-blocked

**Positions to manage:** none — flat (0 open paper positions). Nothing for the exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier; the gate-huggers kept firming through the session:** fresh `market_data.py scan` (VIX **13.71**) — NIFTY spot 24,093.25 ADX **23.59**, BANKNIFTY spot 57,477.85 ADX **25.38**, SENSEX spot 77,113.27 ADX **23.96**. All `range_bound: false` → **no ADX qualifier**. ADX rose further from the earlier addendum read (NIFTY 18.9→23.59, BANKNIFTY 18.6→25.38, SENSEX 19.16→23.96) as spot kept ticking down (NIFTY 24,120→24,093, SENSEX 77,281→77,113) — the soft pre-market board (14.61/15.80/16.81) has now decisively firmed into a mild down-drift regime, the opposite of the range-bound setup this strategy trades. No entry.
  `2026-07-14 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 23.59/25.38/23.96 all ≥18, VIX 13.71 | — | — | pre-market range-bound board firmed decisively away from 18 through the session. No entry.`
- **Stock fresh-setup check — unchanged; morning's 17 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks per protocol). This morning's 17 qualifiers (TECHM 9.61 … GRASIM 16.41) are DTE-clear (Jul 30 monthly, 16 DTE) but collide with peak Q1 season — none affirmatively earnings-clear. No re-alert — steer still pending from Pushkar.
  `2026-07-14 intraday IST | STOCKS (17 qualifiers) | 16 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 17 but none earnings-clear. No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram (per protocol).
- **Nothing contradicted backtest expectations** — indices firming off the 18 gate into a mild trend is the stand-aside regime; stock earnings collision is a recurring calendar constraint. No new signals-learnings entry needed.

---

## 2026-07-14 intraday-monitor — flat; NO index qualifier (all three FIRMED away from the gate at the open, ADX 18.9/18.6/19.16, VIX 13.73); 17 stock qualifiers still ALL earnings-blocked

**Positions to manage:** none — flat (0 open paper positions) coming out of yesterday's EOD force-close. Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier; the pre-market's soft board firmed away from 18 once the opening range printed:** fresh `market_data.py scan` (VIX **13.73**, up from 13.28 pre-market) — NIFTY spot 24,120.1 ADX **18.9**, BANKNIFTY spot 57,573.75 ADX **18.6**, SENSEX spot 77,281.0 ADX **19.16**. All `range_bound: false` (≥18) → **no ADX qualifier**. This morning's pre-market flagged all three as range-bound (NIFTY 14.61, BANKNIFTY 15.80, SENSEX 16.81) with SENSEX Jul 16 (DTE 2) the clean open candidate — but by the open all three had **risen back through the 18 gate** (NIFTY 14.61→18.9, BANKNIFTY 15.80→18.6, SENSEX 16.81→19.16) as spot ticked down modestly (NIFTY 24,211→24,120, SENSEX 77,616→77,281) and ADX firmed with the drift. Softest pre-market board in weeks did NOT resolve into a setup — same "gate-hugger firms away, not below" pattern as 07-13. (NIFTY was in any case avoid-today on 0-DTE Jul 14 expiry; the Jul 21 weekly would have been the vehicle, but ADX ≥18 moots it. BANKNIFTY separately DTE-blocked, Jul 28 monthly only.)
  `2026-07-14 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 18.9/18.6/19.16 all ≥18, VIX 13.73 | — | — | pre-market range-bound board (14.61/15.80/16.81) firmed back through 18 at the open. No entry.`
- **Stock fresh-setup check — unchanged; morning's 17 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks per protocol). This morning's 17 qualifiers (TECHM 9.61 … GRASIM 16.41) are DTE-clear (Jul 30 monthly, 16 DTE) but Jul 30 collides with peak Q1 season — none affirmatively earnings-clear (HDFCLIFE/TECHM ~Jul 16, JSWSTEEL ~Jul 18, ULTRACEMCO ~Jul 21, RELIANCE mid-late Jul, EICHERMOT/SBIN/MARUTI/ADANIPORTS ~Jul 31). No re-alert — steer still pending from Pushkar.
  `2026-07-14 intraday IST | STOCKS (17 qualifiers) | 16 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 17 but none earnings-clear. No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram (per protocol).
- **Nothing contradicted backtest expectations** — indices firming back off the 18 gate is the stand-aside regime; the stock earnings-season collision is a recurring calendar constraint, not a thesis break. No new signals-learnings entry needed.

---

## 2026-07-13 EOD square-off — **FORCE-CLOSED both index condors** (A NIFTY −₹175.50, B SENSEX −₹35.40); day realized −₹210.90; flat into 07-14

**Both positions are INDEX condors → intraday-only, force-close at EOD.** Carry-forward requires ALL three conditions (currently in profit + ADX<18 + tightened stop); both fail condition 1 (each in small loss), so force-close — the normal index outcome.

**Final-hour candle check before recording P&L (spot-range, VIX 13.29):**
- **Position A (NIFTY Jul 14, DTE 1, credit 37.76, PT ≤18.88 / SL ≥75.52):** `spot-range NIFTY` high 24,250.85 / low 24,201.35, current spot 24,202.65. Cost-to-close @current 40.46 / @high 46.26 / @low 40.27. worst 46.26 < SL 75.52 AND best 40.27 > PT 18.88 → **no intra-hour trigger**, exit at current cost-to-close 40.46. Realized = (37.76−40.46)×65 = **−₹175.50**. Spot drifted ~58 pts up from the 24,144.75 entry into/through the 24250 short call.
  `2026-07-13 EOD IST | NIFTY | 1 | CLOSE iron condor (EOD_SQUAREOFF) | SP24050/LP23950/SC24250/LC24350 | exit cost 40.46 vs credit 37.76 | 1 lot | index intraday-only force-close; no PT/SL trigger in final hour. Realized −₹175.50.`
- **Position B (SENSEX Jul 16, DTE 3, credit 149.91, PT ≤74.96 / SL ≥299.82):** `spot-range SENSEX` high 77,741.58 / low 77,620.63, current spot 77,646.41. Cost-to-close @current 151.68 / @high 153.53 / @low 151.8. worst 153.53 < SL 299.82 AND best 151.68 > PT 74.96 → **no intra-hour trigger**, exit at current cost-to-close 151.68. Realized = (149.91−151.68)×20 = **−₹35.40**. Spot drifted ~219 pts up from the 77,427.86 entry to just above the 77600 short call.
  `2026-07-13 EOD IST | SENSEX | 3 | CLOSE iron condor (EOD_SQUAREOFF) | SP77200/LP77000/SC77600/LC77800 | exit cost 151.68 vs credit 149.91 | 1 lot | index intraday-only force-close; no PT/SL trigger in final hour. Realized −₹35.40.`
- **Broker:** `square-off-all` (best-effort) touched only the stale expired sid=71472 Jun artifact (SELL, TRANSIT) — the strategy legs were DH-905-blocked at entry and never in the broker, so paper close is authoritative. No new entry at EOD (flat is the correct end-of-day state; no fresh setup evaluated on the square-off run).
- **Day totals:** realized −₹210.90; cumulative from reset −₹210.90; capital ₹4,00,000 → **₹3,99,789.10**. **EOD Telegram summary sent.**
- **Nothing contradicted backtest expectations** — two small range-bound-drift losses (both < ₹200, both deep inside SL) on a day where spot ticked modestly up into the upper short strikes is exactly the ordinary "range-bound but not perfectly pinned → give back a few points of the credit" outcome; ~89% WR doesn't mean every condor prints, and small give-backs on the ~11% are expected. No new signals-learnings entry.

---

## 2026-07-13 (latest-3) intraday-monitor — managed both open index condors (A NIFTY + B SENSEX both stay OPEN, neither hit exit); NO new entry (NIFTY/SENSEX already open, BANKNIFTY DTE-blocked, stocks earnings-blocked)

**Positions managed against exit rules (last completed 1h candle, VIX 13.27):**
- **Position A (NIFTY Jul 14, DTE 1, entry credit 37.76, PT ≤18.88 / SL ≥75.52):** `spot-range NIFTY` candle high 24,238.25 / low 24,209.75, current ~24,216. Cost-to-close 41.47 (current) / 44.38 (high) / 41.06 (low). worst 44.38 < SL 75.52 AND best 41.06 > PT 18.88 → **neither threshold hit, stays OPEN.** Unrealized ≈ (37.76−41.47)×65 = −₹241 (spot drifted further up toward/through the 24250 short call, call side gained). Comfortably inside both thresholds. Must force-close by EOD today.
  `2026-07-13 latest-3 IST | NIFTY | 1 | HOLD (no exit) | SP24050/LP23950/SC24250/LC24350 | cost-to-close 41.47 vs credit 37.76 | 1 lot | neither PT≤18.88 nor SL≥75.52; force-close at EOD.`
- **Position B (SENSEX Jul 16, DTE 3, entry credit 149.91, PT ≤74.96 / SL ≥299.82):** `spot-range SENSEX` candle high 77,671.99 / low 77,621.16, current ~77,693. Cost-to-close 153.42 (current) / 151.96 (high) / 150.86 (low). worst 153.42 < SL 299.82 AND best 150.86 > PT 74.96 → **neither threshold hit, stays OPEN.** Unrealized ≈ (149.91−153.42)×20 = −₹70 (spot ticked up ~265 off the 77,427.86 entry to just above the 77600 short call, call side slightly ITM). Must force-close by EOD today.
  `2026-07-13 latest-3 IST | SENSEX | 3 | HOLD (no exit) | SP77200/LP77000/SC77600/LC77800 | cost-to-close 153.42 vs credit 149.91 | 1 lot | neither PT≤74.96 nor SL≥299.82; force-close at EOD.`
- **Index fresh-setup check — all three range_bound, but no new entry available:** fresh `scan` (VIX 13.27) — NIFTY 24,223.35 ADX **15.41**, BANKNIFTY 58,131.4 ADX **15.04**, SENSEX 77,684.9 ADX **16.21** — all `range_bound: true`. NIFTY and SENSEX qualify on ADX but already have open Positions A/B → one-per-instrument, skip. **BANKNIFTY qualifies on ADX (15.04) and has no open position, but its only available expiry is the July monthly 2026-07-28 = DTE 15** (re-confirmed via `dhan.py lookup`: Jul 14 weekly 404s / no weeklies, Jul 28 sid 61891 lot 30). 15 DTE is far outside BANKNIFTY's ≤7-DTE near-expiry data-gathering window + intraday-only no-theta-runway. **Skip on DTE grounds**, same as every prior run this cycle.
  `2026-07-13 latest-3 IST | NIFTY/SENSEX | — | SKIP | both range_bound but already have open Positions A/B (one-per-instrument) | — | — | no new entry.`
  `2026-07-13 latest-3 IST | BANKNIFTY | 15 | SKIP (DTE) | Jul 28 monthly only, ADX 15.04<18 qualifies but 15 DTE ≫ ≤7-DTE near-expiry window + intraday-only no-theta-runway | — | — | no entry.`
- **Stock fresh-setup check — unchanged; morning's 18 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX static intraday (didn't re-run scan-stocks per protocol). This morning's 18 qualifiers (TECHM 9.55 … ITC 16.88) are DTE-clear (Jul 30 monthly, 17 DTE) but Jul 30 collides with peak Q1 season — none affirmatively earnings-clear. No re-alert — steer still pending from Pushkar.
  `2026-07-13 latest-3 IST | STOCKS (18 qualifiers) | 17 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | no entry.`
- **Broker:** no action (no close, no new entry). No trade placed or closed → no Telegram (per protocol).
- **Nothing contradicted backtest expectations** — both condors sitting slightly-underwater (SENSEX spot now just above its upper short, NIFTY through its upper short) is normal for a range-bound-drifting-up day; both comfortably inside SL. BANKNIFTY DTE-block and stock earnings-block are recurring calendar constraints. No new signals-learnings entry. Both index condors MUST be force-closed by ~3:15 PM IST today per the index intraday-only rule (EOD-squareoff run to handle unless PT/SL hits first).

---

## 2026-07-13 (latest) intraday-monitor — managed both open index condors (A NIFTY + B SENSEX both stay OPEN, neither hit exit); NO new entry (NIFTY/SENSEX already open, BANKNIFTY DTE-blocked, stocks earnings-blocked)

**Positions managed against exit rules (last completed 1h candle, VIX 13.38):**
- **Position A (NIFTY Jul 14, DTE 1, entry credit 37.76, PT ≤18.88 / SL ≥75.52):** `spot-range NIFTY` candle high 24,222.65 / low 24,161.8, current 24,189.25. Cost-to-close 39.69 (current) / 42.74 (high) / 38.4 (low). worst 42.74 < SL 75.52 AND best 38.4 > PT 18.88 → **neither threshold hit, stays OPEN.** Unrealized ≈ (37.76−39.69)×65 = −₹125 (spot drifted up toward the 24250 short call, call side gained slightly). Comfortably inside both thresholds. Must force-close by EOD today.
  `2026-07-13 latest IST | NIFTY | 1 | HOLD (no exit) | SP24050/LP23950/SC24250/LC24350 | cost-to-close 39.69 vs credit 37.76 | 1 lot | neither PT≤18.88 nor SL≥75.52; force-close at EOD.`
- **Position B (SENSEX Jul 16, DTE 3, entry credit 149.91, PT ≤74.96 / SL ≥299.82):** `spot-range SENSEX` candle high 77,664.36 / low 77,583.41, current 77,586.95. Cost-to-close 151.18 (current) / 152.24 (high) / 151.14 (low). worst 152.24 < SL 299.82 AND best 151.14 > PT 74.96 → **neither threshold hit, stays OPEN.** Unrealized ≈ (149.91−151.18)×20 = −₹25, essentially flat (spot pinned mid-range between the 77200/77600 shorts). Must force-close by EOD today.
  `2026-07-13 latest IST | SENSEX | 3 | HOLD (no exit) | SP77200/LP77000/SC77600/LC77800 | cost-to-close 151.18 vs credit 149.91 | 1 lot | neither PT≤74.96 nor SL≥299.82; force-close at EOD.`
- **Index fresh-setup check — all three range_bound, but no new entry available:** fresh `scan` (VIX 13.38) — NIFTY 24,189.25 ADX **14.21**, BANKNIFTY 57,950.8 ADX **12.26**, SENSEX 77,586.95 ADX **17.26** — all `range_bound: true`. NIFTY and SENSEX qualify on ADX but already have open Positions A/B → one-per-instrument, skip. **BANKNIFTY qualifies on ADX (12.26) and has no open position, but its only available expiry is the July monthly 2026-07-28 = DTE 15** (confirmed via `dhan.py lookup`: Jul 14 weekly 404s / no weeklies, Jul 28 sid 61886 lot 30). 15 DTE is far outside BANKNIFTY's ≤7-DTE near-expiry data-gathering window (its sole rationale per strategy.md), and as an index it's intraday-only — a 15-DTE condor entered and force-closed same day captures ~zero theta. **Skip on DTE grounds**, same as every prior run this cycle.
  `2026-07-13 latest IST | NIFTY/SENSEX | — | SKIP | both range_bound but already have open Positions A/B (one-per-instrument) | — | — | no new entry.`
  `2026-07-13 latest IST | BANKNIFTY | 15 | SKIP (DTE) | Jul 28 monthly only, ADX 12.26<18 qualifies but 15 DTE ≫ ≤7-DTE near-expiry window + intraday-only no-theta-runway | — | — | no entry.`
- **Stock fresh-setup check — unchanged; morning's 18 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX static intraday (didn't re-run scan-stocks per protocol). This morning's 18 qualifiers (TECHM 9.55 … ITC 16.88) are DTE-clear (Jul 30 monthly, 17 DTE) but Jul 30 collides with peak Q1 season — none affirmatively earnings-clear. No re-alert — steer still pending from Pushkar.
  `2026-07-13 latest IST | STOCKS (18 qualifiers) | 17 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | no entry.`
- **Broker:** no action (no close, no new entry). No trade placed or closed → no Telegram (per protocol).
- **Nothing contradicted backtest expectations** — both condors sitting slightly-underwater near mid-range is normal for a range-bound day; BANKNIFTY DTE-block and stock earnings-block are recurring calendar constraints. No new signals-learnings entry. Both index condors MUST be force-closed by ~3:15 PM IST today per the index intraday-only rule (EOD-squareoff run to handle unless PT/SL hits first).

---

## 2026-07-13 (later) intraday-monitor — managed both open index condors (A NIFTY + B SENSEX both stay OPEN, neither hit exit); NO new entry (NIFTY/SENSEX already open, BANKNIFTY DTE-blocked, stocks earnings-blocked)

**Positions managed against exit rules (last completed 1h candle, VIX 13.38):**
- **Position A (NIFTY Jul 14, DTE 1, entry credit 37.76, PT ≤18.88 / SL ≥75.52):** `spot-range NIFTY` candle high 24,207.7 / low 24,168.9, current 24,199.85. Cost-to-close 40.49 (current) / 41.18 (high) / 38.61 (low). worst 41.18 < SL 75.52 AND best 38.61 > PT 18.88 → **neither threshold hit, stays OPEN.** Unrealized ≈ (37.76−40.49)×65 = −₹177 (spot drifted up toward the 24250 short call vs 24,144.75 at entry, call side gained a touch). Slightly more underwater than last check (−₹22) but comfortably inside both thresholds. Must force-close by EOD today.
  `2026-07-13 later IST | NIFTY | 1 | HOLD (no exit) | SP24050/LP23950/SC24250/LC24350 | cost-to-close 40.49 vs credit 37.76 | 1 lot | neither PT≤18.88 nor SL≥75.52; force-close at EOD.`
- **Position B (SENSEX Jul 16, DTE 3, entry credit 149.91, PT ≤74.96 / SL ≥299.82):** `spot-range SENSEX` candle high 77,587.44 / low 77,489.19, current 77,556.34. Cost-to-close 150.85 (current) / 151.19 (high) / 150.29 (low). worst 151.19 < SL 299.82 AND best 150.29 > PT 74.96 → **neither threshold hit, stays OPEN.** Unrealized ≈ (149.91−150.85)×20 = −₹19, essentially flat (spot ticked up ~130 off the 77,427.86 entry, still pinned mid-range between the 77200/77600 shorts). Must force-close by EOD today.
  `2026-07-13 later IST | SENSEX | 3 | HOLD (no exit) | SP77200/LP77000/SC77600/LC77800 | cost-to-close 150.85 vs credit 149.91 | 1 lot | neither PT≤74.96 nor SL≥299.82; force-close at EOD.`
- **Index fresh-setup check — all three now range_bound, but no new entry available:** fresh `scan` (VIX 13.38) — NIFTY spot 24,199.85 ADX **13.77**, BANKNIFTY 57,950.7 ADX **14.99**, SENSEX 77,556.34 ADX **13.29** — all `range_bound: true` (regime fully softened; BANKNIFTY crossed <18 too, was 18.51 at 11:38). NIFTY and SENSEX both qualify on ADX but already have open Positions A/B → one-per-instrument, skip. **BANKNIFTY qualifies on ADX (14.99) and has no open position, but its only available expiry is the July monthly 2026-07-28 = DTE 15** (confirmed via `dhan.py lookup`: sid 61884, lot 30; Jul 14/Jul 16 both 404 — no weeklies). 15 DTE is far outside BANKNIFTY's ≤7-DTE near-expiry data-gathering window (its sole rationale per strategy.md), and as an index it's intraday-only — a 15-DTE condor entered and force-closed same day captures ~zero theta and just drifts to EOD (the documented long-dated-BANKNIFTY low-value outcome). **Skip on DTE grounds**, same as 07-06/07-07/07-09.
  `2026-07-13 later IST | NIFTY/SENSEX | — | SKIP | both range_bound but already have open Positions A/B (one-per-instrument) | — | — | no new entry.`
  `2026-07-13 later IST | BANKNIFTY | 15 | SKIP (DTE) | Jul 28 monthly only, ADX 14.99<18 qualifies but 15 DTE ≫ ≤7-DTE near-expiry window + intraday-only no-theta-runway | — | — | no entry.`
- **Stock fresh-setup check — unchanged; morning's 18 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX static intraday (didn't re-run scan-stocks per protocol). This morning's 18 qualifiers (TECHM 9.55 … ITC 16.88) are DTE-clear (Jul 30 monthly, 17 DTE) but Jul 30 collides with peak Q1 season — none affirmatively earnings-clear. No re-alert — steer still pending from Pushkar.
  `2026-07-13 later IST | STOCKS (18 qualifiers) | 17 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | no entry.`
- **Broker:** no action (no close, no new entry). No trade placed or closed → no Telegram (per protocol).
- **Nothing contradicted backtest expectations** — both condors sitting flat/slightly-underwater near mid-range is normal for a range-bound day; BANKNIFTY DTE-block and stock earnings-block are recurring calendar constraints. No new signals-learnings entry. Both index condors MUST be force-closed by ~3:15 PM IST today per the index intraday-only rule (EOD-squareoff run to handle unless PT/SL hits first).

---

## 2026-07-13 11:38 IST intraday-monitor — **ENTERED SENSEX iron condor** (2nd position of the day); managed open NIFTY condor (stays open, flat)

**Positions to manage on entry:** Position A (NIFTY Jul 14 condor, opened 10:37). Checked vs last completed 1h candle via `spot-range NIFTY` (high 24,158.8 / low 24,133.0, current 24,142.55) — cost-to-close 38.10 (current) / 38.22 (high) / 38.23 (low): worst 38.23 < SL 75.52 and best 38.10 > PT 18.88 → **neither threshold hit, Position A stays OPEN**, essentially flat (unrealized ≈ (37.76−38.10)×65 = −₹22). Spot pinned mid-range between the 24050/24250 shorts. Must be force-closed by EOD today per index intraday-only rule.
- **Index setup — SENSEX QUALIFIES and traded:** fresh `market_data.py scan` at 11:38 IST (VIX **13.35**) — SENSEX spot 77,427.86 ADX **13.99 → range_bound: true** (no open SENSEX position); NIFTY 24,142.55 ADX 14.49 range_bound but already has Position A → skip; BANKNIFTY 57,865.55 ADX 18.51 (trending ≥18, no). SENSEX settled clearly into range-bound (down from 19.37 at 10:37). ADX re-confirmed 13.99 via `adx SENSEX`. 11:38 IST → full runway to EOD.
  - **Trade placed:** SENSEX Jul 16 (DTE 3) iron condor — **SP 77200PE / LP 77000PE / SC 77600CE / LC 77800CE**, 1 lot (20). DTE 3 chosen: nearest available SENSEX weekly (Jul 16 Thu), within validated 1-6 range, near the ~2-DTE preference; closed intraday today so never held to expiry. Leg premiums (BS, spot 77,427.86, VIX 13.35, DTE 3): 263.73 / 191.99 / 301.98 / 223.81 → **net credit 149.91/unit = ₹2,998.20**. Max loss (200−149.91)×20 = ₹1,001.80 (within 5% cap). PT cost-to-close ≤74.96, SL ≥299.82.
  `2026-07-13 11:38 IST | SENSEX | 3 | OPEN iron condor | SP77200/LP77000/SC77600/LC77800 | +149.91/unit credit (₹2,998.20) | 1 lot | ADX 13.99<18 qualifies, VIX 13.35, full runway. Broker REJECTED DH-905 (known sandbox blocker) — paper position authoritative.`
- **Other indices:** NIFTY (ADX 14.49) range_bound but Position A already open → one-per-instrument, skip. BANKNIFTY (ADX 18.51) just above the gate, trending → no entry.
  `2026-07-13 11:38 IST | NIFTY/BANKNIFTY | — | SKIP | NIFTY already has open Position A; BANKNIFTY ADX 18.51≥18 | — | — | no new entry.`
- **Stock fresh-setup check — unchanged; morning's 18 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks). This morning's 18 qualifiers (TECHM 9.55 … ITC 16.88) are DTE-clear (Jul 30 monthly, 17 DTE) but Jul 30 collides with peak Q1 season — none affirmatively earnings-clear. No re-alert — steer still pending from Pushkar.
  `2026-07-13 11:38 IST | STOCKS (18 qualifiers) | 17 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | No entry.`
- **Broker:** `place-spread` REJECTED with DH-905 (documented long-standing sandbox blocker). Paper position logged to portfolio.md regardless (source of truth in paper mode). Telegram sent (trade placed).
- **Note:** Both index condors (A NIFTY Jul 14, B SENSEX Jul 16) MUST be force-closed by ~3:15 PM IST today per the index intraday-only rule, unless PT/SL hits first.

---

## 2026-07-13 10:37 IST intraday-monitor — **ENTERED NIFTY iron condor** (first trade since 07-02); NIFTY settled into range-bound at the open (ADX 17.65<18)

**Positions to manage on entry:** none pre-existing — flat coming in. Opened one new NIFTY IC this run (details below).
- **Index setup — NIFTY QUALIFIES and traded:** fresh `market_data.py scan` at 10:37 IST (VIX **13.33**) — **NIFTY spot 24,144.75 ADX 17.65 → range_bound: true** (first index qualifier to actually resolve since the 07-09 late-day cross); BANKNIFTY 58,027.45 ADX 24.36 (trending, no); SENSEX 77,290.19 ADX 19.37 (trending, no). The pre-market flagged NIFTY (19.84) and SENSEX (18.89) as gate-huggers and said "do NOT skip the open re-check" — NIFTY duly settled below 18 once the opening range printed. Early session (10:37, full runway to EOD) → genuine open-entry, exactly the setup the forward notes said not to skip. ADX re-confirmed 17.65 via `adx NIFTY`.
  - **Trade placed:** NIFTY Jul 14 (DTE 1) iron condor — **SP 24050PE / LP 23950PE / SC 24250CE / LC 24350CE**, 1 lot (65). DTE 1 chosen: nearest available NIFTY weekly, closest to the ~2-DTE preference (next is Jul 21 DTE 8), within the validated 1-6 range; index closes intraday today so the position is never held into Jul 14 same-day-expiry gamma. Leg premiums (BS, spot 24,144.75, VIX 13.32, DTE 1): 28.8 / 9.75 / 28.3 / 9.59 → **net credit 37.76/unit = ₹2,454.40**. Max loss (100−37.76)×65 = ₹4,045.60 (within 5% cap). PT cost-to-close ≤18.88, SL ≥75.52.
  `2026-07-13 10:37 IST | NIFTY | 1 | OPEN iron condor | SP24050/LP23950/SC24250/LC24350 | +37.76/unit credit (₹2,454.40) | 1 lot | ADX 17.65<18 qualifies, VIX 13.33, early session full runway. Broker REJECTED DH-905 (known sandbox blocker) — paper position authoritative.`
- **Other indices:** BANKNIFTY (ADX 24.36) and SENSEX (19.37) both trending ≥18 → no entry. SENSEX just above the gate again but not through.
  `2026-07-13 10:37 IST | BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 24.36/19.37 ≥18, VIX 13.33 | — | — | both trending. No entry.`
- **Stock fresh-setup check — unchanged; morning's 18 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks). This morning's 18 qualifiers (TECHM 9.55 … ITC 16.88) are DTE-clear (Jul 30 monthly, 17 DTE) but Jul 30 collides with peak Q1 season — none affirmatively earnings-clear. No re-alert — steer still pending from Pushkar.
  `2026-07-13 10:37 IST | STOCKS (18 qualifiers) | 17 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 18 but none earnings-clear. No entry.`
- **Broker:** `place-spread` REJECTED with DH-905 (sandbox OMS rejects current weekly securityIds — the documented long-standing blocker). Paper position logged to portfolio.md regardless (source of truth in paper mode). Telegram sent (trade placed).
- **Note:** this NIFTY condor MUST be force-closed by ~3:15 PM IST today per the index intraday-only rule, unless PT/SL hits first. The next intraday-monitor / EOD-squareoff run must manage/close it.

---

## 2026-07-13 intraday-monitor — flat; NO index qualifier (all three FIRMED away from the gate, ADX 24/33/22, VIX 13.31); 18 stock qualifiers still ALL earnings-blocked

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier; the pre-market gate-huggers pulled BACK away from 18:** fresh `market_data.py scan` (VIX **13.31**, up from 12.25 pre-market) — NIFTY spot 24,036.6 ADX **24.48**, BANKNIFTY spot 57,686.45 ADX **32.69**, SENSEX spot 76,967.37 ADX **22.3**. All `range_bound: false` (≥18) → **no ADX qualifier**. This morning's pre-market flagged NIFTY (19.84) and SENSEX (18.89) as on-the-threshold open re-check candidates, but by this run both had **risen** off the gate (NIFTY 19.84→24.48, SENSEX 18.89→22.3) rather than settling below — spot ticked down modestly (NIFTY 24,207→24,037, SENSEX 77,569→76,967) and ADX firmed with the drift. Softest index read of the week did NOT resolve into a setup. BANKNIFTY (32.69) still clearly trending → DTE moot.
  `2026-07-13 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 24.48/32.69/22.3 all ≥18, VIX 13.31 | — | — | pre-market gate-huggers (NIFTY 19.84/SENSEX 18.89) firmed away from 18, not below it. No entry.`
- **Stock fresh-setup check — unchanged; morning's 18 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks per protocol). This morning's 18 qualifiers (TECHM 9.55 … ITC 16.88) are DTE-clear (Jul 30 monthly, 17 DTE) but the Jul 30 expiry collides with peak Q1 season — none affirmatively earnings-clear (HDFCLIFE/TECHM ~Jul 16, JSWSTEEL ~Jul 18, ULTRACEMCO ~Jul 21, RELIANCE mid-late Jul, EICHERMOT/SBIN/MARUTI/ADANIPORTS ~Jul 31). No re-alert — already Telegram-flagged 07-07, steer still pending from Pushkar.
  `2026-07-13 intraday IST | STOCKS (18 qualifiers) | 17 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 18 but none earnings-clear. No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — indices firming back off the 18 gate is the stand-aside regime; the stock earnings-season collision is a recurring calendar constraint, not a thesis break. No new signals-learnings entry needed.

---

## 2026-07-09 EOD square-off (CANONICAL — scheduled cron run) — NO-OP, flat all day: 0 open positions, 0 trades; day P&L ₹0

`2026-07-09 EOD IST | — | — | NO-OP (no strategy positions, no trades) | nothing to close/carry`
- **This is the true scheduled EOD square-off** (an earlier premature routine wrote an EOD-labelled NO-OP lower in this log before the 14:37 intraday run; this canonical run confirms the day's final flat state). Also fixed a real infra problem this run: **8 commits (weekly-review + all 07-09 intraday runs + the earlier EOD entry) were committed locally but never pushed to `origin/main`** — the exact "memory lost on next fresh clone" failure mode CLAUDE.md warns about. Pushed all to main this run.
- **Positions to carry/close:** none — flat the entire session. Broker `orders` shows only the stale expired `sid=71472` NIFTY-Jun2026-24000-CE (TRADED, drvExpiryDate 2026-06-25) — not a strategy position, will lapse on its own. `funds`: utilizedAmount ₹934,698 / availableBalance ₹65,301 (the known locked artifact). No index condor to force-close, no stock condor to evaluate for carry-forward — both paths N/A. No spot-range candle check needed (no position to price).
- **No-trade day recap:** **Indices** trended most of the session, ADX easing steadily off the pre-market highs (52.98/46.93/53.45) as the 07-08 sell-off consolidated, finally crossing below the 18 gate only at the 14:37 last slot (NIFTY 17.13, BANKNIFTY 16.38, SENSEX 14.91, VIX 13.15) — first index qualifier in >1 week, but too late in the session to open a same-day-close intraday condor (no theta runway before forced EOD). **Stocks:** 18 F&O names cleared ADX<18 (daily) and the DTE gate (Jul 30 monthly, 21 DTE) but ALL skipped on earnings grounds — Jul 30 is the only in-range expiry and it collides with peak Q1 season; no name affirmatively earnings-clear. Steer still pending from Pushkar (flagged 07-07).
- **Circuit breaker:** DISABLED in paper mode (no daily loss cap). Day P&L ₹0 regardless.
- **Final state:** cash ₹4,00,000.00 (unchanged, post-2026-07-07 reset), realized P&L from reset ₹0.00, today's P&L ₹0. Flat into the close. EOD Telegram summary sent.
- **FORWARD NOTE for Fri 07-10:** indices ended range-bound (ADX 17/16/15, VIX 13.15) — if ADX holds <18 at the 07-10 open, NIFTY (Jul 14, DTE 4) and SENSEX (Jul 16, DTE 6) are genuine open-entry iron-condor candidates with full-session runway. Do NOT skip at the open if it persists. (BANKNIFTY still DTE-blocked at 19; SENSEX use Jul 16 not the same-day expiry.)
- **Nothing contradicted backtest expectations** — a cooling-but-still-trending tape that only crossed range-bound at the bell is the stand-aside regime given intraday-only + open-entry-timing constraints; the stock earnings collision is a recurring calendar constraint. No new signals-learnings entry needed.

---

## 2026-07-09 14:37 IST intraday-monitor (LAST slot, 2:30 PM IST cron) — REGIME SHIFT: all three indices FINALLY range-bound (first index qualifier in >1 week) but ALL SKIPPED on entry-TIMING grounds (too late to enter a same-day-close intraday condor)

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — ALL THREE now qualify on ADX, but SKIPPED on timing:** fresh `market_data.py scan` (VIX **13.15**) — NIFTY spot 24,052.85 ADX **17.13**, BANKNIFTY spot 57,332.8 ADX **16.38**, SENSEX spot 76,992.8 ADX **14.91**. All three `range_bound: true` (<18) — **the 07-08 sell-off has finished consolidating into chop and the whole complex crossed below the 18 gate for the first time in over a week** (ADX eased all of 07-09: 52.98/46.93/53.45 → 20.08/18.64/18.95 at 13:37 → now 17.13/16.38/14.91). This is the exact range-bound regime the strategy is built for. **BUT it's 14:37 IST — this routine fired on the last intraday slot (cron `0 4-9` = 9:30 AM–2:30 PM IST), ~38 min to the mandatory EOD square-off** (indices intraday-only, must close today). Entering a 5–7 DTE condor now captures ~zero theta before forced close and just drifts to EOD + eats bid-ask — the **"late-day entry leaves no runway before forced EOD exit" failure mode the backtest explicitly identified** (signals-learnings v5, 0-17% WR), and precisely why the entry-trigger guardrail says enter *"shortly after the open, once the opening range has printed."* 14:37 is not that. → **SKIP all three on entry-timing grounds** (guardrail-consistent, not over-caution).
  - Per-instrument DTE/expiry confirmed via `dhan.py lookup`: **NIFTY** nearest weekly **2026-07-14 (Tue), DTE 5** (sid 51373, lot 65) — clean, a valid open-entry candidate tomorrow. **SENSEX** nearest is **TODAY 2026-07-09 same-day expiry** (avoid — gamma at <1h to expiry), next **2026-07-16, DTE 7** (sid 826761, lot 20). **BANKNIFTY** nearest **2026-07-28 monthly, DTE 19** (sid 61873, lot 30; no weeklies) — *separately* fails DTE (far outside its ≤7-DTE near-expiry data-gathering window, same skip as 07-07).
  `2026-07-09 14:37 IST | NIFTY | 5 | SKIP (entry timing — last slot, ~38min to EOD) | Jul 14 exp, ADX 17.13<18 qualifies but no runway before forced same-day close | — | — | validated setup is an OPEN entry, not a 14:37 entry. No entry.`
  `2026-07-09 14:37 IST | SENSEX | 7 | SKIP (entry timing + same-day-expiry gamma) | Jul 16 exp (nearest is today's same-day exp, avoid), ADX 14.91<18 qualifies but no runway | — | — | No entry.`
  `2026-07-09 14:37 IST | BANKNIFTY | 19 | SKIP (DTE + entry timing) | Jul 28 monthly, ADX 16.38<18 qualifies but 19 DTE ≫ ≤7-DTE data window AND no runway | — | — | No entry.`
- **Stock fresh-setup check — unchanged; morning's qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks per protocol). This morning's 18 qualifiers are DTE-clear (Jul 30 expiry, 21 DTE) but the Jul 30 monthly collides with peak Q1 season — none affirmatively earnings-clear. No re-alert — steer still pending from Pushkar (flagged 07-07).
  `2026-07-09 14:37 IST | STOCKS (18 qualifiers) | 21 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram.
- **FORWARD NOTE for tomorrow's pre-market / open routine:** the indices have crossed into range-bound (ADX 17/16/15, VIX 13.15) — **if ADX holds <18 at Friday 07-10's open, NIFTY (Jul 14, DTE 4) and SENSEX (Jul 16, DTE 6) are genuine open-entry iron-condor candidates with full-session runway.** Today's only obstacle was that the qualifier appeared at the last intraday slot. First tradeable index regime in over a week — do NOT skip it at tomorrow's open if it persists. (BANKNIFTY still DTE-blocked at 19 DTE; SENSEX use Jul 16 not the same-day expiry.)
- **Nothing contradicted backtest expectations** — the range-bound regime finally arriving is the setup the strategy wants; today it just arrived too late in the session to act on within the intraday-only + open-entry-timing constraints. A scheduling/timing artifact, not a thesis break. Late-day-no-runway lesson already documented (v5) — no new signals-learnings entry needed.

---

## 2026-07-09 13:37 IST intraday-monitor — flat; NO index qualifier (ADX 20/19/19, closing on the 18 gate but not through, VIX 13.15); stock qualifiers still ALL earnings-blocked

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A. (Note: an EOD-labelled NO-OP entry was already written for 07-09 by an earlier-fired routine; this run is a genuine 13:37 IST intraday check, market still open, state unchanged — flat.)
- **Index fresh-setup check — no qualifier, all three still trending but ADX now near the gate:** fresh `market_data.py scan` (VIX **13.15**) — NIFTY spot 24,060.65 ADX **20.08**, BANKNIFTY spot 57,355.9 ADX **18.64**, SENSEX spot 77,044.06 ADX **18.95**. All `range_bound: false`, all still ≥18 gate → **no ADX qualifier**. ADX has kept easing off the pre-market highs (52.98/46.93/53.45 → … → now 20.08/18.64/18.95) as the 07-08 sell-off consolidates; BANKNIFTY (18.64) and SENSEX (18.95) are now hovering just above the 18 line — closest they've been all day — worth a re-check next run in case one settles below 18. Spot flat intraday (NIFTY ~24,060). BANKNIFTY still ≥18 → DTE moot.
  `2026-07-09 13:37 IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 20.08/18.64/18.95 all ≥18, VIX 13.15 | — | — | none range-bound; BANKNIFTY/SENSEX nearing the gate but not through. No entry.`
- **Stock fresh-setup check — unchanged; morning's qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks per protocol). This morning's 18 qualifiers (TECHM 9.49 … ADANIPORTS 16.86) are DTE-clear (Jul 30 expiry, 21 DTE) but the Jul 30 monthly collides with peak Q1 season — none affirmatively earnings-clear (ULTRACEMCO ~Jul 21, JSWSTEEL ~Jul 18 mid-hold; SBIN/MARUTI/EICHERMOT/ADANIPORTS ~Jul 31 <5d of expiry; HDFCLIFE/TECHM ~Jul 16 mid-hold). No re-alert — already Telegram-flagged 07-07, steer still pending from Pushkar.
  `2026-07-09 13:37 IST | STOCKS (18 qualifiers) | 21 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 18 but none earnings-clear. No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — indices trending (even as ADX approaches the gate) is the stand-aside regime; the stock earnings-season collision is a recurring calendar constraint, not a thesis break. No new signals-learnings entry needed.

---

## 2026-07-09 EOD square-off — NO-OP, flat all day: 0 open positions, 0 trades; day P&L ₹0

`2026-07-09 EOD IST | — | — | NO-OP (no strategy positions, no trades) | nothing to close/carry`
- **Positions to carry/close:** none — flat the entire session (came in flat from 07-02 EOD, opened nothing 07-08 or 07-09). No index condor to force-close, no stock condor to evaluate for carry-forward. Both paths (index force-close, stock carry-forward) N/A — nothing held. No spot-range candle check needed (no position to price).
- **No-trade day recap:** every 07-09 intraday run skipped. **Indices:** all three trended the whole session, ADX easing steadily off the pre-market highs (52.98/46.93/53.45 → 39/34/40 → 30/27/29 → 25/22/26 → final ~24.27/21.39/25.67) as the 07-08 risk-off sell-off's momentum faded, but all three stayed firmly ≥18 all day; spot essentially flat intraday (NIFTY ~24,025). VIX drifted 13.4→13.28. Firmly ≥18 gate all day → no index ADX qualifier. A multi-day directional move that's cooling but not yet range-bound is the trending regime this strategy stands aside from. BANKNIFTY trending too → DTE moot. **Stocks:** 18-19 F&O names cleared ADX<18 (daily) and the DTE gate (Jul 30 monthly, 21 DTE, within 2-30) but ALL SKIPPED on earnings grounds — the only in-range expiry (Jul 30) collides with peak Q1 season (opened 07-09 w/ TCS) and no name could be affirmatively earnings-cleared (ULTRACEMCO ~Jul 21, JSWSTEEL ~Jul 18 mid-hold; SBIN/MARUTI/EICHERMOT/ADANIPORTS ~Jul 31 <5d of expiry; HDFCLIFE/TECHM ~Jul 16 mid-hold). Open item still pending Pushkar's steer (flagged 07-07): enter names name-by-name after they report vs. hold through earnings per the DTE-2-30 backtest.
- **Circuit breaker:** DISABLED in paper mode (no daily loss cap). Day P&L ₹0 regardless.
- **Broker (best-effort):** flat — nothing to square off. `funds` shows the known locked artifact (utilizedAmount ₹934,698, availabelBalance ₹65,301) — the stale expired sid=71472 NIFTY artifact, not a strategy position, will lapse on its own, no escalation. No order placed.
- **Final state:** cash ₹4,00,000.00 (unchanged, post-2026-07-07 reset), realized P&L from reset ₹0.00, today's P&L ₹0. Flat into the close. EOD Telegram summary sent (always fires, even on a no-trade day).
- **Nothing contradicted backtest expectations** — a cooling-but-still-trending index tape (ADX ≥18 all day) is the stand-aside regime; the stock earnings-season collision is a recurring calendar constraint while Jul 30 is the only in-range expiry, not a thesis break. No new signals-learnings entry needed.

---

## 2026-07-09 intraday-monitor (latest run) — flat; NO index qualifier (all three still trending, ADX 24/21/26, VIX 13.29); 19 stock qualifiers still ALL earnings-blocked

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier, all three still trending:** fresh `market_data.py scan` (VIX **13.29**) — NIFTY spot 24,025.15 ADX **24.27**, BANKNIFTY spot 57,226.3 ADX **21.39**, SENSEX spot 77,064.09 ADX **25.67**. All `range_bound: false`, all ≥18 gate → **no ADX qualifier**. ADX keeps easing off the pre-market highs (52.98/46.93/53.45 → 25.30/21.76/25.67 → now 24.27/21.39/25.67) as the 07-08 sell-off's momentum fades, but all three remain firmly trending — none near the 18 gate. Spot essentially flat intraday (NIFTY ~24,025). BANKNIFTY trending too → DTE moot.
  `2026-07-09 latest2 IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 24.27/21.39/25.67 all ≥18, VIX 13.29 | — | — | none range-bound; still trending though ADX easing further. No entry.`
- **Stock fresh-setup check — unchanged; all 19 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks per protocol). This morning's 19 qualifiers (TECHM 10.15 … BEL 17.96) are DTE-clear (Jul 30 expiry, 21 DTE) but the Jul 30 monthly collides with peak Q1 season — none affirmatively earnings-clear (ULTRACEMCO ~Jul 21, JSWSTEEL ~Jul 18 mid-hold; SBIN/MARUTI/EICHERMOT/ADANIPORTS ~Jul 31 <5d of expiry; HDFCLIFE/TECHM ~Jul 16 mid-hold). No re-alert — already Telegram-flagged 07-07, steer still pending from Pushkar.
  `2026-07-09 latest2 IST | STOCKS (19 qualifiers) | 21 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 19 but none earnings-clear. No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — indices trending (even as ADX eases) is the stand-aside regime; the stock earnings-season collision is a recurring calendar constraint, not a thesis break. No new signals-learnings entry needed.

---

## 2026-07-09 intraday-monitor (prior run) — flat; NO index qualifier (all three still trending, ADX 25/22/26, VIX 13.2); 19 stock qualifiers still ALL earnings-blocked

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier, all three still trending:** fresh `market_data.py scan` (VIX **13.2**) — NIFTY spot 24,043.7 ADX **25.30**, BANKNIFTY spot 57,258.0 ADX **21.76**, SENSEX spot 77,036.41 ADX **25.67**. All `range_bound: false`, all ≥18 gate → **no ADX qualifier**. ADX keeps cooling off the pre-market highs (52.98/46.93/53.45 → 29.57/26.55/28.86 earlier → now 25.30/21.76/25.67) as the 07-08 sell-off's momentum fades, but all three remain firmly trending — none near the 18 gate. Spot essentially flat intraday (NIFTY ~24,044, holding the 24,022–24,052 band). BANKNIFTY trending too → DTE moot.
  `2026-07-09 latest IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 25.30/21.76/25.67 all ≥18, VIX 13.2 | — | — | none range-bound; still trending though ADX easing further. No entry.`
- **Stock fresh-setup check — unchanged; all 19 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks per protocol). This morning's 19 qualifiers (TECHM 10.15 … BEL 17.96) are DTE-clear (Jul 30 expiry, 21 DTE) but the Jul 30 monthly collides with peak Q1 season — none affirmatively earnings-clear (ULTRACEMCO ~Jul 21, JSWSTEEL ~Jul 18 mid-hold; SBIN/MARUTI/EICHERMOT/ADANIPORTS ~Jul 31 <5d of expiry; HDFCLIFE/TECHM ~Jul 16 mid-hold). No re-alert — already Telegram-flagged 07-07, steer still pending from Pushkar.
  `2026-07-09 latest IST | STOCKS (19 qualifiers) | 21 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 19 but none earnings-clear. No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — indices trending (even as ADX eases) is the stand-aside regime; the stock earnings-season collision is a recurring calendar constraint, not a thesis break. No new signals-learnings entry needed.

---

## 2026-07-09 intraday-monitor (later run) — flat; NO index qualifier (all three still trending, ADX 30/27/29, VIX 13.18); 19 stock qualifiers still ALL earnings-blocked

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier, all three still trending:** fresh `market_data.py scan` (VIX **13.18**) — NIFTY spot 24,051.85 ADX **29.57**, BANKNIFTY spot 57,328.7 ADX **26.55**, SENSEX spot 77,007.49 ADX **28.86**. All `range_bound: false`, all ≫18 gate → **no ADX qualifier**. ADX continues to cool off the pre-market highs (52.98/46.93/53.45 → now 29.57/26.55/28.86) as the 07-08 sell-off's momentum eases, but all three remain firmly trending. Spot essentially flat intraday (NIFTY 24,022→24,052). BANKNIFTY trending too → DTE moot.
  `2026-07-09 later IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 29.57/26.55/28.86 all ≥18, VIX 13.18 | — | — | none range-bound; still trending though ADX easing. No entry.`
- **Stock fresh-setup check — unchanged; all 19 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks per protocol). This morning's 19 qualifiers (TECHM 10.15 … BEL 17.96) are DTE-clear (Jul 30 expiry, 21 DTE) but the Jul 30 monthly collides with peak Q1 season — none affirmatively earnings-clear (ULTRACEMCO ~Jul 21, JSWSTEEL ~Jul 18 mid-hold; SBIN/MARUTI/EICHERMOT/ADANIPORTS ~Jul 31 <5d of expiry; HDFCLIFE/TECHM ~Jul 16 mid-hold). No re-alert — already Telegram-flagged 07-07, steer still pending from Pushkar.
  `2026-07-09 later IST | STOCKS (19 qualifiers) | 21 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 19 but none earnings-clear. No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — indices trending (even with ADX easing) is the stand-aside regime; the stock earnings-season collision is a recurring calendar constraint, not a thesis break. No new signals-learnings entry needed.

---

## 2026-07-09 intraday-monitor — flat; NO index qualifier (all three trending, ADX 39/34/40, VIX 13.4); 19 stock qualifiers ALL earnings-blocked (Jul 30 expiry in Q1 season)

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier, all three trending:** fresh `market_data.py scan` (VIX **13.4**, eased from 14.68 pre-market) — NIFTY spot 24,022.35 ADX **39.17**, BANKNIFTY spot 57,160.85 ADX **34.04**, SENSEX spot 77,055.58 ADX **39.61**. All ≫18 gate, all `range_bound: false` → **no ADX qualifier**. ADX cooled off the pre-market 52.98/46.93/53.45 highs but stays firmly trending as the 07-08 sell-off's directional move persists (spot little changed intraday: NIFTY 23,882→24,022). BANKNIFTY trending too → DTE moot.
  `2026-07-09 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 39.17/34.04/39.61 all ≥18, VIX 13.4 | — | — | none range-bound; still trending on the multi-day sell-off. No entry.`
- **Stock fresh-setup check — unchanged; all 19 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks per protocol). This morning's 19 qualifiers (TECHM 10.15 … BEL 17.96) are DTE-clear (Jul 30 expiry, 21 DTE, within 2-30) but the Jul 30 monthly collides with Q1 season (started today 07-09 w/ TCS) — none affirmatively earnings-clear (ULTRACEMCO ~Jul 21, JSWSTEEL ~Jul 18 mid-hold; SBIN/MARUTI/EICHERMOT/ADANIPORTS ~Jul 31 <5d of expiry; HDFCLIFE/TECHM ~Jul 16 mid-hold). No re-alert — already Telegram-flagged 07-07, steer still pending from Pushkar.
  `2026-07-09 intraday IST | STOCKS (19 qualifiers) | 21 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 19 but none earnings-clear. No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — a multi-day directional sell-off with ADX firmly ≥18 is the trending regime this range-bound strategy stands aside from; the stock earnings-season collision is a recurring calendar constraint while Jul 30 is the only in-range expiry, not a thesis break. No new signals-learnings entry needed.

---

## 2026-07-08 EOD square-off — NO-OP, flat all day: 0 open positions, 0 trades; day P&L ₹0

`2026-07-08 EOD IST | — | — | NO-OP (no strategy positions, no trades) | nothing to close/carry`
- **Positions to carry/close:** none — flat the entire session (came in flat from 07-02 EOD, opened nothing today). No index condor to force-close, no stock condor to evaluate for carry-forward. Both paths (index force-close, stock carry-forward) N/A — nothing held. No spot-range candle check needed (no position to price).
- **No-trade day recap:** every 07-08 intraday run skipped. **Indices:** all three trended the whole session and only harder into the close as spot sold off on a risk-off day — final reads NIFTY 23,860 ADX 50.14, BANKNIFTY 56,724 ADX 42.63, SENSEX 76,564 ADX 46.53 (spot −1.3-1.9%, VIX popped 12.24→15.1). Firmly ≥18 gate all day → no index ADX qualifier. A one-way directional sell-off is exactly the trending regime this range-bound strategy stands aside from; the VIX pop is the market pricing the move, not a setup. BANKNIFTY trending too → DTE moot. **Stocks:** 18 F&O names cleared ADX<18 (daily) and the DTE gate (Jul 30 monthly, 22 DTE, within 2-30) but ALL SKIPPED on earnings grounds — the only in-range expiry (Jul 30) collides with peak Q1 season and no name could be affirmatively earnings-cleared (ULTRACEMCO ~Jul 21, JSW ~Jul 18 mid-hold; SBIN/MARUTI/EICHERMOT/ADANIPORTS ~Jul 31 <5d of expiry). Open item still pending Pushkar's steer (flagged 07-07): enter names name-by-name after they report vs. hold through earnings per the DTE-2-30 backtest.
- **Circuit breaker:** DISABLED in paper mode (no daily loss cap). Day P&L ₹0 regardless.
- **Broker (best-effort):** flat — nothing to square off. `funds` shows the known locked artifact (utilizedAmount ₹934,698, availabelBalance ₹65,301); `orders` shows only the stale expired sid=71472 NIFTY-Jun2026-24000-CE (REJECTED, "Fund Limit Insufficient", drvExpiryDate 2026-06-25) — not a strategy position, will lapse on its own, no escalation. No order placed.
- **Final state:** cash ₹4,00,000.00 (unchanged, post-2026-07-07 reset), realized P&L from reset ₹0.00, today's P&L ₹0. Flat into the close. EOD Telegram summary sent (always fires, even on a no-trade day).
- **Nothing contradicted backtest expectations** — a risk-off directional day (spot down, ADX and VIX both up) is the trending regime the strategy correctly stands aside from; the stock earnings-season collision is a recurring calendar constraint while Jul 30 is the only in-range expiry, not a thesis break. No new signals-learnings entry needed.

---

## 2026-07-08 intraday-monitor (sell-off run) — flat; NO index qualifier (all three trending HARDER on a risk-off day, VIX spiked 12.24→15.1); stocks unchanged (all 18 earnings-blocked, daily ADX static intraday)

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier; risk-off, spot down + ADX up + VIX up:** fresh `market_data.py scan` (VIX **15.1**, up from 12.24 earlier today) — NIFTY spot 23,860.3 ADX **50.14**, BANKNIFTY spot 56,724.35 ADX **42.63**, SENSEX spot 76,564.21 ADX **46.53**. Spot sold off across the board (NIFTY 24,211.7→23,860.3 ≈ −1.5%, BANKNIFTY −1.9%, SENSEX −1.3%) and ADX rose sharply with the one-way down-move → all three now trending *harder* than the earlier 38.53/28.54/36.77. Firmly ≥18 gate → **no ADX qualifier**. A directional sell-off is exactly the trending regime this range-bound strategy stands aside from; the VIX pop is the market pricing the move, not a setup. BANKNIFTY trending too, DTE moot.
  `2026-07-08 sell-off IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 50.14/42.63/46.53 all ≥18, VIX 15.1 spike on risk-off | — | — | trending harder on a down-day; no range-bound entry. No entry.`
- **Stock fresh-setup check — unchanged; all 18 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks per protocol). This morning's 18 qualifiers are DTE-clear (Jul 30 expiry, 22 DTE) but the Jul 30 monthly collides with Q1 season — none affirmatively earnings-clear (established this morning: ULTRACEMCO ~Jul 21, JSW ~Jul 18 mid-hold; SBIN/MARUTI/EICHERMOT/ADANIPORTS ~Jul 31 <5d of expiry). No re-alert — already Telegram-flagged 07-07, steer still pending from Pushkar.
  `2026-07-08 sell-off IST | STOCKS (18 qualifiers) | 22 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 18 but none earnings-clear. No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — a risk-off directional day (spot down, ADX and VIX both up) is the trending regime the strategy correctly stands aside from. Worth noting the VIX pop off ~12 into 15 if it persists (a higher-vol backdrop is what credit spreads prefer, *once* ADX cools back below 18) — but no thesis break, no new signals-learnings entry needed.

---

## 2026-07-08 intraday-monitor (later run) — flat; NO index qualifier (all three still trending, VIX 12.24); stocks unchanged (all 18 earnings-blocked, daily ADX static intraday)

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier, all three still trending:** fresh `market_data.py scan` (VIX **12.24**) — NIFTY spot 24,211.7 ADX **38.53**, BANKNIFTY spot 57,827.2 ADX **28.54**, SENSEX spot 77,585.14 ADX **36.77**. All well above the 18 gate → **no ADX qualifier** (essentially unchanged from this morning's 38.98/32.37/36.07). BANKNIFTY trending too, DTE moot.
  `2026-07-08 later IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 38.53/28.54/36.77 all ≥18 | — | — | none range-bound; VIX 12.24 low but ADX is the binding gate. No entry.`
- **Stock fresh-setup check — unchanged; all 18 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks). This morning's 18 qualifiers are DTE-clear (Jul 30 expiry, 22 DTE, within 2-30) but the Jul 30 monthly collides with Q1 season — none affirmatively earnings-clear (established this morning; ULTRACEMCO ~Jul 21, JSW ~Jul 18 mid-hold; SBIN/MARUTI/EICHERMOT/ADANIPORTS ~Jul 31 <5d of expiry). No re-alert — already Telegram-flagged 07-07, steer still pending from Pushkar.
  `2026-07-08 later IST | STOCKS (18 qualifiers) | 22 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly | — | — | ADX<18 on all 18 but none earnings-clear. No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — indices trending in a low-VIX grind is the stand-aside regime; the stock earnings-season collision is a recurring calendar constraint, not a thesis break. No new signals-learnings entry needed.

## 2026-07-08 intraday-monitor — flat; NO index qualifier (all three trending, VIX 12.34); 18 stock qualifiers but ALL earnings-blocked (Jul 30 expiry in Q1 season). First run of 07-08 (no pre-market ran today)

**No pre-market entry exists for 07-08** — this run did the first scan of the day (daily ADX changes day-to-day, so 07-07's stock scan is stale; running scan-stocks now is the day's first read, not a prohibited mid-day re-run).
- **Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier, all three trending:** fresh `market_data.py scan` (VIX **12.34**) — NIFTY spot 24,195.95 ADX **38.98**, BANKNIFTY spot 57,762.4 ADX **32.37**, SENSEX spot 77,608.36 ADX **36.07**. All well above the 18 gate → **no ADX qualifier**. Spot pulled back a touch from 07-07 EOD (NIFTY 24,471→24,196) but ADX still firmly trending. BANKNIFTY trending too, DTE moot.
  `2026-07-08 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 38.98/32.37/36.07 all ≥18 | — | — | none range-bound; VIX 12.34 low but ADX is the binding gate. No entry.`
- **Stock fresh-setup check — 18 ADX qualifiers (fresh 07-08 scan), ALL SKIPPED on EARNINGS grounds (unchanged structural blocker from 07-07):** fresh `scan-stocks` lists 18 names ADX(14) daily <18 (TECHM 10.15, SBIN 10.97, ULTRACEMCO 12.37 … MARUTI 17.91; neither blocklisted name qualifies). Only in-range stock expiry is the July monthly **2026-07-30** (22 DTE, within 2-30), but entering now holds through Q1 (June-qtr) earnings season. A name is earnings-clean for a Jul 8→Jul 30 hold only if it reports before today (none — Q1 season starts Jul 9 w/ TCS) or >5 days after the Jul 30 expiry (after ~Aug 4). Fresh web check on the top uncovered candidates confirms the cluster: ULTRACEMCO ~Jul 21, JSW Steel ~Jul 18 (during hold); EICHERMOT ~Jul 31, ADANIPORTS ~Jul 31/Aug 1 (within 5d of expiry); HEROMOTOCO late Jul/early Aug (during hold or <5d of expiry). Plus 07-07's dates (SBIN/MARUTI ~Jul 31 <5d expiry, TECHM/HDFCLIFE ~Jul 16 mid-hold, RELIANCE/COALINDIA mid-late Jul). **Could not affirmatively earnings-clear a single one of the 18** → all skipped.
  `2026-07-08 intraday IST | STOCKS (18 qualifiers) | 22 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; no name reports cleanly (before today or after ~Aug 4) | — | — | ADX<18 on all 18 but none earnings-clear. No entry.`
  - **Open item still pending Pushkar (flagged since 07-07):** whether to enter names name-by-name *after they report* (earnings behind us, remaining DTE into Jul 30) OR hold through earnings per the DTE-2-30 Bhavcopy backtest (which included earnings gaps). No new action — awaiting his steer. Not re-Telegrammed (already flagged 07-07).
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — indices trending in a low-VIX grind is the stand-aside regime; the stock earnings-season collision is a calendar constraint (recurring while Jul 30 is the only in-range expiry), not a thesis break. No new signals-learnings entry needed.

---

## 2026-07-07 EOD square-off — NO-OP, flat all day: 0 open positions, 0 trades; day P&L ₹0

`2026-07-07 EOD IST | — | — | NO-OP (no strategy positions, no trades) | nothing to close/carry`
- **Positions to carry/close:** none — flat the entire session (came in flat, opened nothing today). No index condor to force-close, no stock condor to evaluate for carry-forward. Both the index force-close path and the stock carry-forward path are N/A — nothing held. No spot-range candle check needed (no position to price).
- **No-trade day recap:** every 07-07 intraday run skipped. **Indices:** NIFTY/SENSEX trended the whole session (ADX ran ~21→39 / ~24→42, well above the 18 gate; VIX very low ~11.5-11.8 but ADX is the binding gate). BANKNIFTY was the sole ADX qualifier late (dipped to 17.6 at 14:37, first sub-18 read) but SKIPPED — nearest expiry Jul 28 monthly = 21 DTE, far outside the ≤7-DTE near-expiry window that is its only data-gathering rationale. **Stocks:** 18 F&O names cleared ADX<18 and the DTE gate (Jul 30 expiry, 23 DTE, within 2-30) but ALL SKIPPED on earnings grounds — the only in-range expiry (Jul 30 monthly) collides with peak Q1 earnings season and no name could be affirmatively earnings-cleared (SBIN/MARUTI ~Jul 31 <5d of expiry; COALINDIA/TECHM/HDFCLIFE/RELIANCE report during the hold).
- **Circuit breaker:** DISABLED in paper mode (no daily loss cap). Day P&L ₹0 regardless.
- **Broker (best-effort):** flat — nothing to square off. No order placed.
- **Final state:** cash ₹4,00,000.00 (unchanged, post-2026-07-07 reset by Pushkar), realized P&L from reset ₹0.00, today's P&L ₹0. Flat into the close. EOD Telegram summary sent (always fires, even on a no-trade day).
- **Nothing contradicted backtest expectations** — a very-low-VIX day trending hard on all three indices is exactly the regime this range-bound strategy stands aside from; the stock earnings-season collision is a calendar constraint, not a thesis break. No new signals-learnings entry needed.

---

## 2026-07-07 intraday-monitor (~14:37 IST) — flat; BANKNIFTY now range-bound (ADX 17.6, first sub-18 read today) but SKIPPED (21 DTE, not near-expiry); NIFTY/SENSEX trending; stocks unchanged (all 18 earnings-blocked)

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — BANKNIFTY the sole ADX qualifier but SKIPPED on DTE grounds:** fresh `market_data.py scan` (VIX **11.51**) — NIFTY spot 24,471.85 ADX **21.11** (trending, no), **BANKNIFTY spot 58,357.05 ADX 17.60** (<18 → range_bound, the only qualifier), SENSEX spot 78,362.44 ADX **24.65** (trending, no). BANKNIFTY dipped below the 18 gate for the first time today (was 22.87 at 13:37) as spot chopped sideways; re-confirmed via `adx BANKNIFTY` → 17.6. Nearest expiry the July monthly **2026-07-28 = 21 DTE** (monthly-only, no weeklies; confirmed via `dhan.py lookup` → sid 61893, lot 30).
  `2026-07-07 14:37 IST | BANKNIFTY | 21 | SKIP (DTE far outside window) | July monthly 2026-07-28, step 100/lot 30, sid 61893 | — | — | ADX 17.60 qualifies but 21 DTE is not the ≤7-DTE near-expiry data point that is the entire rationale for trading unvalidated BANKNIFTY; far-dated IC held intraday captures negligible theta and drifts to EOD per signals-learnings. Intraday routine → would square off same day for ~zero decay. No entry.`
  `2026-07-07 14:37 IST | NIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 21.11/24.65 ≥18 | — | — | both trending, VIX 11.51 low but ADX is the binding gate. No entry.`
- **Stock fresh-setup check — unchanged from 13:37; all 18 qualifiers still SKIPPED on EARNINGS grounds:** daily ADX doesn't change intraday (didn't re-run scan-stocks). This morning's 18 qualifiers are DTE-clear (Jul 30 expiry, 23 DTE, within 2-30) but the Jul 30 monthly collides with Q1 earnings season — none affirmatively earnings-clear (SBIN/MARUTI ~Jul 31 <5d of expiry banned; COALINDIA/TECHM/HDFCLIFE/RELIANCE report during the hold). Established earlier this run's cycle; no re-alert.
  `2026-07-07 14:37 IST | STOCKS (18 qualifiers) | 23 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season | — | — | ADX<18 on all 18 but none earnings-clear. No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — BANKNIFTY finally clearing ADX only at 21 DTE is the recurring monthly-expiry mismatch (its data-gathering value lives at ≤7 DTE, which it won't reach until ~Jul 21+), not a thesis break; NIFTY/SENSEX grinding in low VIX is the stand-aside regime.

## 2026-07-07 intraday-monitor (~13:37 IST) — flat; NO index qualifier; STOCKS now DTE-unblocked but ALL 18 SKIPPED on EARNINGS (Jul 30 expiry collides with Q1 season); fixed dhan.py stock-lookup bug

**First run under the DTE 2-30 cap (commit c1b555d) — re-evaluated all stock qualifiers under the new cap.** Flat coming in (0 open paper positions), capital ₹4,00,000.
- **Positions to manage:** none — flat. Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier, all three trending:** fresh `market_data.py scan` (VIX **11.71**) — NIFTY spot 24,430.65 ADX **28.24**, BANKNIFTY spot 58,256.0 ADX **22.87**, SENSEX spot 78,289.82 ADX **31.13**. All ≥18 gate → **no ADX qualifier**. BANKNIFTY trending too, DTE moot.
  `2026-07-07 13:37 IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 28.24/22.87/31.13 all ≥18 | — | — | none range-bound; VIX 11.71 low but ADX is the binding gate. No entry.`
- **Stock fresh-setup check — 18 ADX qualifiers now clear the DTE gate (23 DTE, Jul 30, within 2-30) but ALL SKIPPED on EARNINGS grounds:** the only in-range stock expiry is the **July monthly 2026-07-30**; entering now (23 DTE) holds through Q1 earnings season (~Jul 16–Aug 8). Web-researched dates: **SBIN ~Jul 31, MARUTI Jul 31** → within 5 days of expiry (banned). **COALINDIA** window closed Jul 1 (imminent), **TECHM ~Jul 16, HDFCLIFE ~Jul 16, RELIANCE** mid-late July → held through earnings. **Could not affirmatively clear a single name** → earnings guardrail ("check NSE calendar before entering") blocks all 18.
  `2026-07-07 13:37 IST | STOCKS (18 qualifiers) | 23 | SKIP (earnings within/through hold) | Jul 30 expiry in peak Q1 season; SBIN/MARUTI ~Jul 31 <5d of expiry; COALINDIA/TECHM/HDFCLIFE/RELIANCE report during hold | — | — | ADX<18 on all 18 but none earnings-clear. No entry.`
  - **Structural finding (see signals-learnings 2026-07-07):** DTE 2-30 removed the DTE block, but the monthly-expiry-in-earnings-season collision now disqualifies the July universe. Refined rule: enter a name **only after it has reported** (earnings behind us), name-by-name later this month, OR wait for Pushkar's steer on holding through earnings. Telegram-flagged.
- **Tooling fix:** `dhan.py find_security_id` was OPTIDX-only → every stock lookup silently failed. Fixed to accept OPTSTK; verified (SBIN→sid 1143559/BSE/lot 750, RELIANCE→lot 500, NIFTY index unaffected). Committed this run.
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed.
- **Nothing contradicted backtest expectations** — indices trending in a low-VIX grind is the stand-aside regime; the stock earnings-collision is a calendar constraint, not a thesis break.

## 2026-07-07 intraday-monitor (~late afternoon) — flat; NO index qualifier (all three still trending, VIX 11.69); stocks still all DTE-blocked

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules to act on. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier, all three still trending:** fresh `market_data.py scan` (VIX **11.69**) — NIFTY spot 24,461.35 ADX **30.51**, BANKNIFTY spot 58,327.0 ADX **22.85**, SENSEX spot 78,405.94 ADX **38.34**. All well above the 18 gate → **no ADX qualifier**. BANKNIFTY trending too, DTE moot.
  `2026-07-07 late-afternoon IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 30.51/22.85/38.34 all ≥18 | — | — | none range-bound; VIX 11.69 low but ADX is the binding gate. No entry.`
- **Stock fresh-setup check — same 18 qualifiers, ALL still SKIPPED on DTE grounds (unchanged; daily ADX doesn't change intraday, didn't re-run scan-stocks):** every single-stock option is monthly-only — nearest expiry **2026-07-30 (23 DTE)** ≫ the DTE 2-7 cap (reference: signals-learnings 2026-07-07). Enterable only in the ~week before monthly expiry (≈ Jul 23–28) absent a Pushkar decision to relax the cap. No re-alert — established reference.
  `2026-07-07 late-afternoon IST | STOCKS (18 qualifiers) | 23 | SKIP (DTE far outside window) | nearest stock expiry 2026-07-30 monthly, no weeklies | — | — | ADX<18 on all 18 but 23 DTE ≫ 7-DTE hard cap. No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — indices grinding in a very-low-VIX regime is exactly the regime this range-bound strategy stands aside from.

## 2026-07-07 intraday-monitor (~afternoon) — flat; NO index qualifier (all three still trending, VIX 11.68); stocks still all DTE-blocked

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules to act on. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier, all three still trending:** fresh `market_data.py scan` (VIX **11.68**) — NIFTY spot 24,472.35 ADX **34.15**, BANKNIFTY spot 58,329.9 ADX **24.36**, SENSEX spot 78,553.19 ADX **42.06**. All well above the 18 gate (NIFTY/BANKNIFTY eased a touch off the midday 39.06/29.06 but nowhere near range-bound; SENSEX firmly trending at 42) → **no ADX qualifier**. BANKNIFTY trending too, DTE moot.
  `2026-07-07 afternoon IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 34.15/24.36/42.06 all ≥18 | — | — | none range-bound; VIX 11.68 low but ADX is the binding gate. No entry.`
- **Stock fresh-setup check — same 18 qualifiers, ALL still SKIPPED on DTE grounds (unchanged; daily ADX doesn't change intraday, didn't re-run scan-stocks):** every single-stock option is monthly-only — nearest expiry **2026-07-30 (23 DTE)** ≫ the DTE 2-7 cap (reference: signals-learnings 2026-07-07). Enterable only in the ~week before monthly expiry (≈ Jul 23–28) absent a Pushkar decision to relax the cap. No re-alert — established reference.
  `2026-07-07 afternoon IST | STOCKS (18 qualifiers) | 23 | SKIP (DTE far outside window) | nearest stock expiry 2026-07-30 monthly, no weeklies | — | — | ADX<18 on all 18 but 23 DTE ≫ 7-DTE hard cap. No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — indices grinding in a very-low-VIX regime is exactly the regime this range-bound strategy stands aside from.

## 2026-07-07 intraday-monitor (midday) — flat; NO index qualifier (all three trending harder still, VIX 11.78); stocks still all DTE-blocked

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules to act on. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier; all three trending harder than the 10:36 run:** fresh `market_data.py scan` (VIX **11.78**) — NIFTY spot 24,515.85 ADX **39.06**, BANKNIFTY spot 58,427.1 ADX **29.06**, SENSEX spot 78,569.68 ADX **39.17**. All well above the 18 gate (NIFTY/SENSEX ticked up again from 37.57/36.95 at 10:36 as the grind-up continued) → **no ADX qualifier**. BANKNIFTY trending too, DTE moot.
  `2026-07-07 midday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 39.06/29.06/39.17 all ≥18 | — | — | none range-bound; VIX 11.78 low but ADX is the binding gate. No entry.`
- **Stock fresh-setup check — same 18 qualifiers, ALL still SKIPPED on DTE grounds (unchanged; daily ADX doesn't change intraday, didn't re-run scan-stocks):** every single-stock option is monthly-only — nearest expiry **2026-07-30 (23 DTE)** ≫ the DTE 2-7 cap (reference: signals-learnings 2026-07-07). Enterable only in the ~week before monthly expiry (≈ Jul 23–28) absent a Pushkar decision to relax the cap. No re-alert — this is the established reference.
  `2026-07-07 midday IST | STOCKS (18 qualifiers) | 23 | SKIP (DTE far outside window) | nearest stock expiry 2026-07-30 monthly, no weeklies | — | — | ADX<18 on all 18 but 23 DTE ≫ 7-DTE hard cap. No entry.`
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — indices grinding up in a very-low-VIX regime is exactly the regime this range-bound strategy stands aside from.

## 2026-07-07 intraday-monitor (~10:36 IST) — flat; NO index qualifier (all three trending harder, VIX 11.76); stocks still all DTE-blocked

**Positions to manage:** none — flat (0 open paper positions). Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules to act on. Circuit breaker DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier, all three trending, harder than the 09:37 run:** fresh `market_data.py scan` (VIX **11.76**) — NIFTY spot 24,491.75 ADX **37.57**, BANKNIFTY spot 58,400.4 ADX **31.19**, SENSEX spot 78,530.52 ADX **36.95**. All well above the 18 gate (NIFTY/SENSEX ticked up from 32.79/32.92 at 09:37 as spot kept grinding up) → **no ADX qualifier**. BANKNIFTY trending too, DTE question moot.
  `2026-07-07 10:36 IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 37.57/31.19/36.95 all ≥18 | — | — | none range-bound; VIX 11.76 low but ADX is the binding gate. No entry.`
- **Stock fresh-setup check — same 18 qualifiers, ALL still SKIPPED on DTE grounds (unchanged from 09:37):** daily ADX doesn't change intraday (don't re-run scan-stocks mid-day), so this morning's 18 qualifiers stand. The 09:37 run already confirmed via the Dhan instrument master that every single-stock option is **monthly-only** — nearest expiry **2026-07-30 (23 DTE)**, then 2026-08-27 — far outside the hard **DTE 2-7** cap, and a 23-DTE condor captures almost no theta (wouldn't reproduce the backtest near-expiry edge). Nothing about the expiry calendar changes within a day → every qualifier still fails the DTE gate.
  `2026-07-07 10:36 IST | STOCKS (18 qualifiers) | 23 | SKIP (DTE far outside window) | nearest stock expiry 2026-07-30 monthly, no weeklies | — | — | ADX<18 on all 18 but 23 DTE ≫ 7-DTE hard cap. No entry.`
  - **Open item still pending Pushkar (flagged 09:37):** stocks are only enterable in the ~week before monthly expiry under DTE 2-7 (this cycle ≈ Jul 23–28) unless the stock DTE cap is explicitly relaxed. No new action this run — awaiting his decision.
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — indices grinding up in a low-VIX regime is exactly what this range-bound strategy stands aside from.

## 2026-07-07 intraday-monitor (~09:37 IST, market open) — flat; NO index qualifier; STOCKS UNLOCKED but ALL 18 skipped (monthly-only, 23 DTE ≫ 7-DTE cap)

**First market-hours run since stocks were unlocked (strategy.md commit 42d8033).** Flat coming in (0 open paper positions), capital ₹4,00,000 post-reset.

- **Positions to manage:** none — flat. Nothing for the 50%/2× (index) or 25%/2.5× (stock) exit rules to act on.
- **Circuit breaker:** DISABLED in paper mode — N/A.
- **Index fresh-setup check — no qualifier, all three trending:** fresh `market_data.py scan` (VIX **11.83**) — NIFTY spot 24,456.95 ADX **32.79**, BANKNIFTY spot 58,469.25 ADX **31.16**, SENSEX spot 78,385.54 ADX **32.92**. All well above the 18 gate → **no ADX qualifier**. BANKNIFTY trending too, DTE question moot.
  `2026-07-07 09:37 IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 32.79/31.16/32.92 all ≥18 | — | — | none range-bound; VIX 11.83 low but ADX is the binding gate. No entry.`
- **Stock fresh-setup check — 18 ADX qualifiers, but ALL SKIPPED on DTE grounds (binding structural blocker):** this morning's scan lists 18 F&O names ADX(14) daily <18 (TECHM 10.96 … HINDUNILVR 17.62; neither blocklisted name qualifies). Checked the Dhan instrument master for available option expiries across the qualifiers (SBIN, TITAN, RELIANCE, ITC, MARUTI, TECHM, HINDUNILVR, ULTRACEMCO, POWERGRID, COALINDIA, BPCL, HDFCLIFE, SBILIFE, HEROMOTOCO, EICHERMOT, PNB, CANBK, BANKBARODA): **every one is monthly-only** — nearest option expiry **2026-07-30 (23 DTE)**, then 2026-08-27, 2026-09-24. **No weekly stock options exist** (only indices carry weeklies; SEBI phased out stock weeklies). 23 DTE is far outside the hard **DTE 2-7** guardrail ("don't go longer") → every qualifier fails the DTE gate. Also substantively: a 23-DTE condor held a few days captures almost no theta (cf. signals-learnings long-dated-BANKNIFTY "drifts to EOD as noise"), so it would NOT reproduce the backtest's near-expiry edge even if the literal cap were waived.
  `2026-07-07 09:37 IST | STOCKS (18 qualifiers) | 23 | SKIP (DTE far outside window) | nearest stock expiry 2026-07-30 monthly, no weeklies | — | — | ADX<18 on all 18 but 23 DTE ≫ 7-DTE hard cap; entering now wouldn't replicate backtest near-expiry theta. No entry.`
  - **Structural finding (see signals-learnings 2026-07-07):** strategy.md's stock section assumes "stocks have weekly + monthly expiry" — **factually wrong**; Indian single-stock options are monthly-only. Under DTE 2-7, stock condors are only enterable in the ~week before monthly expiry (this cycle ≈ **Jul 23–28**), held into the Jul 30 expiry — a late-month trade, not an any-day trade. Needs a Pushkar decision: either (a) accept stocks trade only near monthly expiry (natural fit with the "held 2-7 days into expiry" backtest), or (b) explicitly relax the stock DTE cap to allow monthly-at-entry (like the BANKNIFTY data-gathering carve-out — but signals-learnings shows long-dated condors are mostly EOD-drift noise). Flagged via Telegram.
- **Broker:** no action (flat, nothing to place/manage). No trade placed or closed.
- **Nothing contradicted backtest expectations** — indices trending in a low-VIX grind is the regime this strategy stands aside from; the stock finding is a strategy-spec gap, not a thesis break.

## 2026-07-06 EOD square-off — NO-OP, flat all day: 0 open positions, 0 trades; day P&L ₹0

`2026-07-06 EOD IST | — | — | NO-OP (no strategy positions, no trades) | nothing to close`
- **Positions to carry/close:** none — flat the entire session (0 open paper positions in portfolio.md; came in flat, opened nothing today). No index condor to force-close, no stock condor to evaluate for carry-forward. Both the index force-close path and the stock carry-forward path are N/A — nothing held.
- **No-trade day:** every 07-06 intraday run skipped — all three indices trended the whole session (ADX ~19→34, well above the 18 gate; VIX very low ~11.8-11.9 but ADX is the binding gate) so no index qualifier; stocks were UNLOCKED late (strategy.md commit 42d8033, ~21:37 IST) but only after market close, so no stock condor could be opened intraday. 18 F&O names qualified in this morning's scan → carried to the next market-hours run.
- **Circuit breaker:** DISABLED in paper mode (no daily loss cap). Day P&L ₹0 regardless.
- **Broker (best-effort):** after-hours — `funds` → FUND_LIMIT_ERROR 500, `orders` → DH-906. Known sandbox + after-hours read-endpoint failure (order-read endpoints error outside market hours), not a new problem. Portfolio.md is authoritative → flat.
- **Final state:** cash ₹50,000.00 (unchanged, post-reset), realized P&L from reset ₹0.00, today's P&L ₹0. Flat into the close. EOD Telegram summary sent (always fires, even on a no-trade day).
- **Nothing contradicted backtest expectations** — a very-low-VIX day trending hard on all three indices is exactly the regime this range-bound strategy stands aside from; no signals-learnings entry needed.

## 2026-07-06 intraday-monitor (~21:38 IST, AFTER MARKET CLOSE) — flat, nothing to manage; NO index qualifier; stocks now UNLOCKED but market closed → no entry

**Timing/label note:** wall clock reads **2026-07-06 21:38 IST — market is closed** (NSE 09:15–15:30 IST). Scan returns EOD-close data (NIFTY 24,430.35 / BANKNIFTY 58,291.5 / SENSEX 78,285.07, VIX 11.82) — identical to the reads logged below under "07-07" labels, which were this same 07-06 EOD snapshot mislabeled a day forward by prior runs. No live market → no executable entry this run.

**Positions to manage:** none — flat (0 open paper positions in portfolio.md). Nothing for the 50%/2× exit rules to act on.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → tripped=False; day P&L ₹0).
- **Index fresh-setup check — no qualifier, all three trending:** VIX **11.82** (very low) — NIFTY spot 24,430.35 ADX **30.61**, BANKNIFTY spot 58,291.5 ADX **27.55**, SENSEX spot 78,285.07 ADX **30.34**. All well above the 18 gate → **no ADX qualifier**. BANKNIFTY trending too, so its DTE-skip question is moot.
  `2026-07-06 21:38 IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup + market closed) | ADX 30.61/27.55/30.34 all ≥18 | — | — | none range-bound; VIX 11.82 low but ADX is the binding gate. No entry.`
- **Stock fresh-setup check — stocks NOW UNLOCKED, but no entry (market closed):** the just-landed strategy.md commit **42d8033 "Unlock stock options for paper trading" (2026-07-06 21:37 IST)** approves Nifty-50 F&O stock iron condors in paper mode — this **supersedes the "gated" reasoning in the earlier 07-07 entries below** (they predate the unlock). This morning's scan (research-log) lists **18 qualifiers** (ADX(14) daily <18: TECHM 10.96, SBIN 11.62, PNB 11.87 … HINDUNILVR 17.62; neither blocklisted name qualifies). **No stock entry this run:** market is closed (21:38 IST) — an intraday condor cannot be opened after close and squared off "today," which violates the intraday mandate. **Action for the next market-hours run:** evaluate these qualifiers live per strategy.md — fresh ADX at the open, per-name earnings check (none of the 18 report Jul 6-10, but re-confirm TECHM given 34% hist-vol), DTE 2-7, short-leg OI>1,000, `hist_vol_pct` (not VIX) for premium, strike step + lot size via `dhan.py lookup`.
- **Broker:** no action (flat, no orders to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — a very-low-VIX day trending hard on all three indices is exactly the regime this range-bound strategy stands aside from. No new signals-learnings entry needed.

## 2026-07-07 intraday-monitor — flat, nothing to manage; NO ADX qualifier (all three trending, VIX 11.82); stocks gated

**Positions to manage:** none — flat (0 open paper positions in portfolio.md; came in flat, opened nothing 07-03/07-06). Nothing for the 50%/2× exit rules to act on.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → tripped=False; day P&L ₹0).
- **Index fresh-setup check — no qualifier, all three trending:** Scan (VIX **11.82**, very low) — NIFTY spot 24,430.35 ADX **30.61** (trending, no), BANKNIFTY spot 58,291.5 ADX **27.55** (trending, no), SENSEX spot 78,285.07 ADX **30.34** (trending, no). All three well above the 18 gate → **no ADX qualifier**. Data identical to today's 07-07 pre-market read (no new bar printed — market closed / no fresh intraday data). BANKNIFTY is trending too (27.55), so its usual DTE-skip question is moot — nothing clears ADX.
  `2026-07-07 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 30.61/27.55/30.34 all ≥18 | — | — | none range-bound; VIX 11.82 low but ADX is the binding gate. No entry.`
- **Stock fresh-setup check — GATED, no entry:** today's 07-07 pre-market logged 18 F&O names ADX<18 (TECHM 10.96, SBIN 11.62, PNB 11.87, … none blocklisted). Per strategy.md hard guardrail ("No individual stock options until this file says otherwise"), stock options remain **gated pending a real index paper track record** — the qualifiers are situational awareness only, not an authorization. **No stock entry.**
- **Broker:** no action (flat, no orders to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — a very-low-VIX day (11.82) that trends hard on all three (ADX≥18) is exactly the regime this range-bound credit-spread strategy stands aside from; low VIX does not imply low ADX. No new signals-learnings entry needed.

## 2026-07-06 EOD square-off (~15:15 IST) — NO-OP, flat all day: 0 open positions, 0 trades; day P&L ₹0

`2026-07-06 EOD IST | — | — | NO-OP (no strategy positions, no trades) | nothing to close`
- **Positions to carry/close:** none — flat the entire session (came in flat from 07-02 EOD, opened nothing today). Carry-forward 3-condition test N/A; nothing held.
- **No-trade day:** every 07-06 intraday run skipped. All three instruments trended the whole session and only harder as spot drifted up (ADX rose through ~19→34: NIFTY 26.66→32.76, BANKNIFTY 19.10→33.97, SENSEX 28.67→34.48; VIX extremely low ~11.8-11.9 but ADX is the binding gate). No ADX<18 qualifier at any point — even BANKNIFTY (its usual DTE-skip is moot when it doesn't clear ADX) climbed well above 18 by mid-session.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → False; day P&L ₹0).
- **Broker (best-effort):** `square-off-all` only saw the expired sid=71472 artifact → SELL 72260706102081 **REJECTED** ("Fund Limit Insufficient", expired 2026-06-25), confirmed via `order-status`. Same known clean terminal rejection — not a stuck order, not a strategy position; will lapse on its own, no escalation. `funds`/`orders` unchanged (utilizedAmount ₹934,698 still locked by the artifact; only TRADED orders are the two artifact BUYs).
- **Final state:** cash ₹99,400.00 (unchanged), all-time realized P&L −₹600.00, today's P&L ₹0. Flat into the close. EOD Telegram summary sent (always fires, even on a no-trade day).
- **Nothing contradicted backtest expectations** — a very-low-VIX day that nonetheless trends hard on all three (ADX>18 across the board) is exactly the regime this range-bound credit-spread strategy correctly stands aside from; low VIX does not imply low ADX. No new signals-learnings entry needed.

## 2026-07-06 intraday-monitor (~late-session IST) — flat, nothing to manage; NO ADX qualifier (all three still trending hard, VIX 11.86)

**Positions to manage:** none — flat (0 open paper positions in portfolio.md; came in flat from 07-02 EOD, opened nothing 07-03/07-06). Nothing for the 50%/2× exit rules to act on.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → tripped=False; day P&L ₹0).
- **Fresh-setup check — no qualifier, all three trending:** Scan (VIX **11.86**, very low) — NIFTY spot 24,413.95 ADX **32.76** (trending, no), BANKNIFTY 58,326.25 ADX **33.97** (trending, no), SENSEX 78,223.94 ADX **34.48** (trending, no). All three well above the 18 gate, essentially flat vs the prior run (40.30/38.58/40.40) → **no ADX qualifier**. BANKNIFTY is firmly trending too, so the usual DTE-skip question is moot — nothing clears ADX.
  `2026-07-06 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 32.76/33.97/34.48 all ≥18 | — | — | none range-bound; VIX 11.86 low but ADX is the binding gate. No entry.`
- **Broker:** no action (flat, no orders to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — a very-low-VIX day (11.86) that keeps trending hard on all three (ADX≥18) is exactly the regime this range-bound credit-spread strategy stands aside from; low VIX does not imply low ADX. No new signals-learnings entry needed.

## 2026-07-06 intraday-monitor (~latest intraday IST) — flat, nothing to manage; NO ADX qualifier (all three still trending hard, VIX 11.91)

**Positions to manage:** none — flat (0 open paper positions in portfolio.md; came in flat from 07-02 EOD, opened nothing 07-03/07-06). Nothing for the 50%/2× exit rules to act on.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → tripped=False; day P&L ₹0).
- **Fresh-setup check — no qualifier, all three trending:** Scan (VIX **11.91**, very low) — NIFTY spot 24,446.7 ADX **40.3** (trending, no), BANKNIFTY 58,430.3 ADX **38.58** (trending, no), SENSEX 78,345.63 ADX **40.4** (trending, no). All three well above the 18 gate, essentially flat vs the prior run (39.52/38.98/38.54) → **no ADX qualifier**. BANKNIFTY is firmly trending too, so the usual DTE-skip question is moot — nothing clears ADX.
  `2026-07-06 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 40.30/38.58/40.40 all ≥18 | — | — | none range-bound; VIX 11.91 low but ADX is the binding gate. No entry.`
- **Broker:** no action (flat, no orders to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — a very-low-VIX day (11.91) that keeps trending hard on all three (ADX≥18) is exactly the regime this range-bound credit-spread strategy stands aside from; low VIX does not imply low ADX. No new signals-learnings entry needed.

## 2026-07-06 intraday-monitor (~latest intraday IST) — flat, nothing to manage; NO ADX qualifier (all three trending harder still, VIX 11.93)

**Positions to manage:** none — flat (0 open paper positions in portfolio.md; came in flat from 07-02 EOD, opened nothing 07-03/07-06). Nothing for the 50%/2× exit rules to act on.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → tripped=False; day P&L ₹0).
- **Fresh-setup check — no qualifier, all three trending even harder:** Scan (VIX **11.93**, very low) — NIFTY spot 24,452.65 ADX **39.52** (trending, no), BANKNIFTY 58,447.95 ADX **38.98** (trending, no), SENSEX 78,328.9 ADX **38.54** (trending, no). All three well above the 18 gate and higher than the prior run (was 35.12/33.83/35.69) → **no ADX qualifier**. BANKNIFTY is firmly trending too, so the usual DTE-skip question is moot — nothing clears ADX.
  `2026-07-06 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 39.52/38.98/38.54 all ≥18 | — | — | none range-bound; VIX 11.93 low but ADX is the binding gate. No entry.`
- **Broker:** no action (flat, no orders to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — a very-low-VIX day (11.93) that trends ever harder on all three (ADX≥18, still rising through the session) is exactly the regime this range-bound credit-spread strategy stands aside from; low VIX does not imply low ADX. No new signals-learnings entry needed.

## 2026-07-06 intraday-monitor (~latest intraday IST) — flat, nothing to manage; NO ADX qualifier (all three trending even harder, VIX 11.89)

**Positions to manage:** none — flat (0 open paper positions in portfolio.md; came in flat from 07-02 EOD, opened nothing 07-03/07-06). Nothing for the 50%/2× exit rules to act on.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → tripped=False; day P&L ₹0).
- **Fresh-setup check — no qualifier, all three trending harder:** Scan (VIX **11.89**, very low) — NIFTY spot 24,413.5 ADX **35.12** (trending, no), BANKNIFTY 58,288.65 ADX **33.83** (trending, no), SENSEX 78,230.92 ADX **35.69** (trending, no). All three well above the 18 gate and higher than the prior run (was 31.55/27.98/31.90) → **no ADX qualifier**. BANKNIFTY is firmly trending too, so the usual DTE-skip question is moot — nothing clears ADX.
  `2026-07-06 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 35.12/33.83/35.69 all ≥18 | — | — | none range-bound; VIX 11.89 low but ADX is the binding gate. No entry.`
- **Broker:** no action (flat, no orders to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — a very-low-VIX day (11.89) that trends on all three (ADX≥18, rising through the session) is exactly the regime this range-bound credit-spread strategy stands aside from; low VIX does not imply low ADX. No new signals-learnings entry needed.

## 2026-07-06 intraday-monitor (~later intraday IST) — flat, nothing to manage; NO ADX qualifier (all three trending harder, VIX 11.83)

**Positions to manage:** none — flat (0 open paper positions in portfolio.md; came in flat from 07-02 EOD, opened nothing 07-03/07-06). Nothing for the 50%/2× exit rules to act on.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → tripped=False; day P&L ₹0).
- **Fresh-setup check — no qualifier, all three trending:** Scan (VIX **11.83**, very low) — NIFTY spot 24,396.8 ADX **31.55** (trending, no), BANKNIFTY 58,267.4 ADX **27.98** (trending, no), SENSEX 78,178.28 ADX **31.9** (trending, no). All three well above the 18 gate → **no ADX qualifier**. BANKNIFTY has now firmly left the range-bound zone too (12.75 pre-market → 19.10 earlier run → 27.98 now, as spot drifted up), so the usual DTE-skip question is moot — nothing even clears ADX.
  `2026-07-06 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 31.55/27.98/31.90 all ≥18 | — | — | none range-bound; VIX 11.83 low but ADX is the binding gate. No entry.`
- **Broker:** no action (flat, no orders to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — a very-low-VIX day (11.83) that trends on all three (ADX≥18) is exactly the regime this range-bound credit-spread strategy stands aside from; low VIX does not imply low ADX. No new signals-learnings entry needed.

## 2026-07-06 intraday-monitor (~intraday IST) — flat, nothing to manage; NO ADX qualifier (all three trending, BANKNIFTY now also >18)

**Positions to manage:** none — flat (0 open paper positions in portfolio.md; came in flat from 07-02 EOD, opened nothing 07-03). Nothing for the 50%/2× exit rules to act on.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → tripped=False; day P&L ₹0).
- **Fresh-setup check — no qualifier at all this run:** Scan (VIX **11.94**, very low) — NIFTY spot 24,375.85 ADX **26.66** (trending, no), BANKNIFTY 58,204.0 ADX **19.10** (above the 18 gate, no), SENSEX 78,044.98 ADX **28.67** (trending, no). All three above the gate → **no ADX qualifier**. Note BANKNIFTY has risen through the gate since the pre-market read (12.75 → 19.10) as spot drifted up ~266 pts, so today's usual DTE-skip question is moot — it doesn't even clear ADX now.
  `2026-07-06 intraday IST | NIFTY/BANKNIFTY/SENSEX | — | SKIP (no qualifying setup) | ADX 26.66/19.10/28.67 all ≥18 | — | — | none range-bound; VIX 11.94 low but ADX is the binding gate. No entry.`
- **Broker:** no action (flat, no orders to place/manage). No trade placed or closed → no Telegram.
- **Nothing contradicted backtest expectations** — another very-low-VIX day (11.94) that is nonetheless trending on all three (ADX≥18) is exactly the regime this range-bound credit-spread strategy stands aside from; low VIX does not imply low ADX. No new signals-learnings entry needed.

## 2026-07-03 EOD square-off (~15:15 IST) — NO-OP, flat all day: 0 open positions, 0 trades; day P&L ₹0

`2026-07-03 EOD IST | — | — | NO-OP (no strategy positions, no trades) | nothing to close`
- **Positions to carry/close:** none — flat the entire session (came in flat from 07-02 EOD, opened nothing today). Carry-forward 3-condition test N/A; nothing held.
- **No-trade day:** every 07-03 intraday run skipped. NIFTY/SENSEX trended the whole session and only harder as spot drifted up (ADX ~26→44 NIFTY, ~32→49 SENSEX; VIX extremely low ~11.9 but ADX is the binding gate). BANKNIFTY was the only ADX qualifier all day (reads 13-17, mostly <18) but SKIPPED every run on DTE grounds — nearest expiry 2026-07-28 = ~25 DTE monthly, far outside the validated DTE 1-6 window and useless for its sole ≤7-DTE near-expiry data-gathering rationale.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → False; day P&L ₹0).
- **Broker (best-effort):** `square-off-all` only saw the expired sid=71472 artifact → SELL 72260703102081 **REJECTED**, confirmed via `order-status`. Same known 2026-06-25-expired sandbox artifact — clean terminal rejection, not a stuck order, not a strategy position; will lapse on its own, no escalation.
- **Final state:** cash ₹99,400.00 (unchanged), all-time realized P&L −₹600.00, today's P&L ₹0. Flat into the close. EOD Telegram summary sent (always fires, even on a no-trade day).
- **Nothing contradicted backtest expectations** — a low-VIX day that nonetheless trended (ADX>18 on both validated instruments) is exactly the regime this range-bound credit-spread strategy correctly stands aside from; low VIX does not imply low ADX. No new signals-learnings entry needed.

## 2026-07-03 intraday-monitor (~latest intraday IST) — flat, nothing to manage; BANKNIFTY still the only ADX qualifier but SKIPPED (25 DTE, not near-expiry)

**Positions to manage:** none — flat (0 open paper positions in portfolio.md). Nothing for the 50%/2× exit rules to act on.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → tripped=False; day P&L ₹0).
- **Fresh-setup check — BANKNIFTY the only ADX qualifier but SKIPPED on DTE grounds:** Scan (VIX **11.93**, very low) — NIFTY spot 24,283.1 ADX **26.49** (trending, no), **BANKNIFTY 57,941.8 ADX 13.73** (<18, no open position → the only qualifier), SENSEX 77,795.88 ADX **32.47** (clearly trending, no). NIFTY/SENSEX remain firmly trending.
  `2026-07-03 intraday IST | BANKNIFTY | 25 | SKIP (DTE far outside window) | July monthly expiry 2026-07-28 (step 100/lot 30), sid confirmed earlier today | — | — | ADX 13.73 qualifies but 25 DTE is not the ≤7-DTE near-expiry data point that is the entire rationale for trading unvalidated BANKNIFTY; far-dated ICs just drift to EOD per signals-learnings, no learning value. No entry.`
- **Broker:** no action (flat, no orders to place/manage). No trade placed or closed → no Telegram.
- **Git note (checked, no real problem — noting so next run doesn't re-alarm):** the *local* `origin/main` tracking ref was stale at `f83488a` (~06-30), which briefly looked like main had been orphaned. It hadn't: `git push` reported remote `main`'s actual prior tip as `60d1974` — i.e. remote `main` already contained all of 07-01/02/03 work; prior runs *were* landing on main correctly. This run's commit pushed cleanly on top; verified `origin/main == HEAD == 07ff221` after a fresh fetch. No orphaning occurred; nothing to fix.

## 2026-07-03 intraday-monitor (later ~intraday IST) — flat, nothing to manage; BANKNIFTY still the only ADX qualifier but SKIPPED (25 DTE, not near-expiry)

**Positions to manage:** none — flat (0 open paper positions in portfolio.md). Nothing for the 50%/2× exit rules to act on.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → tripped=False; day P&L ₹0).
- **Fresh-setup check — BANKNIFTY the only ADX qualifier but SKIPPED on DTE grounds:** Scan (VIX **11.92**, very low) — NIFTY spot 24,280.75 ADX **34.46** (trending, no), **BANKNIFTY 57,830.55 ADX 13.76** (<18, no open position → the only qualifier), SENSEX 77,915.06 ADX **44.29** (clearly trending, no). NIFTY/SENSEX remain firmly trending.
  `2026-07-03 intraday IST | BANKNIFTY | ~25 | SKIP (DTE far outside window) | July monthly expiry, step 100/lot 30 | — | — | ADX 13.76 qualifies but ~25 DTE is not the ≤7-DTE near-expiry data point that is the entire rationale for trading unvalidated BANKNIFTY; far-dated ICs just drift to EOD per signals-learnings, no learning value. No entry.`

## 2026-07-03 intraday-monitor (~late-session IST) — flat, nothing to manage; BANKNIFTY again the only ADX qualifier but SKIPPED (25 DTE, not near-expiry)

**Positions to manage:** none — flat (0 open paper positions in portfolio.md). Nothing for the 50%/2× exit rules to act on.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → False; no positions, day P&L ₹0).
- **Fresh-setup check — BANKNIFTY the only ADX qualifier but SKIPPED on DTE grounds:** Scan (VIX **11.86**, still very low) — NIFTY spot 24,351.4 ADX **43.21** (clearly trending, no), **BANKNIFTY 57,972.5 ADX 13.12** (<18, no open position → the only qualifier), SENSEX 78,087.62 ADX **49.26** (clearly trending, no). NIFTY/SENSEX have trended even harder than earlier today as spot kept drifting up.
  `2026-07-03 intraday IST | BANKNIFTY | 25 | SKIP (DTE far outside window) | nearest expiry 2026-07-28 (re-confirmed via dhan.py lookup → sid 61889, lot 30) | — | — | ADX 13.12 qualifies but 25 DTE is not the ≤7-DTE near-expiry data point that is the entire rationale for trading unvalidated BANKNIFTY`
  - Same reasoning as the four earlier runs today: BANKNIFTY is monthly-only (no weeklies), nearest expiry **2026-07-28 = 25 DTE**, far outside the validated DTE 1-6 window and the ~2-DTE preference. Strategy.md's *sole* justification for trading unvalidated BANKNIFTY is accumulating **near-expiry (≤7 DTE)** data points; a 25-DTE IC does not serve that (negligible intraday theta; backtest showed long-dated BANKNIFTY just drifts to EOD as noise). Opening it would add ~₹5k at-risk for zero data-gathering benefit. **No entry** — no-trade is the correct guardrail-consistent outcome.
- **Broker:** no action (flat, no orders to place/manage). No trade placed or closed → no Telegram.

## 2026-07-03 intraday-monitor (~late intraday IST) — flat, nothing to manage; BANKNIFTY again the only ADX qualifier but SKIPPED (25 DTE, not near-expiry)

**Positions to manage:** none — flat (0 open paper positions in portfolio.md). Nothing for the 50%/2× exit rules to act on.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → False; no positions, day P&L ₹0).
- **Fresh-setup check — BANKNIFTY the only ADX qualifier but SKIPPED on DTE grounds:** Scan (VIX **11.88**, very low) — NIFTY spot 24,326.6 ADX **39.32** (clearly trending, no), **BANKNIFTY 58,004.1 ADX 14.41** (<18, no open position → the only qualifier), SENSEX 77,972.3 ADX **45.82** (clearly trending, no). NIFTY/SENSEX have trended even harder than earlier runs as spot kept drifting up.
  `2026-07-03 intraday IST | BANKNIFTY | 25 | SKIP (DTE far outside window) | nearest expiry 2026-07-28 | — | — | ADX 14.41 qualifies but 25 DTE is not the ≤7-DTE near-expiry data point that is the entire rationale for trading unvalidated BANKNIFTY`
  - Same reasoning as the two earlier runs today: BANKNIFTY is monthly-only (no weeklies), nearest expiry **2026-07-28 = 25 DTE**, far outside the validated DTE 1-6 window and the ~2-DTE preference. Strategy.md's *sole* justification for trading unvalidated BANKNIFTY is accumulating **near-expiry (≤7 DTE)** data points; a 25-DTE IC does not serve that (negligible intraday theta; backtest showed long-dated BANKNIFTY just drifts to EOD as noise). Opening it would add ~₹5k at-risk for zero data-gathering benefit. **No entry** — no-trade is the correct guardrail-consistent outcome.
- **Broker:** no action (flat, no orders to place/manage). No trade placed or closed → no Telegram.

## 2026-07-03 intraday-monitor (~later intraday IST) — flat, nothing to manage; BANKNIFTY again the only ADX qualifier but SKIPPED (25 DTE, boundary flicker at 17.78)

**Positions to manage:** none — flat (0 open paper positions in portfolio.md). Nothing for the 50%/2× exit rules to act on.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → False; no positions, day P&L ₹0).
- **Fresh-setup check — BANKNIFTY the only ADX qualifier but SKIPPED on DTE grounds:** Scan (VIX **11.99**, very low) — NIFTY spot 24,347.65 ADX **37.22** (clearly trending, no), **BANKNIFTY 58,108.3 ADX 17.78, re-confirmed 17.78** (just under the 18 gate → the only qualifier, but a boundary flicker vs earlier 14.89), SENSEX 77,997.77 ADX **41.84** (clearly trending, no). Both validated instruments (NIFTY/SENSEX) have trended harder than the prior run as spot kept drifting up.
  `2026-07-03 intraday IST | BANKNIFTY | 25 | SKIP (DTE far outside window) | nearest expiry 2026-07-28 | — | — | ADX 17.78 barely qualifies but 25 DTE is not the ≤7-DTE near-expiry data point that is the entire rationale for trading unvalidated BANKNIFTY`
  - Same reasoning as this morning's run: BANKNIFTY is monthly-only (no weeklies), nearest expiry **2026-07-28 = 25 DTE**, far outside the validated DTE 1-6 window and the ~2-DTE preference. Strategy.md's *sole* justification for trading unvalidated BANKNIFTY is accumulating **near-expiry (≤7 DTE)** data points; a 25-DTE IC does not serve that (negligible intraday theta; backtest showed long-dated BANKNIFTY just drifts to EOD as noise). ADX 17.78 is also a boundary read. Opening it would add ~₹5k at-risk for zero data-gathering benefit. **No entry** — no-trade is the correct guardrail-consistent outcome.
- **Broker:** no action (flat, no orders to place/manage). No trade placed or closed → no Telegram.

## 2026-07-03 intraday-monitor (~intraday IST) — flat, nothing to manage; BANKNIFTY the only ADX qualifier but SKIPPED (25 DTE, not near-expiry)

**Positions to manage:** none — flat into the close (both ICs squared off at 2026-07-02 EOD). Zero open paper positions in portfolio.md → nothing for the 50%/2× exit rules to act on.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 99400 --day-pnl 0` → False; no positions, day P&L ₹0).
- **Fresh-setup check — BANKNIFTY the only ADX qualifier but SKIPPED on DTE grounds:** Scan (VIX 12.02, very low) — NIFTY spot 24,350.7 ADX **31.31** (clearly trending, no), **BANKNIFTY 58,101.1 ADX 14.89, re-confirmed 14.89** (<18, no open position → the only fresh qualifier), SENSEX 77,942.94 ADX **34.23** (clearly trending, no). Both validated instruments (NIFTY/SENSEX) have trended hard as spot drifted up — no setup.
  `2026-07-03 intraday IST | BANKNIFTY | 25 | SKIP (DTE far outside window) | nearest expiry 2026-07-28 | — | — | ADX 14.89 qualifies but 25 DTE is not the ≤7-DTE near-expiry data point that is the entire rationale for trading unvalidated BANKNIFTY`
  - Confirmed nearest BANKNIFTY expiry via fresh instrument-master lookup (`dhan.py lookup BANKNIFTY 2026-07-28 58200 CE` → sid 61893, lot 30): monthly-only, no weeklies. **2026-07-28 = 25 DTE**, far outside the validated DTE 1-6 window and the ~2-DTE preference. Strategy.md's *sole* justification for trading unvalidated BANKNIFTY is accumulating **near-expiry (≤7 DTE)** data points; a 25-DTE IC does not serve that (negligible intraday theta, backtest showed long-dated BANKNIFTY just drifts to EOD as noise). Opening it would add ~₹5k at-risk for zero data-gathering benefit. **No entry** — no-trade is the correct guardrail-consistent outcome (same reasoning as the 07-02 runs).
- **Broker:** no action (flat, no orders to place/manage). No trade placed or closed → no Telegram.

## 2026-07-02 EOD square-off (~15:15 IST) — BOTH ICs force-closed: SENSEX #2 −₹568.80, NIFTY #3 −₹61.10; day P&L −₹629.90; flat into the close

`2026-07-02 EOD IST | SENSEX | 7 | CLOSE (paper position #2) | IC SP77100/LP76900/SC77500/LC77700 | cost-to-close 165.86/unit vs 161.12 credit | 6 lots (120 qty) | forced EOD square-off, realized −₹568.80`
- **Position closed — SENSEX IC (entry credit 161.12/unit):** priced all four legs via Black-Scholes (spot ~77,511, VIX 12.26, DTE 7). Buy-back SP77100PE 313.73 + SC77500CE 572.17 − sell LP76900PE 247.89 − LC77700CE 472.15 = **cost-to-close 165.86/unit**. Realized = (161.12−165.86)×120 = **−₹568.80**. Spot drifted up to 77,511 through the session, closing just *above* the 77500 upper short → call side went marginally ITM, so the spread cost slightly more to close than the credit collected.
- **Carry-forward test:** FAILS on condition (a) — position is at a loss (cost-to-close 165.86 > entry credit 161.12). Strategy.md is explicit: do NOT carry forward losers. Forced EOD close, no exception. (Also: neither profit target ≤80.56 nor SL ≥322.24 was hit intraday.)

`2026-07-02 EOD IST | NIFTY | 5 | CLOSE (paper position #3) | IC SP24000/LP23900/SC24200/LC24300 | cost-to-close 68.22/unit vs 67.75 credit | 2 lots (130 qty) | forced EOD square-off, realized −₹61.10`
- **Position closed — NIFTY IC (entry credit 67.75/unit):** priced all four legs via Black-Scholes (spot ~24,175, VIX 12.26, DTE 5). Buy-back SP24000PE 61.03 + SC24200CE 137.64 − sell LP23900PE 36.95 − LC24300CE 93.50 = **cost-to-close 68.22/unit**. Realized = (67.75−68.22)×130 = **−₹61.10**. Spot 24,175 closed just above the 24200 upper short — essentially flat, a rounding-level loss.
- **Carry-forward test:** FAILS on condition (a) — marginal loss (68.22 > 67.75). Losers don't carry. Forced EOD close. (Neither profit target ≤33.88 nor SL ≥135.50 hit.)

- **Day totals:** realized −₹568.80 + −₹61.10 = **−₹629.90**. Cash 100,029.90 → **₹99,400.00**. All-time realized +₹29.90 → **−₹600.00**. Circuit breaker not tripped (−₹629.90 vs −₹10,000 trip line).
- **Broker (best-effort):** `square-off-all` only saw the expired sid=71472 artifact → SELL 72260702102081 **REJECTED** ("Fund Limit Insufficient", expired 2026-06-25), confirmed via `order-status`. Known clean terminal rejection, will lapse on its own — no escalation. The strategy ICs can't be broker-closed (DH-905/DH-906 block current weekly securityIds) → paper close in portfolio.md is authoritative.
- **Note on the day:** both ICs drifted the *same* way — NIFTY and SENSEX both crept up through their upper short strikes intraday (NIFTY 24,081→24,175 through the 24200 short region; SENSEX 77,262→77,511 through the 77500 short), so both finished marginally red rather than collecting theta. Not a thesis break: VIX stayed low (12.26) and moves were small/grinding, exactly the low-vol regime the credit spread wants — the shorts just happened to sit right where price drifted to. A −₹630 combined loss on ~₹28k credit at risk across two near-ATM condors is a modest, in-line outcome, not a tail event. EOD Telegram summary sent.

## 2026-07-02 intraday-monitor (~later intraday IST) — HOLD both ICs (#2 −₹436, #3 −₹64); BANKNIFTY qualified on ADX but SKIPPED again (26 DTE, not near-expiry)

**Position management — both open ICs held (spot NIFTY 24,157 / SENSEX 77,363, VIX 12.51):**
`2026-07-02 intraday IST | SENSEX | 7 | HOLD (paper position #2) | IC SP77100/LP76900/SC77500/LC77700 | cost-to-close 164.75/unit | 6 lots (120 qty) | neither 50% target nor 2× SL hit`
- Priced all four legs via Black-Scholes (spot ~77,363, VIX 12.51, DTE 7). Buy-back SP77100PE 373.79 + SC77500CE 513.57 − sell LP76900PE 301.01 − LC77700CE 421.60 = **cost-to-close 164.75/unit**. Gates: PROFIT_TARGET ≤ 80.56 (not hit), SL ≥ 322.24 (not hit) → **HOLD**. Spot 77,363 still inside the 77100/77500 shorts (near upper short); unrealized ≈ (161.12−164.75)×120 = **−₹436**. Exit levels unchanged.
`2026-07-02 intraday IST | NIFTY | 5 | HOLD (paper position #3) | IC SP24000/LP23900/SC24200/LC24300 | cost-to-close 68.24/unit | 2 lots (130 qty) | neither 50% target nor 2× SL hit`
- Priced all four legs via Black-Scholes (spot ~24,157, VIX 12.51, DTE 5). Buy-back SP24000PE 69.86 + SC24200CE 129.68 − sell LP23900PE 43.30 − LC24300CE 88.00 = **cost-to-close 68.24/unit**. Gates: PROFIT_TARGET ≤ 33.88 (not hit), SL ≥ 135.50 (not hit) → **HOLD**. Spot 24,157 sits inside the 24000/24200 shorts (near upper short); unrealized ≈ (67.75−68.24)×130 = **−₹64** (marginally red). Exit levels unchanged.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 100029 --day-pnl -500` → False; combined open unrealized ≈ −₹500, nowhere near −₹10,000 trip line).
- **Fresh-setup check — BANKNIFTY again the only ADX qualifier but SKIPPED on DTE grounds:** Scan — NIFTY 24,156.9 ADX 19.61 (above gate, no — also holds #3), **BANKNIFTY 57,977.45 ADX 15.56, re-confirmed 15.72** (<18, no open position → the only fresh qualifier), SENSEX 77,363.34 ADX 22.03 (above gate, no — also holds #2). India VIX 12.51.
  `2026-07-02 intraday IST | BANKNIFTY | 26 | SKIP (DTE far outside window) | nearest expiry 2026-07-28 | — | — | ADX 15.72 qualifies but 26 DTE is not the ≤7-DTE near-expiry data point that is the entire rationale for trading unvalidated BANKNIFTY`
  - Same reasoning as the prior run today: BANKNIFTY is monthly-only (no weeklies), nearest expiry 2026-07-28 = 26 DTE, far outside the validated DTE 1-6 window and useless for the ≤7-DTE data-gathering that is strategy.md's sole justification for trading unvalidated BANKNIFTY. **No entry** — no-trade is the correct guardrail-consistent outcome.
- **Broker:** paper positions tracked in portfolio.md (source of truth); no broker action (both open orders remain REJECTED by DH-905/DH-906, unchanged). No trade placed or closed → no Telegram.

## 2026-07-02 intraday-monitor (~later intraday IST) — HOLD both ICs (#2 −₹584, #3 −₹65); BANKNIFTY qualified on ADX but SKIPPED (26 DTE, not near-expiry)

**Position management — both open ICs held (spot NIFTY 24,141 / SENSEX 77,375, VIX 12.53):**
`2026-07-02 intraday IST | SENSEX | 7 | HOLD (paper position #2) | IC SP77100/LP76900/SC77500/LC77700 | cost-to-close 165.99/unit | 6 lots (120 qty) | neither 50% target nor 2× SL hit`
- Priced all four legs via Black-Scholes (spot ~77,375, VIX 12.53, DTE 7). Buy-back SP77100PE 371.86 + SC77500CE 520.02 − sell LP76900PE 298.28 − LC77700CE 427.61 = **cost-to-close 165.99/unit**. Gates: PROFIT_TARGET ≤ 80.56 (not hit), SL ≥ 322.24 (not hit) → **HOLD**. Spot 77,375 still inside the 77100/77500 shorts (drifted toward upper short); unrealized ≈ (161.12−165.99)×120 = **−₹584**. Exit levels unchanged.
`2026-07-02 intraday IST | NIFTY | 5 | HOLD (paper position #3) | IC SP24000/LP23900/SC24200/LC24300 | cost-to-close 68.25/unit | 2 lots (130 qty) | neither 50% target nor 2× SL hit`
- Priced all four legs via Black-Scholes (spot ~24,141, VIX 12.53, DTE 5). Buy-back SP24000PE 76.61 + SC24200CE 120.78 − sell LP23900PE 48.32 − LC24300CE 80.82 = **cost-to-close 68.25/unit**. Gates: PROFIT_TARGET ≤ 33.88 (not hit), SL ≥ 135.50 (not hit) → **HOLD**. Spot 24,141 sits inside the 24000/24200 shorts (near upper short); unrealized ≈ (67.75−68.25)×130 = **−₹65** (marginally red). Exit levels unchanged.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 100029 --day-pnl -649` → False; combined open unrealized ≈ −₹649, nowhere near −₹10,000 trip line).
- **Fresh-setup check — BANKNIFTY cleared the ADX gate but SKIPPED on DTE grounds:** Scan — NIFTY spot 24,140.95 ADX 18.53 (above gate, no — also holds #3), **BANKNIFTY 58,047.3 ADX 16.43, re-confirmed 16.19** (clearly <18, no open position → the only fresh qualifier), SENSEX 77,374.55 ADX 21.54 (above gate, no — also holds #2). India VIX 12.53.
  `2026-07-02 intraday IST | BANKNIFTY | 26 | SKIP (DTE far outside window) | nearest expiry 2026-07-28 | — | — | ADX 16.19 qualifies but 26 DTE is not the ≤7-DTE near-expiry data point that is the entire rationale for trading unvalidated BANKNIFTY`
  - BANKNIFTY has monthly-only expiries (no weeklies, confirmed against fresh instrument master): nearest is **2026-07-28 = 26 DTE**. That is far outside the validated DTE 1-6 window and far from the ~2-DTE preference. Critically, strategy.md's *sole* justification for trading unvalidated BANKNIFTY is "to accumulate real **near-expiry (≤7 DTE)** data points" — a 26-DTE IC does not serve that (negligible intraday theta at 26 DTE; backtest already showed BANKNIFTY long-dated trades just drift to EOD as noise, and a near-the-money tune made it worse). Opening it would add ~₹5k at-risk and a EOD-flat/cost-only outcome for no data-gathering benefit. **No entry** — no-trade is the correct guardrail-consistent outcome.
- **Broker:** paper positions tracked in portfolio.md (source of truth); no broker action (both open orders remain REJECTED by DH-905/DH-906, unchanged). No trade placed or closed → no Telegram.


**Position management — both open ICs held (spot NIFTY 24,127 / SENSEX 77,314, VIX 12.56):**
`2026-07-02 intraday IST | SENSEX | 7 | HOLD (paper position #2) | IC SP77100/LP76900/SC77500/LC77700 | cost-to-close 164.26/unit | 6 lots (120 qty) | neither 50% target nor 2× SL hit`
- Priced all four legs via Black-Scholes (spot ~77,314, VIX 12.56, DTE 7). Buy-back SP77100PE 400.72 + SC77500CE 485.98 − sell LP76900PE 323.98 − LC77700CE 398.46 = **cost-to-close 164.26/unit**. Gates: PROFIT_TARGET ≤ 80.56 (not hit), SL ≥ 322.24 (not hit) → **HOLD**. Spot 77,314 still inside the 77100/77500 shorts (drifted toward upper short); unrealized ≈ (161.12−164.26)×120 = **−₹377**. Exit levels unchanged.
`2026-07-02 intraday IST | NIFTY | 5 | HOLD (paper position #3) | IC SP24000/LP23900/SC24200/LC24300 | cost-to-close 67.38/unit | 2 lots (130 qty) | neither 50% target nor 2× SL hit`
- Priced all four legs via Black-Scholes (spot ~24,127, VIX 12.56, DTE 5). Buy-back SP24000PE 80.46 + SC24200CE 115.69 − sell LP23900PE 51.26 − LC24300CE 77.51 = **cost-to-close 67.38/unit**. Gates: PROFIT_TARGET ≤ 33.88 (not hit), SL ≥ 135.50 (not hit) → **HOLD**. Spot 24,127 sits inside the 24000/24200 shorts; unrealized ≈ (67.75−67.38)×130 = **+₹48** (marginally green). Exit levels unchanged.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 100029 --day-pnl -329` → False; combined open unrealized ≈ −₹329, nowhere near −₹10,000 trip line).
- **Fresh-setup check:** none qualifies on an un-held instrument. Scan — NIFTY spot 24,127.3 ADX 15.96 (range-bound but already holds #3, no stacking), BANKNIFTY 58,149.15 ADX 19.42 (above gate, no), SENSEX 77,313.53 ADX 18.25 (above gate, no — already holds #2 anyway). India VIX 12.56. **No new entry.**
- **Broker:** paper positions tracked in portfolio.md (source of truth); no broker action (both open orders remain REJECTED by DH-905/DH-906, unchanged). No trade placed or closed → no Telegram.

## 2026-07-02 intraday-monitor (~later intraday IST) — HOLD SENSEX IC #2 (flat); NIFTY IC #3 OPENED (ADX 15.55, broker DH-905 rejected)

**Position management — SENSEX IC #2 (entry credit 161.12/unit):**
`2026-07-02 intraday IST | SENSEX | 7 | HOLD (paper position #2) | IC SP77100/LP76900/SC77500/LC77700 | cost-to-close 165.54/unit | 6 lots (120 qty) | neither 50% target nor 2× SL hit`
- Priced all four legs via Black-Scholes (spot ~77,218, VIX 12.8, DTE 7 rem). Buy-back SP77100PE 448.42 + SC77500CE 455.44 − sell LP76900PE 365.69 − LC77700CE 372.63 = **cost-to-close 165.54/unit**. Gates: PROFIT_TARGET ≤ 80.56 (not hit), SL ≥ 322.24 (not hit) → **HOLD**. Spot 77,218 sits inside the 77100/77500 shorts; unrealized ≈ (161.12−165.54)×120 = **−₹530** (small drift, theta not yet biting hard). Exit levels unchanged.

**Fresh setup — NIFTY QUALIFIED & OPENED (paper position #3):**
`2026-07-02 intraday IST | NIFTY | 5 | OPEN (paper) | IC SP24000/LP23900/SC24200/LC24300 | net credit 67.75/unit | 2 lots (130 qty) | ADX 15.55 range-bound, cleared all guardrails`
- **Scan:** NIFTY spot 24,081 **ADX(14) 15.55, re-confirmed 15.55** (clearly below 18, robust — not a flicker). BANKNIFTY 57,999 ADX 22.38 (trending, no). SENSEX 77,230 ADX 18.99 (above gate, no — already hold #2 anyway). India VIX 12.78 (low-vol backdrop credit spreads like). NIFTY had no open position → fresh distinct-instrument setup, not stacking on #2.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 100029 --day-pnl -530` → False).
- **Strikes (step 50, ATM 24100):** short 24000PE/24200CE (2 OTM), long 23900PE/24300CE (4 OTM), width 100. Legs est via Black-Scholes (spot ~24,081, VIX 12.76, DTE 5): SP24000PE 98.46 + SC24200CE 99.56 − LP23900PE 64.35 − LC24300CE 65.92 = **net credit 67.75/unit**.
- **DTE choice (5 DTE, 2026-07-07):** nearest listed NIFTY weekly (Tue); within validated DTE 1-6 and closer to the ~2-DTE preference than SENSEX #2's 7.
- **Sized (2 lots):** `size-spread --capital 100029 --width 100 --credit 67.75 --lot-size 65` → 2 lots. Max loss 2×(100−67.75)×65 = **₹4,192.50 ≤ 5% cap (₹5,000)**. Credit collected 67.75×130 = ₹8,807.50.
- **Broker (best-effort):** `place-spread` → **DH-905 Input_Exception** (sandbox OMS still doesn't recognize current NIFTY weekly securityIds — same frozen-instrument blocker as 07-01). **Broker status: REJECTED, 0 legs filled. Paper position NOT unwound** — portfolio.md is source of truth in TRADING_MODE: paper.
- **Exit levels for IC #3 next run:** PROFIT_TARGET cost-to-close ≤ 33.88/unit, SL ≥ 135.50/unit, else forced EOD square-off. Telegram sent (paper position opened + broker rejected).

## 2026-07-02 intraday-monitor (~earlier intraday IST) — HOLD open SENSEX IC (flat); no fresh setup

`2026-07-02 intraday IST | SENSEX | 7 | HOLD (paper position #2) | IC SP77100/LP76900/SC77500/LC77700 | cost-to-close 161.63/unit | 6 lots (120 qty) | neither 50% target nor 2× SL hit`
- **Position managed — SENSEX IC (entry credit 161.12/unit):** priced all four legs via Black-Scholes (spot ~77,232, VIX 12.72, DTE 7). Buy-back SP77100PE 434.19 + SC77500CE 459.18 − sell LP76900PE 354.71 − LC77700CE 377.03 = **cost-to-close 161.63/unit**. Exit gates: PROFIT_TARGET ≤ 80.56 (not hit), SL ≥ 322.24 (not hit) → **HOLD**. Spot 77,232 sits comfortably inside the 77100/77500 short strikes; spread ≈ at entry, unrealized ≈ (161.12−161.63)×120 = **−₹61** (theta hasn't bitten same-day). Exit levels unchanged.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 100029 --day-pnl -61` → False).
- **Fresh-setup check:** none qualifies. Scan — NIFTY spot 24,102.25 ADX 18.4 (above gate, no), BANKNIFTY 58,155.55 ADX 26.37 (trending, no), SENSEX 77,231.92 ADX 20.14 (above gate, no). India VIX 12.72. Already hold SENSEX #2 regardless — no stacking. **No new entry.**
- **Broker:** paper position tracked in portfolio.md (source of truth); no broker action (open order blocked by DH-906 BSE connectivity, unchanged). No trade placed or closed → no Telegram.

## 2026-07-02 intraday-monitor (~intraday IST) — SENSEX IRON CONDOR OPENED (paper position #2, broker best-effort DH-906 BSE rejected)

`2026-07-02 intraday IST | SENSEX | 7 | OPEN (paper) | IC SP77100/LP76900/SC77500/LC77700 | net credit 161.12/unit | 6 lots (120 qty) | ADX 17.09→17.38 range-bound, cleared all guardrails`
- **Positions to manage first:** none open in portfolio.md at start of run → nothing for the 50%/2× exit rules to act on. Flat coming in (NIFTY IC #1 closed at 07-01 EOD).
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 100029 --day-pnl 0` → False).
- **Setup — SENSEX QUALIFIED:** scan NIFTY spot 24,134.7 ADX 18.07 then re-check **18.16** (above the 18 gate → boundary flicker, no entry). BANKNIFTY 58,237.6 ADX 26.14 (trending, no). **SENSEX spot ~77,262 ADX(14) 17.09, re-confirmed 17.38** (clearly below 18, robust — not a flicker). India VIX 12.85 (low-vol backdrop credit spreads like).
- **Strikes (step 100, ATM 77300):** short 77100PE/77500CE (2 OTM), long 76900PE/77700CE (4 OTM), width 200. Legs est via Black-Scholes (spot ~77,300, VIX ~12.7, DTE 7): SP77100PE 402.92 + SC77500CE 482.92 − LP76900PE 326.03 − LC77700CE 398.69 = **net credit 161.12/unit**.
- **DTE choice (7 DTE, 2026-07-09):** only two SENSEX expiries listed — 2026-07-02 (today, **0 DTE**) and 2026-07-09 (**7 DTE**). Both sit just outside the backtest-validated 1-6 window. Chose 07-09 over the 0-DTE per strategy.md's explicit caution against same-day expiry (gamma/bid-ask risk near expiry) and its capital-protection/lower-drawdown-at-higher-DTE preference; 7 DTE is only 1 day beyond the validated range and mirrors yesterday's 6-DTE NIFTY choice. DTE is a soft preference, not a hard guardrail.
- **Sized (6 lots):** `size-spread --capital 100029 --width 200 --credit 161.12 --lot-size 20` → 6 lots. Max loss 6×(200−161.12)×20 = **₹4,665.60 ≤ 5% cap (₹5,000)**. Credit collected 161.12×120 = ₹19,334.40. High credit/width ratio (80%) is structural for SENSEX — 2 strikes = 200 pts ≈ 0.26% OTM on a 77k index, so shorts sit near-ATM; sizing is by defined max-loss per guardrail, so lot count is higher than NIFTY's while risk stays capped.
- **Broker (best-effort):** `place-spread` → **DH-906 Order_Error "Exchange Connectivity is not established for BSE Derivatives"** — a NEW distinct sandbox blocker (BSE-side connectivity, not the NIFTY DH-905 unknown-securityId or the earlier fund-limit DH-906). **Broker status: REJECTED, 0 legs filled. Paper position NOT unwound** — portfolio.md is source of truth in TRADING_MODE: paper.
- **Exit levels for next monitor run:** PROFIT_TARGET cost-to-close ≤ 80.56/unit, SL ≥ 322.24/unit, else forced EOD square-off. Telegram sent (paper position opened + broker rejected).

## 2026-07-01 EOD square-off (~15:15 IST) — NIFTY IC #1 CLOSED for +₹30; flat into the close

`2026-07-01 EOD IST | NIFTY | 6 | CLOSE (paper position #1) | IC SP23950/LP23850/SC24150/LC24250 | cost-to-close 71.78/unit vs 72.01 credit | 2 lots (130 qty) | forced EOD square-off, realized +₹29.90`
- **Position closed — NIFTY IC (entry credit 72.01/unit):** priced all four legs via Black-Scholes
  (spot ~24,008, VIX 13.3, DTE 6). Buy-back SP23950PE 125.50 + SC24150CE 111.20 − sell LP23850PE
  87.72 − LC24250CE 77.20 = **cost-to-close 71.78/unit**. Realized = (72.01−71.78)×130 = **+₹29.90**.
- **Carry-forward test N/A by design:** strategy.md is explicit that a defined-risk spread has no
  reason to carry overnight → forced EOD square-off, no exception. (Even so, note the position was
  only marginally green and ADX still <18 — none of that overrides the forced-close rule.)
- **Broker (best-effort):** `square-off-all` only saw the expired sid=71472 artifact → SELL
  72260701103081 **REJECTED** ("Fund Limit Insufficient", expired 2026-06-25), confirmed via
  `order-status`. Known clean terminal rejection, will lapse on its own — no escalation. The strategy
  IC itself can't be broker-closed (DH-905 blocks current weekly securityIds) → paper close in
  portfolio.md is authoritative.
- **Final state:** cash ₹1,00,029.90, all-time realized P&L +₹29.90, today's P&L +₹29.90. No open
  positions. EOD Telegram summary sent.
- **Note on the day:** first paper trade under the portfolio-first restructure ran its full lifecycle
  (open 12:36 → held through 13:36/14:36 monitors → EOD close) — the paper-position accounting worked
  end-to-end even though the sandbox broker stayed unusable all day. Nothing contradicted backtest
  expectations: a low-vol (VIX ~13.3), ADX<18 range-bound NIFTY day let a 2-strike-OTM iron condor
  sit essentially at entry value with theta only just starting to bite same-day — a small green close
  is exactly the modest, high-probability outcome the credit-spread thesis predicts on a quiet day.

## 2026-07-01 intraday-monitor (~14:36 IST) — HOLD open NIFTY IC (near flat, slight +); no fresh setup

`2026-07-01 14:36 IST | NIFTY | 6 | HOLD (paper position #1) | IC SP23950/LP23850/SC24150/LC24250 | cost-to-close 71.58/unit | 2 lots (130 qty) | neither 50% target nor 2× SL hit`
- **Position managed — NIFTY IC (entry credit 72.01/unit):** priced all four legs via Black-Scholes
  (spot 24,018.6, VIX 13.4, DTE 6). SP23950PE 123.15 + SC24150CE 116.49 − LP23850PE 86.56 −
  LC24250CE 81.50 = **cost-to-close 71.58/unit**. Exit gates: PROFIT_TARGET ≤ 36.01 (not hit),
  SL ≥ 144.02 (not hit) → **HOLD**. Spot near condor center (~24,050 mid); spread sits ~at entry,
  unrealized ≈ (72.01−71.58)×130 = **+₹56** (marginally green vs −₹117 last run). Exit levels unchanged.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 100000 --day-pnl 56` → False).
- **Fresh-setup check:** NIFTY ADX(14) **16.97** qualifies (<18) but already holds position #1 —
  no stacking. BANKNIFTY spot 57,947.75 ADX 27.96 (trending, no), SENSEX spot 77,044.22 ADX 18.44
  (above gate, no). India VIX 13.39. **No new entry.**
- **Broker:** paper position tracked in portfolio.md (source of truth); no broker action (open order
  still blocked by DH-905/DH-906, unchanged). No trade placed or closed → no Telegram.

## 2026-07-01 intraday-monitor (~13:36 IST) — HOLD open NIFTY IC (near flat); no fresh setup

`2026-07-01 13:36 IST | NIFTY | 6 | HOLD (paper position #1) | IC SP23950/LP23850/SC24150/LC24250 | cost-to-close 72.91/unit | 2 lots (130 qty) | neither 50% target nor 2× SL hit`
- **Position managed — NIFTY IC (opened 12:36, entry credit 72.01/unit):** priced all four legs via
  Black-Scholes (spot 24,029.6, VIX 13.32, DTE 6). SP23950PE 115.39 + SC24150CE 123.49 −
  LP23850PE 78.70 − LC24250CE 87.27 = **cost-to-close 72.91/unit**. Exit gates: PROFIT_TARGET ≤ 36.01
  (not hit), SL ≥ 144.02 (not hit) → **HOLD**. Spot barely moved from ~24,034 entry, so the spread
  sits essentially at entry value; unrealized ≈ (72.01−72.91)×130 = **−₹117** (theta hasn't bitten
  same-day). Exit levels unchanged for next run.
- **Circuit breaker:** not tripped (`risk.py circuit-breaker --capital 100000 --day-pnl -117` → False;
  −₹117 is nowhere near the −₹10,000 / −10% trip line).
- **Fresh-setup check:** NIFTY ADX(14) **14.57** does qualify (<18) but already holds position #1 —
  no stacking. BANKNIFTY spot 58,024.95 ADX 25.24 (trending, no), SENSEX spot 77,035.62 ADX 20.22
  (trending, no). India VIX 13.34. **No new entry.**
- **Broker:** paper position tracked in portfolio.md (source of truth); no broker action this run
  (open order still blocked by DH-905/DH-906, unchanged). No trade placed or closed → no Telegram.

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
