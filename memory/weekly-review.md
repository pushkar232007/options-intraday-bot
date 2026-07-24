# Weekly Review

Performance vs. backtest expectations (~8-9 trades/month combined, ~70-79% win rate in backtest),
graded honestly each week. Flag drift from backtest expectations as a signal to slow down and
investigate — not as an automatic trigger to change `memory/strategy.md`.

---

## Week of 2026-07-20 (Mon 07-20 → Fri 07-24) — 3 trades (2 NIFTY index + 1 BANKNIFTY, 0 SENSEX, 0 stock), all EOD-forced closes, week +₹41.55; index WR 1/2 = 50% BUT n=2 noise — ON TRACK on P&L/process, with an INVESTIGATE-flag raised: index WR now sub-65% for a 2nd straight week (record + watch, no strategy change). Stocks 0 (earnings-blocked all week). BANKNIFTY +₹8.40 (only near-expiry data point ever).

**Formal weekly-review routine ran 2026-07-24 (Fri).** The book opened three index condors this
week — two NIFTY, one BANKNIFTY — all forced shut at EOD by the index intraday-only rule (none hit
PT or SL), and finished the week a small net positive (**+₹41.55**). The three trades all landed
early week (07-20 / 07-21); from Wed onward the market shifted into a firm directional down-move
(the "07-22 regime") and every scan Wed–Fri read trending on all three indices, so nothing else
qualified. Stocks stayed 100% earnings-blocked all five sessions; SENSEX never dipped sub-18.

**The week's tally (indices — NIFTY/SENSEX validated; BANKNIFTY separate below):**
- Trade count: **2 index** (both NIFTY; SENSEX 0), **0 stock**. Both entered & closed same-day,
  forced at EOD (intraday-only rule); on neither did cost-to-close reach PT (50% decay) or SL (2×) —
  each pinned mid-range between its shorts and closed on residual near-expiry time value.
  - **D — NIFTY Jul 21 (DTE 1), entered 07-20, −₹13.65.** Pinned mid-range 24100/24300 all session
    (entry spot 24,209 → 24,241); closed a hair underwater (exit 38.72 vs credit 38.51) on leftover
    time value, not a directional breach.
  - **E — NIFTY Jul 28 (DTE 7), entered 07-21, +₹46.80.** Pinned mid-range 24150/24350 (entry 24,228
    → 24,185); textbook flat range-bound hold, exit 72.43 vs credit 73.15.
- Win rate: **1/2 = 50%** (index). **On a 2-trade sample this carries no signal** on its own — but
  see the grade: combined with last week it is the 2nd straight sub-65% week, which trips the
  "investigate" flag by the letter of the rule (record + watch, not act). The one loss (D, −₹13.65)
  is normal small range-bound drift caught by the EOD force-close, not a stop-out.
- P&L: **+₹33.15** index (per-trade avg **+₹16.58**). Trivial vs capital (+0.008%).
- Drawdown / risk control: no position ever approached SL; max single loss −₹13.65 (well inside the
  ₹1,745 max-loss on Position D). Circuit breaker disabled (paper). Nothing to flag.

**Combined week P&L (index + BANKNIFTY): +₹41.55.** Capital **₹3,99,880.05**; realized-from-reset
**−₹119.95** (was −₹161.50 entering the week; +₹41.55 this week narrows it).

**vs. backtest expectations (~9/week combined, 89% WR stocks / 70-79% indices):**
- **Frequency: 3 vs ~9/week — below pace, fully explained, not a drift signal.** Per protocol, a low
  count with ADX elevated most of the week = trending market = fewer qualifiers = expected. Indices
  only dipped sub-18 in narrow windows Mon–Tue (07-20 NIFTY 17.18 midday; 07-21 NIFTY 11.46 open,
  BANKNIFTY 17.7); every scan Wed–Fri read trending on all three (ADX mid-20s→mid-40s, the 07-22
  down-move regime). Stocks — the other ~7-8/week of the combined figure — were **100% earnings-
  blocked every session** (Jul 30 monthly ∩ peak Q1). So the achievable count was ~indices-only, and
  indices only qualified early week.
- **Win rate: 1/2 index — noise on its own, but a 2nd sub-65% week (see grade).** The one loss's
  *mechanism* is the same recurring one: intraday-only forces the book flat at 3:15 before theta
  finishes, so a range-bound day that drifts a touch into a short closes at a small loss even though
  the position was never in trouble. Structural to intraday index condors, not an edge failure.
- **Stocks: 0 — the earnings block held the entire week.** Same collision as prior weeks: only
  in-range expiry is the **Jul 30 monthly**, a hold into it spans **peak Q1 (~Jul 16–Aug 8)**. DTE
  compressed 10→6 across the week (final week of the cycle), 23 names cleared ADX<18 daily
  (HDFCLIFE 10.95 … HINDZINC 17.96) but none could be affirmatively earnings-cleared. Pushkar's
  steer (post-earnings name-by-name / hold-through / stand-aside) is **still pending** — watch item 2.

**Grade: ON TRACK on P&L and process — with an INVESTIGATE-flag raised on index win rate.** The two
NIFTY condors behaved exactly as designed (E a clean textbook win; D a benign −₹13.65 EOD drift,
never near SL), the week netted positive, and the low frequency is the documented trending-regime +
earnings-block combination, both expected. **However, honesty requires flagging:** index WR has now
been below the 65% floor for **two consecutive weeks** (last week 1/3 = 33%, this week 1/2 = 50%;
combined **2/5 = 40%** index over the two weeks), which by the letter of the task's "below 65% for
2+ weeks = investigate" rule is an investigate-trigger. **What the investigation finds:** (a) the
combined sample is only **5 index trades** — statistically it still carries little signal; (b) **every
single loss across both weeks has been a sub-₹200 EOD-force-close on a small drift, never a stop-out,
never a real directional breach** — the losses are the *intraday-only mechanism* (watch item 1), not
an edge breakdown; (c) net index P&L over the two weeks is **−₹128.35**, i.e. essentially flat/
trivial. So: **record and keep watching — do NOT change strategy.md** (per protocol: even real drift →
investigate, never edit on the spot; here the "drift" is a 5-trade artifact of a known structural
cost). If sub-65% persists a 3rd/4th week on a larger sample, that escalates watch item 1 into a real
question about the intraday-only rule leaving edge on the table vs. the multi-day hold stocks use.

**BANKNIFTY (tracked separately per strategy.md — do NOT blend into the figures above):** **1 trade,
1 win, +₹8.40** this week — Position F (Jul 28 monthly, DTE-at-entry **7**), the **first BANKNIFTY
condor the bot has ever opened** (the ADX<18 ∩ DTE≤7 carve-out finally aligned on 07-21). It pinned
mid-range 57700/58100 all session and drifted to a flat EOD close — **exactly the "29 of 31 trades
drift to EOD with tiny P&L" pattern the 2026-06-29 re-backtest flagged**, so the first live near-
expiry data point *confirms* the drift-to-flat expectation rather than contradicting it. **All-time
BANKNIFTY tally: 1 trade, 1 win, +₹8.40, 1 near-expiry (≤7-DTE) data point.** One point is essentially
noise — nowhere near enough to judge "validated" status; keep accumulating.

**Watch items for coming weeks (record, don't act):**
1. **⚠ ESCALATING — index WR sub-65% two weeks running, mechanism = EOD force-close.** All 5 index
   trades over the two weeks closed at EOD with neither PT nor SL hit; the 3 losses were all small
   drift-into-a-short closes before theta could decay the position. This is inherent to intraday-only
   index condors. NOT actionable on 5 trades — but it is now a *named, escalating* watch: if the
   forced-close-at-small-loss pattern dominates over 2–3 more weeks, seriously examine whether the
   index intraday-only rule leaves edge on the table vs. the multi-day hold stocks use (would require
   a backtest to change, never an on-the-spot edit).
2. **⚠ Pushkar's earnings-season steer is STILL open (now ~17 days).** Same binding blocker as the
   last three weekly reviews — the whole stock program (the bulk of the ~40/month cadence) has been
   earnings-blocked its entire live window since unlock. The Jul 30 cycle is now nearly over (DTE 6
   Fri); the block will clear mechanically once Q1 season ends / the Aug cycle opens, but the standing
   *policy* question (enter post-earnings name-by-name?) remains unanswered. Re-surface it.
3. **Regime: firm directional down-move since 07-22.** After early-week range-bound windows, all three
   indices trended hard Wed–Fri (the 07-22 down-move: NIFTY spot 24,038→23,616 across the week). Keep
   the 18 threshold untouched; just note the regime is currently trending, so thin index days are
   expected to continue until it relaxes (NIFTY was a gate-hugger at 18.77 by Fri — watch for a turn).
4. **Broker execution still non-functional** (DH-905 unknown securityIds). portfolio.md remains
   authoritative; every trade this week was paper-tracked, broker never held the legs.

---

## Week of 2026-07-13 (Mon 07-13 → Fri 07-17) — 3 index trades (first index condors to actually execute in-window since the reset), all EOD-forced closes, week −₹161.50; WR 1/3 = 33% BUT a 3-trade artifact, not drift — ON TRACK, no strategy change. Stocks 0 (earnings-blocked all week), BANKNIFTY 0.

**Formal weekly-review routine ran 2026-07-17 (Fri).** The week produced the **first index
condors since the 07-07 capital reset that actually opened AND closed inside their window** — three
of them, all forced shut at EOD by the index intraday-only rule (none hit PT or SL). Small sample,
small money, but the combined program is finally off zero on the index side. Stocks stayed shut out
all five sessions (earnings collision, see below); BANKNIFTY never qualified in-window.

**The week's tally (indices — NIFTY/SENSEX validated; BANKNIFTY separate below):**
- Trade count: **3** (index 3, stock 0). All three index, all entered & closed same-day, forced at
  EOD (intraday-only rule) — on none did cost-to-close reach PT (50% decay) or SL (2×); each drifted
  slightly into a short strike and closed at a small P&L.
  - **A — NIFTY Jul 14 (DTE 1), entered 07-13, −₹175.50.** Spot drifted ~58 pts up into the 24250 short call.
  - **B — SENSEX Jul 16 (DTE 3), entered 07-13, −₹35.40.** Spot drifted ~219 pts up to just above the 77600 short call.
  - **C — NIFTY Jul 21 (DTE 5), entered 07-16, +₹49.40.** Stayed pinned mid-range between the 24000/24200 shorts — textbook condor outcome.
- Win rate: **1/3 = 33%** (index). **Below the 65% floor, but on a 3-trade sample it carries no
  signal** — the "below 65% for 2+ weeks" investigate-trigger needs a meaningful sample, and 3 forced
  EOD closes where nothing hit PT/SL is noise, not an edge read. The two losses (−175.50, −35.40)
  are normal small range-bound drift caught by the EOD force-close, not stop-outs.
- P&L: **−₹161.50** for the week (per-trade avg **−₹53.83**). Trivial vs capital (−0.04%). Capital
  **₹3,99,838.50**; realized-from-reset **−₹161.50** (this week IS the entire from-reset P&L — the
  book was flat-since-reset until 07-13).
- Drawdown / risk control: no position ever approached SL; max single loss −₹175.50 (well inside the
  ₹4,045.60 max-loss on Position A). Circuit breaker disabled (paper). Nothing to flag.

**vs. backtest expectations (~9/week combined, 89% WR stocks / 70-79% indices):**
- **Frequency: 3 vs ~9/week — below pace, fully explained, not a drift signal.** Per protocol, a low
  count with ADX elevated most of the week = trending market = fewer qualifiers = expected. Indices
  only dipped sub-18 in two narrow intraday windows all week (07-13 open, 07-16 midday); every other
  scan across all five sessions read trending (ADX mid-20s→high-30s). Stocks — the other ~7-8/week of
  the combined figure — were **100% earnings-blocked every session** (see below). So the achievable
  count was ~indices-only, and indices barely qualified.
- **Win rate: 1/3 index — noise, don't compare to the 70-79% band yet.** Sample far too small. Worth
  noting the *mechanism*: all three closed at EOD because the intraday-only rule forces the book flat
  before theta finishes working, so a range-bound day that drifts a touch into a short by 3:15 closes
  at a small loss even though the position was never in real trouble. That's structural to trading
  index condors intraday, not an edge failure — but see watch item 1.
- **Stocks: 0 — the earnings block held the entire week.** Same collision as the prior two weeks: the
  only in-range expiry is the **Jul 30 monthly**, and a hold into it spans **peak Q1 season (~Jul 16–
  Aug 8)**. 17 names cleared ADX<18 + DTE daily (SBIN 11.05 … MARUTI 16.17) but none could be
  affirmatively earnings-cleared (SBIN/MARUTI ~Jul 31 within 5 days of expiry = banned; rest held
  through a pending result). Pushkar's steer (enter post-earnings name-by-name / hold-through /
  stand-aside) is **still pending** — see watch item 2.

**Grade: ON TRACK — no drift to act on.** The index side finally executed and behaved as designed
(C is a clean textbook win; A/B are small drift losses inside SL). The 33% WR is a 3-trade artifact,
not a trend — do NOT read it as the WR drifting below the band, and do NOT touch strategy.md (per
protocol: even real drift → investigate, never edit on the spot; here there is no real drift). The
combined ~40/month cadence remains theoretical because stocks are still shut out on the calendar.

**BANKNIFTY (tracked separately per strategy.md — do NOT blend into the figures above):** **0 trades,
0 new near-expiry data points this week.** BANKNIFTY qualified on ADX several times (dipped <18 intraday
on 07-16 and 07-17-first) but only the **Jul 28 monthly** was listed (11-12 DTE, no weeklies), far
outside its ≤7-DTE data-gathering window → skipped every time on DTE grounds. Still **0 genuine
near-expiry BANKNIFTY data points accumulated all-time**; "validated" status remains far off. Expected
given it now trades only a monthly cycle.

**Watch items for coming weeks (record, don't act):**
1. **EOD force-close is quietly costing the index side.** All three trades this week closed at EOD
   with neither PT nor SL hit; two were small losses purely because spot drifted a little into a short
   by 3:15 before theta could decay the position. This is inherent to intraday-only index condors and
   is NOT a reason to change anything yet — but track it: if a pattern of "forced-close-at-small-loss"
   dominates over several weeks, it's worth asking whether the index intraday-only rule is leaving
   edge on the table vs. the multi-day hold that stocks use. Record only; no action.
2. **⚠ Pushkar's earnings-season steer is STILL open (now ~10 days).** Same binding blocker as the
   prior two weekly reviews — the whole stock program (the bulk of the ~40/month cadence) has been
   earnings-blocked for its entire live window since unlock. Re-surface it; until answered the book
   stays index-only and thin.
3. **Index ADX drought easing but choppy.** Sub-18 windows did appear this week (07-13, 07-16) after
   ~3 weeks of drought — the regime is loosening enough to occasionally qualify. Keep the 18 threshold
   untouched; just note that range-bound index days are starting to return.
4. **Broker execution still non-functional** (DH-905 unknown securityIds). portfolio.md remains
   authoritative; every trade this week was paper-tracked, broker never held the legs.

---

## Week of 2026-07-06 (Mon 07-06 → Thu 07-09) — 0 trades: indices trending ALL week, every stock qualifier earnings-blocked (Jul 30 monthly ∩ Q1 season) with Pushkar's steer still pending — INCOMPLETE, on track, no drift; the pending earnings decision is now the binding blocker

**Formal weekly-review routine ran 2026-07-09 (Thu)** and confirmed the grade below — nothing
changed vs. the running in-progress read (four clean no-trade sessions, 0 trades, no drift). Fri
07-10 still to come but cannot alter the tally materially: indices would need to break a ~3-week
ADX drought AND a stock name would need to earnings-clear, both unlikely in one session.
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

