# Signals & Learnings

## 2026-07-21 (EOD) — FIRST BANKNIFTY near-expiry data point CLOSED: flat/noise (+₹8.40), matching backtest expectation

The first-ever BANKNIFTY iron condor (Position F, opened this morning — see the entry below) was
EOD force-closed for **+₹8.40** (exit 153.27 vs credit 153.55, DTE-at-entry 7). It was pinned
mid-range between the 57700/58100 shorts all session (spot 57,882 → 57,833, ~49 pts, well inside
both shorts) and never came close to PT (76.78) or SL (307.10). **This is exactly the behavior the
2026-06-29 BANKNIFTY re-backtest flagged: "29 of 31 trades drift to EOD with tiny P&L."** So the
first live near-expiry (≤7-DTE) data point *confirms* the drift-to-flat pattern rather than
contradicting it — one data point, essentially noise, no edge visible yet either way. **Running
BANKNIFTY-only tally (kept separate from validated NIFTY/SENSEX per strategy.md): 1 trade, 1 win
(barely), +₹8.40, DTE-at-entry 7 (near-expiry).** Still nowhere near enough to judge "validated"
status — keep accumulating. On the same day, NIFTY (Position E, also Jul 28 / DTE 7) behaved
identically (+₹46.80, also flat mid-range) — the anticipated comparably-near-ATM quiet-drift played
out benignly for both, no directional breach of either condor. No thesis update.

## 2026-07-21 — FIRST BANKNIFTY entry ever: the data-gathering carve-out finally fired (ADX<18 AND DTE≤7 aligned)

Position F is the **first BANKNIFTY iron condor the bot has ever opened** — the milestone the
2026-06-29 BANKNIFTY note anticipated ("trade BANKNIFTY in paper anyway to accumulate real
near-expiry data points over the coming months"). It took this long because BANKNIFTY needs
**two independent conditions to line up on the same day**, and they rarely do:
1. **ADX(14) < 18** (range-bound) — the usual index entry gate; and
2. **The Jul 28 monthly at DTE ≤ 7** — because BANKNIFTY is monthly-only (no weeklies, SEBI
   removed them), so on most days its nearest expiry is DTE 11-30, far outside the ≤7-DTE
   near-expiry window where the edge (such as it is) actually lives. Every prior qualifying-ADX
   day this month (07-16 DTE 12, 07-17 DTE 11, etc.) was skipped purely on DTE grounds.

Today (Jul 21) both aligned for the first time: ADX 17.7, Jul 28 monthly at exactly DTE 7. Entry:
SP57700/LP57500/SC58100/LC58300, 1 lot (30), credit 153.55/unit (₹4,606.50), DTE-at-entry **7**.
Because it's an index it's still intraday-only (force-closed at EOD), so this is a *near-expiry
intraday* data point, not a multi-day hold — but that matches how NIFTY/SENSEX index condors run,
and it's the kind of data the carve-out wants. **Tracking reminder (per strategy.md): assess
BANKNIFTY's results SEPARATELY from NIFTY/SENSEX — do not blend into a combined win-rate figure.
Its sample is known-thin (~2 genuine near-expiry data points in the whole backtest window); every
new live data point like this one matters for eventually deciding whether BANKNIFTY earns
"validated" status.** No thesis update — this is a normal qualifying setup, just the first for this
instrument. Watch how it behaves vs. NIFTY on the same day (both Jul 28, both DTE 7): BANKNIFTY's
2-strike offset is 200 pts ≈ 0.35% OTM on a ~58k index vs NIFTY's 100 pts ≈ 0.41% — comparably
near-ATM, so a similar quiet-drift risk to the one that pinned SENSEX on 2026-07-02.

## 2026-07-07 — DTE 2-30 unlocks early-cycle entry, but the July monthly expiry COLLIDES with Q1 earnings season → all 18 stocks skipped on earnings; + fixed dhan.py stock-lookup bug

First market-hours run with the DTE 2-30 cap live (commit c1b555d). Stocks are no longer
DTE-blocked (23-DTE Jul 30 expiry now qualifies), so the **earnings guardrail becomes the binding
constraint** — and for this cycle it blocks everything:

- The only in-range stock expiry is the **July monthly, 2026-07-30**. Entering now (Jul 7, 23 DTE)
  means holding a short-vol condor straight through the company's Q1 (June-qtr) result. Q1 season
  runs ~Jul 16–Aug 8, so essentially the entire liquid Nifty universe reports **during the hold**.
- Verified via web research (dates approximate, future-dated sources conflate FY labels): **SBIN
  ~Jul 31, MARUTI Jul 31** → within 5 days of the Jul 30 expiry (banned outright by the earnings
  guardrail — pre-earnings IV ramp hits the final days near expiry). **COALINDIA** trading window
  closed Jul 1, result imminent. **TECHM ~Jul 16, HDFCLIFE ~Jul 16, RELIANCE** mid-late July →
  held through the earnings gap. Could **not affirmatively clear a single one** of the 18 qualifiers.
- strategy.md guardrail: "Never trade a stock during earnings week... Check NSE calendar before
  entering." That check is an *affirmative* requirement — a name that can't be cleared isn't
  cleared. → **All 18 skipped. No-trade is the correct, guardrail-consistent outcome**, not
  over-caution: the monthly-expiry-in-earnings-season collision genuinely disqualifies the universe.

**Refined operating rule (supersedes the "enter any day of the month" optimism in the c1b555d note
below):** DTE 2-30 is validated on Bhavcopy that *did* include earnings gaps (89-94% WR), so the
backtest tolerates earnings holds — BUT the explicit hard guardrail still forbids per-name earnings
proximity to expiry, and the cleanest execution is to enter a stock condor **only after that name
has already reported** (earnings behind us) for the remaining DTE into expiry. For the July cycle
that means candidates become enterable name-by-name as each reports (e.g. RELIANCE after ~Jul 21,
holding ~9 days into Jul 30). Do NOT open early-cycle condors held blind through a pending result.

**Decision needed from Pushkar (Telegram-flagged):** (a) enter post-earnings, name-by-name, as each
reports this month [recommended — respects both the guardrail and the theta edge]; or (b) explicitly
authorize holding through earnings per the backtest and enter now (accepting occasional gap losses
the 89-94% WR already prices in); or (c) stand aside on stocks until a cycle without earnings overlap.

**Tooling fix (committed this run):** `scripts/dhan.py find_security_id` hardcoded
`INSTRUMENT == "OPTIDX"`, so **every stock (OPTSTK) lookup silently returned "no contract found"** —
stock trading was strategy-approved but the tooling never supported it. Fixed to match
`("OPTIDX", "OPTSTK")`. Verified: SBIN 30-Jul 1050CE → sid 1143559/BSE/lot 750; RELIANCE → lot 500;
NIFTY index lookup unaffected. Note: single-stock options sit on **BSE** in the Dhan master
(EXCH_ID=BSE, `_exchange_segment` already maps → BSE_FNO), strike steps are tight (SBIN step 10).

## 2026-07-07 — Stock options are MONTHLY-ONLY: DTE 2-7 stock guardrail is unexecutable except near monthly expiry

First market-hours run after stocks were unlocked (strategy.md commit 42d8033). Discovered a
spec/reality gap that blocks every stock entry under the current guardrails:

- strategy.md's stock section states "DTE range: 2-7 days (**stocks have weekly + monthly
  expiry**)". That premise is **false**. Checked the Dhan instrument master directly across 18
  qualifying names (SBIN, TITAN, RELIANCE, ITC, MARUTI, TECHM, ULTRACEMCO, POWERGRID, COALINDIA,
  BPCL, HDFCLIFE, SBILIFE, HEROMOTOCO, EICHERMOT, PNB, CANBK, BANKBARODA, HINDUNILVR): **every one
  is monthly-only** — expiries 2026-07-30, 2026-08-27, 2026-09-24 and nothing in between. Indian
  single-stock options have no weeklies (only NIFTY/SENSEX indices do; SEBI removed stock weeklies).
- Consequence: on any given day the nearest stock expiry is up to ~23 DTE (Jul 7 → Jul 30). That
  is far outside the DTE 2-7 hard cap, so **all stock qualifiers get skipped every day except in
  the ~week before monthly expiry** (this cycle ≈ Jul 23–28, when Jul 30 sits at 2-7 DTE).
- This is the same structural issue that skips BANKNIFTY daily (monthly-only, 25 DTE). And it's
  consistent with the backtest, which "held 2-7 days into expiry" — i.e. the stock edge is a
  **near-monthly-expiry theta trade**, entered ~2-7 days before expiry, not an any-day trade. A
  23-DTE condor held a few days captures almost no theta (long-dated positions just drift to EOD
  as noise), so entering now would not reproduce the validated setup even if the cap were waived.

**Operating rule until Pushkar decides otherwise:** treat stock condors as a late-month trade —
evaluate the 18-name scan only when the monthly expiry is within DTE 2-7 (≈ last week of the
monthly cycle), enter then, hold into expiry per the stock exit rules. On all other days, log the
qualifiers for awareness and skip on DTE grounds (no re-alerting — this entry is the reference).
**Decision needed from Pushkar:** either (a) formally re-word strategy.md to "enter stock condors
2-7 DTE before the monthly expiry" (recommended — matches the backtest and reality), or (b)
explicitly relax the stock DTE cap to allow monthly-at-entry as a data-gathering carve-out like
BANKNIFTY. Do not loosen the guardrail unilaterally.

## 2026-07-07 — **SUPERSEDED:** Stock DTE cap expanded to 2-30 after split-sample validation

Pushkar ran split-sample backtests on DTE 8-14 and DTE 15-30 windows using the same real
Bhavcopy data. Both passed PF > 1.2 in both halves:
  - DTE 2-7:   H1 PF 4.60, H2 PF 16.88 (original validated window)
  - DTE 8-14:  H1 PF 9.09, H2 PF 13.35 ← newly validated
  - DTE 15-30: H1 PF 19.64, H2 PF 55.25 ← newly validated

**strategy.md updated (commit c1b555d):** DTE cap is now 2-30. Stock condors can now enter
any day of the month — not just the last week. One-trade-per-symbol guardrail added to prevent
stacking concurrent condors on the same name. The above "DTE-blocked" reasoning is no longer
operative — 23 DTE now qualifies. Realistic combined volume ~60-80 trades/month.

## 2026-07-01 — FIRST live-sandbox spread attempt blocked: naked-leg margin + un-clearable artifact

The very first time this bot hit a qualifying setup and tried to place a real iron condor
(SENSEX, ADX 17.09), the order was **rejected by Dhan sandbox (400 DH-906)** before any leg
filled. Two compounding causes, both now known so future routines don't re-derive them:

1. **`place-spread` is margined as a naked short at leg 1.** It places legs sequentially in the
   order `[short-put SELL, long-put BUY, short-call SELL, long-call BUY]` — so the very first
   order is a *naked* short put, which the broker margins at full naked-short requirement
   (several lakh for SENSEX) before the protective long wing exists. A defined-risk condor's real
   margin (≈ its ₹5k max loss) is never reached because it never gets past leg 1. **Fix to
   consider: reorder to place BUY (long) legs first, or submit as a margin-benefit basket.**
2. **Sandbox `availableBalance` is only ₹65,301** — `utilizedAmount` ₹934,698 (of the ~₹10L
   sandbox notional) is locked by the leftover expired sid=71472 test-artifact positions, whose
   closing SELLs keep getting REJECTED ("Fund Limit Insufficient") and can't be cleared because
   the contract expired 2026-06-25. So even the correctly-margined ₹5k condor may not fit until
   the sandbox is reset/topped up.

**Lesson:** "validated end-to-end against the sandbox" (strategy.md) covered funds/orders/position
*reads* and a single naked test order — it never actually placed a full 4-leg condor. First real
placement surfaced this. Until (1) place-spread leg ordering and/or (2) the sandbox margin state
is fixed, qualifying setups will keep getting rejected at entry. Flagged to Pushkar via Telegram +
routine push on 2026-07-01.

## 2026-06-29 — naked option buying rejected, credit spreads adopted (pre-launch backtest)

Before this bot ever placed a paper trade, six versions of naked directional option-buying were
backtested (in `backtest/` in this repo) and rejected:

- v1: opening-range breakout + EMA9/21 + RSI — lost money, 30% win rate.
- v2: + ATR range filter, fixed 2:1 reward:risk — P&L flips sign across nearby days-to-expiry
  values (a classic overfitting fingerprint, not real edge).
- v3: + daily-trend-alignment filter — looked great on a 60-day sample (+40%), but **lost badly
  (-40% to -80%) once tested on a proper 491-day sample**. The 60-day "win" was a small-sample
  artifact, not real.
- v4: mean-reversion fade (the opposite direction from v1-v3) — also failed on the large sample.
- v5: added an ADX trend-strength filter but scanned for entries all day — failed worse, because
  late-day entries left no runway before forced EOD exit (0-17% win rate). Diagnosed as a timing
  bug, not proof the ADX idea was bad.
- v6: fixed the timing (entries back at the open, like v3) + kept the ADX filter — still lost
  money on the large sample (-53k to -77k). Confirmed: it's not a timing artifact, naive directional
  signals just don't have edge here.

**Lesson:** a strategy that "wins" on a 60-day sample but flips sign when you change one
parameter slightly, or when you extend the sample, is noise — not edge. Always test across
multiple parameter values and the largest sample you can get before trusting a backtest result.

**What worked instead:** selling iron condors (defined-risk credit spreads) specifically on days
ADX(14) reads below 18 (range-bound/chop) — profitable across every DTE (1-6) and every timeframe
tested (1h/15m/5m), with win rates of 67-86%. This matches a known real phenomenon (index option
IV tends to run a bit above realized volatility on average), not a discovered technical pattern —
that's part of why it's more believable than the directional attempts. See `memory/strategy.md`
for the adopted structure and guardrails.

**Open question, not yet answered by backtest:** the 2-year backtest window had no true tail/crisis
event. Watch live/paper performance closely on any day VIX spikes hard or the underlying gaps —
that's exactly the scenario the backtest couldn't validate.

## 2026-06-29 — scripts/dhan.py corrected against a real Dhan Sandbox account

`scripts/dhan.py` was originally written without live credentials (pure guesswork from general
DhanHQ knowledge). Tested end-to-end against a real sandbox account the same day and found/fixed
several real bugs - don't repeat these:

- **Orders need `securityId` (numeric) + `dhanClientId` in the body, not `tradingSymbol`.** The
  original script guessed `tradingSymbol` - wrong, every order would have failed.
- **Lot sizes were wrong.** Guessed NIFTY=75/BANKNIFTY=35; real values (verified against Dhan's
  published instrument master) are NIFTY=65/BANKNIFTY=30/SENSEX=20. Backtest re-run with corrected
  sizes - conclusion unchanged (win rate/robustness identical, P&L magnitude barely moved).
- **BANKNIFTY has no weekly options anymore - monthly only.** memory/strategy.md said "weekly" for
  all three instruments; corrected. The backtest's DTE=1-6 range does not represent BANKNIFTY's
  real expiry cycle - don't trust that instrument's backtest numbers without a dedicated re-test.
- **Market data (option chain, quotes) is NOT available in the free sandbox** - confirmed 404 on
  every path tried (`/optionchain`, `/optionchain/expirylist`, `/marketfeed/ltp`,
  `/marketfeed/quote`). Needs a real account + the paid Data API subscription (~Rs499/month).
  Sandbox only covers order/fund/position management.
- **Closing orders are not reliably fast.** A test BUY filled in ~3 seconds; the matching closing
  SELL on the same contract sat `PENDING` with `filledQty: 0` for over a minute and was eventually
  cancelled rather than waited out further - its `drvExpiryDate` field oddly showed a date 4 days
  before the test date, which may be why. **Never trust a `TRANSIT` response as confirmation -
  poll `order-status` until `TRADED`.** This is now baked into `.claude/commands/squareoff.md` and
  `monitor.md`.
- **`/positions` returned `[]` even right after a confirmed `TRADED` fill.** Track open positions
  by filtering `/orders` for `orderStatus == "TRADED"` and netting BUY/SELL qty per `securityId`
  instead - this is what `square-off-all` and the monitor command now do.

If live trading later behaves differently from these sandbox findings (e.g. closing orders fill
fast, `/positions` populates correctly), that's worth a new dated entry here too - don't assume
sandbox quirks automatically carry over to live, only that they're confirmed *in sandbox*.

## 2026-06-29 — BankNifty backtested against its real monthly cycle: roughly breakeven, mostly noise

Re-ran the validated iron-condor strategy against BANKNIFTY's actual monthly expiry calendar
(see `backtest_banknifty_monthly.py` - it no longer has weekly options, see the correction above).
Result: 31 trades over ~10 months (the only window with a stable expiry-day convention), 61.3% win
rate, but total P&L only +₹1,166 - essentially flat.

Looked at the trade-level detail before concluding anything: **29 of 31 trades exit at EOD with
tiny P&L (mostly ±100-300)** regardless of win/loss - consistent with far-from-expiry options
barely moving in one day (slow theta, low gamma that far out), so the strategy's 50%-target/2x-
stop thresholds almost never trigger and the outcome is just incidental drift, not a real signal.
**The only two trades with real magnitude were both right before expiry** (DTE 1 and 0.2) - a
+1,681 win immediately followed by a -1,377 loss, which nearly cancel out and are far too few data
points (n=2) to call either a win or a loss pattern.

Tried fixing it with `strategy_spread_banknifty_v1.py` (near-the-money strikes 1/3 instead of 2/4,
smaller 15% profit target instead of 50%, reasoning that long-dated options need more gamma/a more
realistic single-day target) - made it slightly worse (-₹1,722), not better. **This was not a
quick-fix-the-parameters situation - the real issue is there's only a couple of genuine
near-expiry data points in the whole window, not that the structure is wrong.** Don't keep
iterating on synthetic backtests trying to manufacture more BankNifty edge from a window that
just doesn't have enough near-expiry days in it.

**Decision:** trade BANKNIFTY in paper mode anyway (alongside the validated NIFTY/SENSEX) since
real money isn't at risk yet, specifically to accumulate real near-expiry data points over the
coming months. Track its results separately in reviews - don't blend into the NIFTY/SENSEX
win-rate figure. See the BANKNIFTY guardrail note in `memory/strategy.md` for the exact tracking
requirement.

## 2026-06-29 — real Dhan account onboarding: F&O activation, sandbox token source, fill-price quirk

Onboarding a real Dhan account (needed for sandbox use too) surfaced several things worth knowing
before the next setup or any debugging session:

- **F&O segment activation is a separate step from KYC**, gated by SEBI regulation, not a Dhan
  quirk. "Account ready for trading" emails / general KYC completion does NOT imply F&O is active -
  check Profile > Segments for `F&O` explicitly. Activation needs one income proof: bank statement
  (6 months/180 days, end date within 35 days), ITR (latest AY, income >= Rs1,20,000), or holdings
  statement (>= Rs10,000, latest month). Apply via Profile > Segment Activated > Apply for F&O
  (app) or My Profile > Apply for Investment Products (web). Usually verified within a few hours.
- **Sandbox credentials are NOT the same as the live "DhanHQ Trading APIs" token.** The
  `web.dhan.co` Profile > "DhanHQ Trading APIs" page generates a token for `api.dhan.co` (live) -
  it will fail with `Invalid Token` (DH-906) against `sandbox.dhan.co`. The correct source is the
  **separate DevPortal** at `developer.dhanhq.co` > log in (this requires connecting/linking your
  real Dhan account once - can have OTP/PIN friction the first time, retry in an incognito window
  if repeated "correct" OTP+PIN attempts fail) > **Sandbox** tab > generates its own
  **sandbox Client ID** (different number from your live Client ID) and sandbox access token. Use
  the sandbox Client ID/token pair together - mixing a live Client ID with a sandbox token (or vice
  versa) is the `Invalid Token` failure mode.
- **Dhan's sandbox fills every order at a flat simulated price of 100, regardless of real market
  price** (per Dhan's own sandbox docs). This means even a "real" `averageTradedPrice` read back
  from a sandbox fill is meaningless for credit/P&L tracking - keep using
  `scripts/market_data.py estimate-premium` for all sizing/exit-threshold decisions in sandbox, the
  same as already documented above for the missing-market-data reason, just for a different reason
  now (fills are real numbers but fake economics, not 404s).
- **Order reads (`/orders`, `/orders/{id}`, `/fundlimit`) return confusing generic 500 errors
  (`FUND_LIMIT_ERROR`, `DH-906 "Incorrect request..."`) when called outside actual NSE F&O trading
  hours (9:15 AM-3:30 PM IST, Mon-Fri)**, even though order *placement* itself was accepted (got a
  real orderId, sat at `TRANSIT`). Confirmed via community reports of the same DH-906 message
  actually meaning "market is closed," not an account problem. **Don't conclude something is broken
  from a sandbox API error without first checking whether it's actually market hours** - retest
  during market hours before treating any read-endpoint failure as a real bug. Confirmed fixed:
  re-checked at 2026-06-29 ~10:35 AM IST (markets open) and the exact same order that errored the
  night before now reads back cleanly with `orderStatus: "TRADED"`, `averageTradedPrice: 100.0`
  (the flat sandbox fill price, as expected).
- **Correction to the "closing orders are slow" note above:** the stuck `PENDING`/`TRANSIT` closing
  SELL orders from that earlier test were not a generic slowness quirk - they were attempts to
  close a position in **NIFTY-Jun2026-24000-CE, whose expiry (2026-06-25) had already passed** by
  test time. You cannot trade an expired contract; that's why `drvExpiryDate` looked wrong and why
  the order never filled. These stuck orders also can't be cancelled (`DELETE /orders/{id}` returns
  `DH-906 "Order is in Transit state"` - you can't even cancel a TRANSIT order, only wait it out or
  let it lapse). Lesson: **always confirm the expiry date being traded is still in the future**
  before testing close/SL behavior, not just before opening a position.
- **First paper losing day (2026-07-02): ADX<18 at entry does not rule out a slow directional
  grind that walks price up to the short strike.** Both ICs opened today on clean ADX<18 reads
  (SENSEX 17.09→17.38, NIFTY 15.55) and both finished marginally red at EOD (SENSEX −₹568.80,
  NIFTY −₹61.10, combined −₹629.90) for the *same* reason: spot drifted steadily upward all
  session (NIFTY 24,081→24,175; SENSEX 77,262→77,511) and closed right at / just above each
  upper short (24200 / 77500), so the call side went marginally ITM and the credit didn't decay.
  This is NOT a thesis break and not a reason to change the strategy: VIX stayed low (12.8→12.26),
  the moves were small and grinding (well under the 2-strike OTM buffer's worst case), and the
  defined-risk structure capped exposure — the max-loss cap (~₹4.7k/₹4.2k) was never remotely
  approached; the actual loss was ~₹630, i.e. the shorts just happened to sit where a quiet drift
  landed. The real lesson is calibration, not correction: **a low ADX reading means "not strongly
  trending," it does NOT mean "won't drift" — a slow one-way grind inside a low-ADX regime can
  still pin an at-worst outcome at a near-ATM short.** SENSEX's structure is especially exposed to
  this: 2 strikes = 200 pts ≈ 0.26% OTM on a 77k index, so its shorts sit near-ATM and a ~0.3%
  drift is enough to touch them (this is why SENSEX's loss was ~9× NIFTY's on a similar % move).
  One day is noise vs. the 70-79% backtest win rate — log it, keep the strategy unchanged, and
  watch in the weekly review whether SENSEX's near-ATM shorts underperform NIFTY's structurally
  (if so, a wider SENSEX short offset — 3 strikes OTM — may be worth backtesting, but not on one
  data point).
