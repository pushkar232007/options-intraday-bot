# Weekly Review

Performance vs. backtest expectations (~8-9 trades/month combined, ~70-79% win rate in backtest),
graded honestly each week. Flag drift from backtest expectations as a signal to slow down and
investigate — not as an automatic trigger to change `memory/strategy.md`.

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

