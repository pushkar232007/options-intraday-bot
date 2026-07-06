# Research Log

Daily notes on option-chain conditions: ADX/trend reading, India VIX level, PCR, OI buildup by
strike, anything news-driven that might affect the day. Keep entries short. Tail the last 2-3
entries when reading this file in a routine.

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
