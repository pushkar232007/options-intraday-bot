Refresh memory/portfolio.md and log learnings.

1. `python3 scripts/dhan.py funds` and `python3 scripts/dhan.py positions` for the current
   account/positions snapshot.
2. Rewrite memory/portfolio.md with: cash, open positions (if any), realized P&L all-time, and
   today's P&L. Keep it short - this file should always reflect *current* state, not history.
3. If anything today contradicted backtest expectations (memory/strategy.md's ~70-79% win rate,
   ~8-9 trades/month), or taught a genuinely new lesson, append a dated entry to
   memory/signals-learnings.md. Don't log routine/expected outcomes here - only surprises.
4. In weekly mode (called from the weekly-review routine): also tally the week's trade count,
   win rate, and P&L from memory/trade-log.md, and write a dated entry to memory/weekly-review.md
   comparing it to backtest expectations.
