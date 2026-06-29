# Theta — Intraday Options Trading Agent

A 24/7 Claude Code routine that sells defined-risk credit spreads (iron condors) on Nifty,
BankNifty, and Sensex weekly options, intraday only. Same pattern as the
[`trading-routine`](https://github.com/pushkar232007/trading-routine) Alpaca bot: a `CLAUDE.md`
persona file, `memory/` for persistent state, `scripts/` for thin API wrappers, and `routines/*.md`
documenting the cron schedule + prompt pasted into Claude Desktop's Routines UI.

## Why credit spreads, not naked option buying

The original idea was buying cheap options for big quick payoffs. Six backtested versions of that
(in [`backtest/`](backtest/)) all failed once tested on a large enough sample. Selling defined-risk
spreads on range-bound days (ADX < 18) backtested profitably across every timeframe and expiry
tested instead. Full account in [`memory/signals-learnings.md`](memory/signals-learnings.md) and
the strategy itself in [`memory/strategy.md`](memory/strategy.md) — read those before changing
anything. To rerun or extend the backtest: `cd backtest && python3 fetch_data.py && python3
backtest_spreads.py --strategy strategy_spread_v1` (data/ is gitignored — regenerate it locally).

## Setup

1. **Dhan Sandbox account.** Sign up at developer.dhanhq.co (no funded live account or KYC
   required for sandbox) and get `DHAN_CLIENT_ID` / `DHAN_ACCESS_TOKEN` (30-day validity — you'll
   need to regenerate and update the env var monthly until this is automated).
   `scripts/dhan.py`'s order/fund/position functions were verified end-to-end against a real
   sandbox account on 2026-06-29 (see `memory/signals-learnings.md` for what got fixed along the
   way). Its `option-chain`/`quote` functions are still untested — the sandbox returns 404 on all
   market-data paths; those need a live account + the paid Data API subscription (~₹499/month).
2. **Telegram bot.** Same steps as documented in `scripts/telegram.py`'s docstring.
3. **Set environment variables** in the Claude Code routine's cloud environment (see
   `.env.example` for the full list) — never in a committed `.env` file.
4. **GitHub repo + push access.** Create `pushkar232007/options-intraday-bot` (private by
   default — see the note in the original plan about why `trading-routine` had to go public; only
   flip this one public if Claude Desktop's repo picker forces it the same way). Add a `GH_TOKEN`
   PAT if the routine's built-in GitHub integration turns out to be push-restricted.
5. **Wire up the routines.** In Claude Desktop → Routines, create one routine per file in
   `routines/`, using that file's cron schedule and pasted prompt.

## Local testing (no live credentials needed)

```
python3 scripts/risk.py size-spread --capital 100000 --width 200 --credit 130 --lot-size 65
python3 scripts/dhan.py --help
```

Once sandbox credentials are set:

```
python3 scripts/dhan.py funds
python3 scripts/dhan.py lookup NIFTY 2026-06-30 24000 CE
python3 scripts/telegram.py "test message"
```
