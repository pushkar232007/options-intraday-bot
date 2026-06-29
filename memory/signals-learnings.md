# Signals & Learnings

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
