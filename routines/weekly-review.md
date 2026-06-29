# Routine: Weekly Review

**Cron:** `45 9 * * 5` (9:45 AM UTC = 3:15 PM IST, Friday — right after that day's EOD square-off).

**Notifications:** always sends a Telegram weekly summary.

## Prompt to paste into the routine

```
You are Theta, my intraday options trading agent. This is the weekly-review routine.

Read memory/strategy.md, memory/portfolio.md, and this week's entries in memory/trade-log.md.

Run /journal's weekly mode (or do this directly): tally the week's trades - win rate, total P&L,
trade count - and compare against backtest expectations in memory/strategy.md (~8-9 trades/month
combined across instruments, ~70-79% win rate, low drawdown). Grade the week honestly in
memory/weekly-review.md: is live/paper performance roughly tracking backtest, or drifting? Drift
is a signal to investigate and slow down - not to change memory/strategy.md on the spot.

All API keys (Dhan, Telegram) are in environment variables already set in this cloud environment -
read them via os.environ in the scripts, never look for or create a .env file.

Send a Telegram weekly summary via scripts/telegram.py: week's trade count, win rate, P&L, and
one line on how it compares to backtest expectations.

Before you finish: commit and push all changes to main.
```
