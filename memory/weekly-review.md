# Weekly Review

Performance vs. backtest expectations (~8-9 trades/month combined, ~70-79% win rate in backtest),
graded honestly each week. Flag drift from backtest expectations as a signal to slow down and
investigate — not as an automatic trigger to change `memory/strategy.md`.

---

## Week of 2026-07-06 (Mon 07-06 → Thu 07-09, in-progress) — 0 trades: indices trending ALL week, every stock qualifier earnings-blocked (Jul 30 monthly ∩ Q1 season) with Pushkar's steer still pending — INCOMPLETE, on track, no drift; the pending earnings decision is now the binding blocker

**Supersedes the first-cut version of this same week** (which was written after only Monday, when
capital briefly read ₹50k). The week now has **four distinct no-trade sessions** (Mon 07-06 → Thu
07-09), and capital was **reset to ₹4,00,000 by Pushkar on 07-07** (commit context in portfolio.md).
Backtest yardstick for the combined phase: **~40 trades/month ≈ ~9/week (indices + stocks)**,
89% WR stocks / 70-79% indices.

**The week's tally (indices — NIFTY/SENSEX validated; BANKNIFTY separate below):**
- Trade count: **0** (index 0, stock 0). Nothing placed, closed, or carried all week.
- Win rate: **N/A** (no completed trades).
- P&L: **₹0.00.** Capital **₹4,00,000** (reset 07-07), realized-from-reset ₹0. Flat with 0 open
  positions every session — came in flat from the 07-02 EOD square-off, opened nothing since.
  (The three closed positions in portfolio.md — NIFTY/SENSEX/NIFTY, net −₹600 — are all 07-01/07-02,
  i.e. *last* week; they belong to the week-ending-07-03 review, not this one.)

**vs. backtest expectations (~9/week combined, 89% WR stocks / 70-79% indices):**
- **Frequency: 0 vs ~9/week — well below pace, but fully explained by TWO independent blockers,
  neither a drift/edge signal.** Per the review protocol, a low count with ADX elevated all week =
  trending market = fewer qualifiers = expected. Both legs of the combined strategy were blocked
  for structural (not performance) reasons this week:
  - **Indices — trending EVERY scan, all week.** No sub-18 read on any of the three at any point:
    NIFTY ADX ranged ~24→50, BANKNIFTY ~21→43, SENSEX ~25→47 across the week (peaked hardest into
    the 07-08 risk-off sell-off — NIFTY 50.14 / BANKNIFTY 42.63 / SENSEX 46.53 — then eased but
    stayed firmly ≥18; 07-09 drifted down to ~24/21/26 but never near the gate). VIX low all week
    (~11.5–13.4, brief pop to 15.1 on the 07-08 sell-off). Correct sit-out, no ADX loosening. This
    is now ~3 consecutive weeks of index ADX drought (see watch item 2).
  - **Stocks — 18-19 names cleared ADX<18 daily + the DTE gate, but ALL earnings-blocked.** The
    only in-range stock expiry is the **July monthly 2026-07-30** (21-23 DTE, within 2-30), and it
    collides with **peak Q1 (June-qtr) earnings season** (~Jul 16–Aug 8). No qualifier could be
    affirmatively earnings-cleared — some report within 5 days of expiry (SBIN/MARUTI/EICHERMOT/
    ADANIPORTS ~Jul 31, banned outright), the rest report mid-hold (ULTRACEMCO ~Jul 21, JSW ~Jul 18,
    TECHM/HDFCLIFE ~Jul 16). Per the affirmative "check NSE calendar before entering" guardrail,
    a name that can't be cleared isn't cleared → all skipped. **This is the single most important
    item of the week: it is a recurring calendar constraint AND it awaits a decision from Pushkar**
    (flagged via Telegram since 07-07, still open — see watch item 1).
- **Win rate: N/A** — no completed trades. Nothing to compare to the 89%/70-79% bands.
- **Drawdown / risk control: N/A** — no positions held. Circuit breaker disabled in paper mode.

**Grade: INCOMPLETE — on track, no drift to act on.** Zero trades over four sessions is fully
accounted for: indices in a trending regime the strategy is *designed* to sit out, and the entire
stock universe blocked by a monthly-expiry-in-earnings-season collision that is a calendar artifact,
not an edge failure. Performance is neither tracking nor drifting — the combined phase remains
effectively **unstarted in live conditions** (still 0 stock condors ever entered). No reason to
touch strategy.md (per protocol: drift → investigate, never edit on the spot; there is no drift to
even investigate). The one thing that genuinely needs resolution is external — Pushkar's steer on
the earnings block, not a strategy parameter.

**BANKNIFTY (tracked separately per strategy.md — do NOT blend into the figures above):** **0 trades,
0 new near-expiry data points this week.** BANKNIFTY was *trending* most of the week (ADX ~21→43),
so it wasn't even an ADX qualifier except a brief dip to 17.60 on 07-07 (skipped — 21 DTE monthly,
far outside its ≤7-DTE data-gathering window). Still **0 genuine near-expiry BANKNIFTY data points
accumulated all-time**; "validated" status remains far off. Expected given the monthly cycle.

**Watch items for coming weeks (record, don't act):**
1. **⚠ The pending earnings-season decision is now THE binding blocker on the whole stock program.**
   The combined ~40/month cadence rests almost entirely on stocks (indices trending, see #2), and
   stocks have been earnings-blocked for the *entire first live window since unlock*. Pushkar's
   3-way choice — (a) enter post-earnings name-by-name as each reports [recommended], (b) authorize
   holding through earnings per the Bhavcopy backtest, or (c) stand aside on stocks this cycle — has
   been open/Telegram-flagged since 07-07 and is unresolved 3 days on. Until it's answered the
   40/month figure stays theoretical and the bot will keep logging clean no-trade days. Re-surface it.
2. **Index ADX drought is now ~3 straight weeks.** ADX>18 on essentially every index scan since the
   06-30 launch week. A *regime* observation, not an edge problem — do NOT loosen the 18 threshold;
   just track whether range-bound index days return. Note the 07-09 easing (ADX ~24/21/26) — if it
   keeps cooling, an index qualifier could finally appear.
3. **Broker execution still non-functional** (DH-905 unknown securityIds / DH-906 BSE + margin
   locked by the expired sid=71472 artifact). portfolio.md remains authoritative; a real sandbox
   reset is still needed before any order fills. Carried over — flagged previously, still open.
4. **BANKNIFTY near-expiry drought is structural** — progresses only the ~1 week/month its monthly
   expiry is ≤7 DTE (this cycle ~Jul 21+). Expect long 0-progress stretches.

---

## Week ending 2026-07-03 (Fri) — first live-trade week: 3 trades, 33% win, −₹600; below-band win rate but n=3, drawdown in-line — WATCH, don't change

**First week with actual paper entries.** The prior review covered through 06-30 (0 trades); this
window (07-01 → 07-03) is the first with real positions. VIX stayed low all week (12–13.6), the
low-vol backdrop the credit spread wants.

**The week's tally (validated NIFTY/SENSEX only — BANKNIFTY tracked separately below):**
- Trade count: **3** (NIFTY ×2, SENSEX ×1). ~2 entries/week is the backtest cadence, so 3 is
  slightly *above* pace — fine, not manufactured (each cleared a clean ADX<18 read).
- Win rate: **33.3% (1 win / 2 losses).**
- P&L: **−₹600.00** (−0.6% of ₹1,00,000 capital). Cash ₹1,00,029.90 → ₹99,400.00; all-time
  realized +₹29.90 → −₹600.00.
- Per-trade: #1 NIFTY 07-01 **+₹29.90** (win) · #2 SENSEX 07-02 **−₹568.80** (loss) ·
  #3 NIFTY 07-02 **−₹61.10** (loss). **All three were forced EOD square-offs** — none hit the 50%
  profit target or the 2× stop; each just drifted to a marginal close.

**vs. backtest expectations (~8-9 trades/month ≈ ~2/week, 70-79% win rate, low drawdown):**
- **Frequency: in line** (3 this week ≈ pace; no ADX loosening to force trades — 06-30 and 07-03
  were correctly sat out as trending, and 07-01/07-02 qualifiers were taken).
- **Win rate: below the 70-79% band (33% vs ~75%), but the sample is statistically meaningless.**
  n=3. A single different outcome (#3 was a −₹61 rounding-level loss) flips this to 67%. One week
  of 3 trades cannot confirm or deny a 75% edge — the backtest sample was 491 days. This is NOT a
  drift signal to act on; it is a first data point.
- **Drawdown: fully in line — arguably the week's *good* news.** The defined-risk structure did
  exactly its job: the −₹630 losing day was ~13% of the two condors' combined ~₹4.7k+₹4.2k
  max-loss caps, which were never remotely approached. No tail event, no thesis break, no
  circuit-breaker anywhere near the −₹10k line. "Low drawdown" held.

**Grade: ROUGHLY TRACKING with one below-band metric on a meaningless sample — WATCH, do not
change strategy.md.** The drawdown/risk-control side is behaving exactly as backtested; the win
rate is below band but on n=3, which is noise, not drift. Nothing here justifies touching the
strategy file (per the review protocol: drift → investigate/slow down, never edit on the spot).

**What actually happened (the real signal, from signals-learnings 07-02):** both losses came from
the *same* mechanism — spot drifted steadily one way (up) all session inside a low-ADX regime and
closed right at/just above the upper short strike, so the call side went marginally ITM and the
credit didn't decay. **A low ADX reading means "not strongly trending," NOT "won't drift."** A slow
one-way grind can still pin an at-worst outcome at a near-ATM short. **SENSEX is structurally the
most exposed:** 2 strikes = 200 pts ≈ 0.26% OTM on a 77k index, so its shorts sit near-ATM and a
~0.3% drift touches them — which is why SENSEX's loss (−₹569) was ~9× NIFTY's (−₹61) on a similar
% move.

**BANKNIFTY (tracked separately, per strategy.md — do NOT blend into the figure above):** **0
trades, 0 new near-expiry data points this week.** BANKNIFTY was the *only* ADX qualifier on
several 07-02/07-03 scans (ADX 13-17), but every one was correctly skipped: it is monthly-only
(nearest expiry 2026-07-28 = 25-26 DTE), far outside the ≤7-DTE window that is the *sole* rationale
for trading the unvalidated instrument. Its data-gathering mandate simply had no qualifying day
this week — expected given the monthly cycle, not a miss. Still 0 genuine near-expiry BANKNIFTY
data points accumulated; "validated" status remains far off.

**Watch items for coming weeks (record, don't act):**
1. **SENSEX near-ATM structural exposure.** If SENSEX condors keep losing to the grind-to-short
   mechanism over more weeks while NIFTY holds up, a wider SENSEX short offset (3 strikes OTM) is
   worth *backtesting* — explicitly NOT changing live on this one data point. One loss ≠ a pattern.
2. **Win rate over a real sample.** Revisit once ≥10-15 completed trades exist; only then does the
   33%-vs-75% gap become interpretable. Do not react to it before then.
3. **Broker execution is still non-functional.** Every trade this week was paper-only, priced via
   Black-Scholes — the Dhan sandbox rejected all orders (DH-905 unknown securityIds / DH-906
   BSE connectivity + margin locked by the expired sid=71472 artifact). portfolio.md is
   authoritative, but a real sandbox reset (fresh instrument set + freed margin) is still needed
   before any order actually fills. Flagged to Pushkar previously; remains open.
4. **BANKNIFTY data drought.** Its ≤7-DTE data-gathering will only ever progress in the ~1 week/
   month its monthly expiry is near — expect long stretches of 0 progress; that's structural.

---

## Week ending 2026-06-30 (Tue) — launch week, 0 trades, too early to grade drift

**This is the bot's first week of operation.** Scaffolded + backtested + sandbox-onboarded on
2026-06-29; first operational trading day was 2026-06-30. So this "week" is effectively a single
trading day of live paper operation, not a full week — read the numbers below in that light.

**The week's tally (strategy trades only — onboarding/backtest activity on 06-29 excluded):**
- Trade count: **0** strategy trades placed.
- Win rate: **N/A** (no trades).
- P&L: **₹0.00** — paper cash unchanged at ₹1,00,000.00, all-time realized P&L ₹0.
- Open positions: none. (The net +130 NIFTY-24000-CE in the sandbox account is a pre-existing,
  already-expired test artifact, not a strategy position — see trade-log 2026-06-30.)

**vs. backtest expectations (~8-9 trades/month ≈ ~2/week, 70-79% win rate, low drawdown):**
- 0 trades on ~1 trading day is **fully consistent** with the strategy's designed selectivity
  (~1 entry per 3-4 trading days). It is NOT a low-trade-count drift signal yet — there simply
  hasn't been enough operating time to expect even one entry.
- **Why no entry:** every scan this week read ADX(14) above the 18 entry gate on all three
  instruments — pre-market 06-30: NIFTY 19.5, BANKNIFTY 27.7, SENSEX 22.8; intraday 06-30: NIFTY
  23.9, BANKNIFTY 24.5, SENSEX 22.3. All trending, the exact regime this range-bound credit-spread
  strategy is designed to sit out. India VIX was low (13.3-13.7) — the right low-vol backdrop — but
  trend strength was too high to qualify. No-trade is a valid, designed outcome (strategy.md §exit
  / §expected frequency), not a miss.

**Grade: INCOMPLETE — on track, no drift to act on.** With n=0 trades over one trading day there
is nothing to compare against the 70-79% backtest win rate. Performance is neither tracking nor
drifting — it's unstarted. No reason to touch strategy.md.

**Watch items for coming weeks (record, don't act):**
1. **Do ADX<18 days actually appear?** If several weeks pass with every scan reading ADX>18 and
   zero qualifying setups, that's a signal the regime filter may be mismatched to the current
   market regime — investigate/slow down (per the review protocol), do NOT loosen the ADX
   threshold on the spot. One trending week is noise; flag the pattern only if it persists.
2. **Operational/infra noise this week (not performance, but worth tracking):** the EOD square-off
   routine fired ~3.5h early twice on 06-30 (~11:40 & ~11:57 AM IST vs. the scheduled 3:15 PM) —
   harmless on a no-position day, but a noon "EOD" would miss any afternoon entry; check the cron
   if it recurs. Also a transient pre-market egress block (Yahoo Finance + Telegram 403) earlier
   on 06-30 that self-cleared. Neither affects the performance grade.

---

