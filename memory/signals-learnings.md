# Signals & Learnings

## 2026-06-29 — naked option buying rejected, credit spreads adopted (pre-launch backtest)

Before this bot ever placed a paper trade, six versions of naked directional option-buying were
backtested (in `~/Projects/options-backtest`) and rejected:

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
