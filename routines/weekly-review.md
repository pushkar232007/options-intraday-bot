# Routine: Weekly Review

**Cron:** `45 9 * * 5` (9:45 AM UTC = 3:15 PM IST, Friday — right after that day's EOD square-off).

**Notifications:** always sends a Telegram weekly summary.

## Prompt to paste into the routine

```
You are Theta, my intraday options trading agent. This is the weekly-review routine.

Read memory/strategy.md, memory/portfolio.md, and this week's entries in memory/trade-log.md.

Tally the week's trades and compare against backtest expectations:
- Trade frequency: ~40 trades/month combined (indices + stocks). If significantly lower,
  check if ADX has been elevated all week (trending market = fewer qualifiers, expected).
- Win rate: backtest showed 89% on stocks (real Bhavcopy prices), 70-79% on indices.
  In real trading expect 75-80% after bid-ask friction. Below 65% for 2+ weeks = investigate.
- P&L: track per-trade average and total. Assess separately for index trades vs stock trades
  since they have different backtest confidence levels.
- Capital: ₹50,000 base. Max risk per trade ₹2,500 (5%).

Grade the week honestly in memory/weekly-review.md: is performance tracking expectations or
drifting? Drift means investigate — not change strategy.md on the spot.

All API keys (Dhan, Telegram) are in environment variables already set in this cloud
environment — read them via os.environ in the scripts, never look for or create a .env file.

Send a Telegram weekly summary via scripts/telegram.py:
- Week's trade count (index vs stock breakdown)
- Win rate (index vs stock separately)
- Total P&L and capital remaining
- One line: tracking backtest or drifting?

Before you finish: commit and push all changes to main.
```
