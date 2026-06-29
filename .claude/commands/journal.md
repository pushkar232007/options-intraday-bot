Refresh memory/portfolio.md and log learnings.

1. `python3 scripts/dhan.py funds` and `python3 scripts/dhan.py orders` for the current
   account/positions snapshot (don't use `positions` - confirmed unreliable in sandbox, see
   memory/signals-learnings.md; derive open positions from `orders` filtered to `TRADED`).
2. Rewrite memory/portfolio.md with: cash, open positions (if any), realized P&L all-time, and
   today's P&L. Keep it short - this file should always reflect *current* state, not history.
3. If anything today contradicted backtest expectations (memory/strategy.md's NIFTY/SENSEX
   ~70-79% win rate), or taught a genuinely new lesson, append a dated entry to
   memory/signals-learnings.md. Don't log routine/expected outcomes here - only surprises.
4. In weekly mode (called from the weekly-review routine): tally NIFTY and SENSEX trades together
   (the validated pair) for one win-rate/P&L figure, and tally BANKNIFTY **separately** - it's
   unvalidated and must not be blended into the validated pair's numbers (see memory/strategy.md).
   Note BANKNIFTY's DTE-at-entry spread too (how many were near-expiry vs. far) since that's the
   actual open question being tracked. Write a dated entry to memory/weekly-review.md with both
   figures clearly separated.
