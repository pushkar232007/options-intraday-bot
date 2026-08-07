# Research Log — 2026-08

Daily notes on option-chain conditions. Newest entries at top.
Older months → research-log-archive.md


Daily notes on option-chain conditions: ADX/trend reading, India VIX level, PCR, OI buildup by
strike, anything news-driven that might affect the day. Keep entries short. Tail the last 2-3
entries when reading this file in a routine.


## 2026-08-04 (intraday-monitor, latest+4) — routine re-fired; all three indices still trending, board eased a touch further (ADX 28/24/27), none yet crossed the 18 gate; VIX 12.42; no index setup; stocks earnings-blocked; flat, nothing to manage

Fresh `scan` (VIX **12.42**, up from 12.31): NIFTY spot 24,459.85 ADX **28.44** → `range_bound: false`; BANKNIFTY spot 57,402.45 ADX **23.98** → `range_bound: false`; SENSEX spot 78,331.47 ADX **27.38** → `range_bound: false`. vs the prior read this session (30.51/25.66/27.7) all three eased a touch further on a softer spot (NIFTY 24,494→24,460, BANKNIFTY 57,483→57,402, SENSEX 78,472→78,331) — now in the mid/high-20s, BANKNIFTY nearest the gate at 23.98 (~6 above 18). The early-August trend regime continues its slow relaxation (44/40/40 several runs ago → 31/26/28 last run → 28/24/27 now) but no index has crossed under the 18 gate, so none is `range_bound: true`. Still worth watching on later runs — the drift has been consistently downward all session. Per the routine, no `range_bound: true` → no `/trade`. **No index qualifier → no entry.**

**Stocks:** this morning's 14 qualifiers stand (daily ADX static, no mid-day re-scan per protocol; HDFCLIFE 9.53 … NMDC 17.32; TATAMOTORS errored). DTE fine (nearest expiry Aug 27 monthly ≈ DTE 23, inside validated DTE 2–30) so **earnings remains the binding constraint** — tail of peak Q1 FY26 season, so all 14 stay **earnings-blocked** pending Pushkar's steer (standing operating rule, signals-learnings 2026-07-07; the 2026-07-07 question remains unanswered). No stock entry.

**Broker:** ✅ Dhan token valid (`funds` availBal ₹65,301.12; util ₹934,698 = stale sid=71472 Jun2026 artifact) → confirms FLAT. Flat — `/monitor` a no-op (0 open positions). No trade placed or closed → no Telegram. **Git clean:** on read, local HEAD and `origin/main` both at 5c63408 after `git fetch origin main` — prior memory on `main`, no stranding; committing this run to `main`.

---

## 2026-08-04 (intraday-monitor, latest+3) — routine re-fired; all three indices still trending but board EASED notably (ADX 31/26/28), none yet crossed the 18 gate; VIX 12.31; no index setup; stocks earnings-blocked; flat, nothing to manage

Fresh `scan` (VIX **12.31**, up from 12.06): NIFTY spot 24,494.1 ADX **30.51** → `range_bound: false`; BANKNIFTY spot 57,482.85 ADX **25.66** → `range_bound: false`; SENSEX spot 78,471.54 ADX **27.7** → `range_bound: false`. vs the prior read this session (39.74/33.43/33.93 — itself down from 44/40/40) all three eased further into the mid-20s/low-30s on a softer spot (NIFTY 24,558→24,494, BANKNIFTY 57,582→57,483, SENSEX 78,685→78,472). BANKNIFTY nearest the gate at 25.66 (~7.7 above 18) — the trend regime is genuinely relaxing off its early-August peak (44/40/40 two runs ago → 31/26/28 now) but no index has yet crossed under the 18 gate, so none is `range_bound: true`. Worth watching on later runs: at this rate of decay a gate-cross is plausible before EOD. Per the routine, no `range_bound: true` → no `/trade`. **No index qualifier → no entry.**

**Stocks:** this morning's 14 qualifiers stand (daily ADX static, no mid-day re-scan per protocol; HDFCLIFE 9.53 … NMDC 17.32; TATAMOTORS errored). DTE fine (nearest expiry Aug 27 monthly ≈ DTE 23, inside validated DTE 2–30) so **earnings remains the binding constraint** — tail of peak Q1 FY26 season, so all 14 stay **earnings-blocked** pending Pushkar's steer (standing operating rule, signals-learnings 2026-07-07; the 2026-07-07 question remains unanswered). No stock entry.

**Broker:** ✅ Dhan token valid (`funds` availBal ₹65,301.12; util ₹934,698 = stale sid=71472 Jun2026 artifact) → confirms FLAT. Flat — `/monitor` a no-op (0 open positions). No trade placed or closed → no Telegram. **Git clean:** on read, local HEAD and `origin/main` both at 4955c9c after `git fetch origin main` — prior memory on `main`, no stranding; committing this run to `main`.

---

## 2026-08-04 (intraday-monitor, latest+1) — routine re-fired; all three indices still trending (ADX 44/40/40), board holding deep in trend on a ~flat spot; VIX 12.0; no index setup; stocks earnings-blocked; flat, nothing to manage

Fresh `scan` (VIX **12.0**, ~flat vs 11.89): NIFTY spot 24,580.8 ADX **44.43** → `range_bound: false`; BANKNIFTY spot 57,746.0 ADX **40.2** → `range_bound: false`; SENSEX spot 78,733.92 ADX **40.28** → `range_bound: false`. vs the earlier read this session (45.24/39.24/41.57) the board is near-identical on a ~flat spot (NIFTY 24,610→24,581, BANKNIFTY 57,799→57,746, SENSEX 78,798→78,734) — all three hold deep in trend in the low/mid-40s, none within ~22 of the 18 gate. The late-July/into-August trend regime persists. No index has `range_bound: true` → per the routine, no `/trade`. **No index qualifier → no entry.**

**Stocks:** this morning's 14 qualifiers stand (daily ADX static, no mid-day re-scan per protocol; HDFCLIFE 9.53 … NMDC 17.32; TATAMOTORS errored). DTE fine (nearest expiry Aug 27 monthly ≈ DTE 23, inside validated DTE 2–30) so **earnings remains the binding constraint** — tail of peak Q1 FY26 season, so all 14 stay **earnings-blocked** pending Pushkar's steer (standing operating rule, signals-learnings 2026-07-07; the 2026-07-07 question remains unanswered). No stock entry.

**Broker:** flat — `/monitor` a no-op (0 open positions). No trade placed or closed → no Telegram. **Git clean:** on read, local HEAD and `origin/main` both at 1495d16 after `git fetch origin main` — prior memory on `main`, no stranding; committing this run to `main`.

---

## 2026-08-04 (intraday-monitor) — all three indices trending (ADX 45/39/42), firmed a touch further from pre-market on a rising spot; VIX 11.89; no index setup; stocks earnings-blocked; flat, nothing to manage

Fresh `scan` (VIX **11.89**, ~flat vs pre-market 11.93): NIFTY spot 24,609.7 ADX **45.24** → `range_bound: false`; BANKNIFTY spot 57,799.4 ADX **39.24** → `range_bound: false`; SENSEX spot 78,797.66 ADX **41.57** → `range_bound: false`. vs this morning's pre-market read (42.99/37.79/37.72 on NIFTY 24,774) all three firmed a touch further into trend on a modestly higher spot (NIFTY 24,774→24,610 is actually softer intraday, but ADX firmed as the trend leg matured) — all deep in the high-30s/mid-40s, none within ~21 of the 18 gate. The late-July/into-August trend regime persists. No index has `range_bound: true` → per the routine, no `/trade`. **No index qualifier → no entry.**

**Stocks:** this morning's 14 qualifiers stand (daily ADX static, no mid-day re-scan per protocol; HDFCLIFE 9.53 … NMDC 17.32; TATAMOTORS errored). DTE fine (nearest expiry Aug 27 monthly ≈ DTE 23, inside validated DTE 2–30) so **earnings remains the binding constraint** — tail of peak Q1 FY26 season, so all 14 stay **earnings-blocked** pending Pushkar's steer (standing operating rule, signals-learnings 2026-07-07; the 2026-07-07 question remains unanswered). No stock entry.

**Broker:** flat — `/monitor` a no-op (0 open positions). No trade placed or closed → no Telegram. **Git clean:** on read, local HEAD and `origin/main` both at 0a8075a after `git fetch origin main` — prior memory on `main`, no stranding; committing this run to `main`.

---

## 2026-08-03 (intraday-monitor, latest+5) — routine re-fired again; all three indices still trending (ADX 43/37/45), board holding deep in trend on a ~flat spot; VIX 12.04; no index setup; stocks earnings-blocked; flat, nothing to manage

Fresh `scan` (VIX **12.04**, ~flat vs 11.97): NIFTY spot 24,594.95 ADX **42.69** → `range_bound: false`; BANKNIFTY spot 57,750.0 ADX **37.01** → `range_bound: false`; SENSEX spot 78,714.01 ADX **45.08** → `range_bound: false`. vs the prior read this session (43.61/38.77/45.05) the board is near-identical on a ~flat spot (NIFTY 24,594→24,595, BANKNIFTY 57,729→57,750, SENSEX 78,710→78,714) — all three hold deep in trend in the high-30s/mid-40s, none within ~19 of the 18 gate. The late-July/into-August trend regime persists (NIFTY 24,384 Mon pre-market → 24,595 now, +0.86%). No index has `range_bound: true` → per the routine, no `/trade`. **No index qualifier → no entry.**

**Stocks:** this morning's 15 qualifiers stand (daily ADX static, no mid-day re-scan per protocol). DTE fine (nearest expiry Aug 27 monthly ≈ DTE 24, inside validated DTE 2–30) so **earnings remains the binding constraint** — tail of peak Q1 FY26 season, so all 15 stay **earnings-blocked** pending Pushkar's steer (standing operating rule, signals-learnings 2026-07-07; the 2026-07-07 question remains unanswered). No stock entry.

**Broker:** ✅ Dhan token valid (`funds` availBal ₹65,301.12; util ₹934,698 = stale sid=71472 Jun2026 artifact) → confirms FLAT. Flat — `/monitor` a no-op (0 open positions). No trade placed or closed → no Telegram. **Git clean:** on read, local HEAD and `origin/main` both at 2b9e3f8 after `git fetch origin main` — prior memory on `main`, no stranding; committing this run to `main`.

---

## 2026-08-03 (intraday-monitor, latest+4) — routine re-fired again; all three indices still trending (ADX 44/39/45), board holding deep in trend; VIX 11.97; no index setup; stocks earnings-blocked; flat, nothing to manage

Fresh `scan` (VIX **11.97**, ~flat vs 11.95): NIFTY spot 24,594.45 ADX **43.61** → `range_bound: false`; BANKNIFTY spot 57,729.1 ADX **38.77** → `range_bound: false`; SENSEX spot 78,710.01 ADX **45.05** → `range_bound: false`. vs the prior read this session (45.9/45.41/47.78) NIFTY/SENSEX eased a touch and BANKNIFTY eased more (45.41→38.77) but all three still hold deep in trend in the high-30s/mid-40s, none within ~21 of the 18 gate. The late-July/into-August trend regime persists (NIFTY 24,384 Mon pre-market → 24,594 now, +0.86%). No index has `range_bound: true` → per the routine, no `/trade`. **No index qualifier → no entry.**

**Stocks:** this morning's 15 qualifiers stand (daily ADX static, no mid-day re-scan per protocol). DTE fine (nearest expiry Aug 27 monthly ≈ DTE 24, inside validated DTE 2–30) so **earnings remains the binding constraint** — tail of peak Q1 FY26 season, so all 15 stay **earnings-blocked** pending Pushkar's steer (standing operating rule, signals-learnings 2026-07-07; the 2026-07-07 question remains unanswered). No stock entry.

**Broker:** ✅ Dhan token valid (`funds` availBal ₹65,301.12; util ₹934,698 = stale sid=71472 Jun2026 artifact) → confirms FLAT. Flat — `/monitor` a no-op (0 open positions). No trade placed or closed → no Telegram. **Git clean:** on read, local HEAD and `origin/main` both at fa89413 after `git fetch origin main` — prior memory on `main`, no stranding; committing this run to `main`.

---

## 2026-08-03 (intraday-monitor, latest+3) — routine re-fired again; all three indices still trending (ADX 46/45/48), board holding deep in trend; VIX 11.95; no index setup; stocks earnings-blocked; flat, nothing to manage

Fresh `scan` (VIX **11.95**, ~flat vs 11.98): NIFTY spot 24,586.3 ADX **45.9** → `range_bound: false`; BANKNIFTY spot 57,714.0 ADX **45.41** → `range_bound: false`; SENSEX spot 78,775.34 ADX **47.78** → `range_bound: false`. vs the prior read this session (43.26/46.44/44.67) the board is holding deep in trend on a near-flat spot — all three in the mid/high-40s, none within ~27 of the 18 gate. The late-July/into-August trend regime persists (NIFTY 24,384 Mon pre-market → 24,586 now, +0.83%). No index has `range_bound: true` → per the routine, no `/trade`. **No index qualifier → no entry.**

**Stocks:** this morning's 15 qualifiers stand (daily ADX static, no mid-day re-scan per protocol). DTE fine (nearest expiry Aug 27 monthly ≈ DTE 24, inside validated DTE 2–30) so **earnings remains the binding constraint** — tail of peak Q1 FY26 season, so all 15 stay **earnings-blocked** pending Pushkar's steer (standing operating rule, signals-learnings 2026-07-07; the 2026-07-07 question remains unanswered). No stock entry.

**Broker:** flat — `/monitor` a no-op (0 open positions). No trade placed or closed → no Telegram. **Git clean:** on read, local HEAD and `origin/main` both at ac8b291 after `git fetch origin main` — prior memory on `main`, no stranding; committing this run to `main`.

---

## 2026-08-03 (intraday-monitor, latest+2) — routine re-fired; all three indices still trending (ADX 43/46/45), board firmed further still into trend on a rising spot; VIX 11.98; no index setup; stocks earnings-blocked; flat, nothing to manage

Fresh `scan` (VIX **11.98**, up a touch from 11.81): NIFTY spot 24,591.2 ADX **43.26** → `range_bound: false`; BANKNIFTY spot 57,809.65 ADX **46.44** → `range_bound: false`; SENSEX spot 78,755.54 ADX **44.67** → `range_bound: false`. vs the prior read this session (37.91/41.94/39.13) all three firmed further into trend on a still-rising spot (NIFTY 24,579→24,591, BANKNIFTY 57,745→57,810, SENSEX 78,699→78,756) — now all deep in the mid-40s, none within ~25 of the 18 gate. The late-July/into-August trend regime keeps deepening on a persistently rising NIFTY (24,384 Mon pre-market → 24,591 now, +0.85%). No index has `range_bound: true` → per the routine, no `/trade`. **No index qualifier → no entry.**

**Stocks:** this morning's 15 qualifiers stand (daily ADX static, no mid-day re-scan per protocol). DTE fine (nearest expiry Aug 27 monthly ≈ DTE 24, inside validated DTE 2–30) so **earnings remains the binding constraint** — tail of peak Q1 FY26 season, so all 15 stay **earnings-blocked** pending Pushkar's steer (standing operating rule, signals-learnings 2026-07-07; the 2026-07-07 question remains unanswered). No stock entry.

**Broker:** flat — `/monitor` a no-op (0 open positions). No trade placed or closed → no Telegram. **Git clean:** on read, local HEAD and `origin/main` both at ef1f366 after `git fetch origin main` — prior memory on `main`, no stranding; committing this run to `main`.

---

## 2026-08-03 (intraday-monitor, latest+1) — routine re-fired; all three indices still trending (ADX 38/42/39), board firmed further into trend on a rising spot; VIX 11.81; no index setup; stocks earnings-blocked; flat, nothing to manage

Fresh `scan` (VIX **11.81**, up a touch from 11.69): NIFTY spot 24,579.15 ADX **37.91** → `range_bound: false`; BANKNIFTY spot 57,744.95 ADX **41.94** → `range_bound: false`; SENSEX spot 78,698.61 ADX **39.13** → `range_bound: false`. vs the earlier read this session (29.89/34.95/29.64) all three firmed further into trend on a rising spot (NIFTY 24,550→24,579, BANKNIFTY 57,658→57,745, SENSEX 78,558→78,699) — NIFTY 29.89→37.91, BANKNIFTY 34.95→41.94, SENSEX 29.64→39.13, now deeply trending in the high-30s/low-40s, none within ~20 of the 18 gate. The trend regime that has held all of late July and into August continues to deepen on a persistently rising NIFTY (24,384 Mon pre-market → 24,579 now, +0.80%). No index has `range_bound: true` → per the routine, no `/trade`. **No index qualifier → no entry.**

**Stocks:** this morning's 15 qualifiers stand (daily ADX static, no mid-day re-scan per protocol). DTE fine (nearest expiry Aug 27 monthly ≈ DTE 24, inside validated DTE 2–30) so **earnings remains the binding constraint** — tail of peak Q1 FY26 season, so all 15 stay **earnings-blocked** pending Pushkar's steer (standing operating rule, signals-learnings 2026-07-07; the 2026-07-07 question remains unanswered). No stock entry.

**Broker:** flat — `/monitor` a no-op (0 open positions). No trade placed or closed → no Telegram. **Git clean:** on read, local HEAD and `origin/main` both at 9b40f95 after `git fetch origin main` — prior memory on `main`, no stranding; committing this run to `main`.

---
