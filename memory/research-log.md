# Research Log

Daily notes on option-chain conditions: ADX/trend reading, India VIX level, PCR, OI buildup by
strike, anything news-driven that might affect the day. Keep entries short. Tail the last 2-3
entries when reading this file in a routine.

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
