Evaluate a candidate setup against every guardrail in memory/strategy.md and execute if it clears
all of them.

1. Confirm ADX(14) < 18 on the instrument right now: `python3 scripts/market_data.py adx <X>`
   (re-check, don't rely on a stale pre-market reading - conditions can change by the time this
   routine fires).
2. Confirm no circuit breaker has tripped today: `python3 scripts/risk.py circuit-breaker --capital <current> --day-pnl <today's running P&L>`.
3. Confirm there isn't already an open position on this instrument (check memory/portfolio.md
   "Open Paper Positions" table — this is the source of truth in TRADING_MODE: paper, not the
   broker).
4. Get the current spot: `python3 scripts/market_data.py spot <X>`. Pick strikes: short legs 2
   strikes OTM, long legs 4 strikes OTM (strike step: NIFTY 50, BANKNIFTY 100, SENSEX 100 per
   memory/strategy.md — re-verify against live instrument master if a `lookup` call comes back
   empty).
5. Estimate the net credit: `python3 scripts/market_data.py estimate-premium <X> <strike>
   <CE|PE> --dte <days>` for each of the 4 legs. Net credit = (short put + short call) - (long
   put + long call). **While TRADING_MODE: paper, this estimate IS the entry credit — it's what
   gets logged, tracked, and used for all exit comparisons.**
6. Size the trade: `python3 scripts/risk.py size-spread --capital <current> --width <strike
   width> --credit <estimated net credit> --lot-size <lot size from memory/strategy.md>`. If
   qty_lots is 0, skip and log why.
7. **Log the paper position to memory/portfolio.md immediately** — add a row to the "Open Paper
   Positions" table with: instrument, expiry, strikes (short put / long put / short call / long
   call), lots, entry credit (step 5 estimate), entry date, DTE. **This happens regardless of
   whether the broker order succeeds or fails.** In TRADING_MODE: paper, portfolio.md is the
   source of truth, not the broker.
8. Attempt the broker order (best-effort only, never blocks the paper trade):
   `python3 scripts/dhan.py place-spread --instrument <X> --expiry <date> --short-put <K>
   --long-put <K> --short-call <K> --long-call <K> --lots <qty>`. If the broker rejects
   (DH-905, DH-906, margin error, or any other error), log the rejection reason in
   memory/trade-log.md but **do not unwind the paper position already written to portfolio.md**.
   When live (TRADING_MODE: live), broker fill is required — if it fails, do NOT write to
   portfolio.md and abort instead.
9. Log the trade to memory/trade-log.md: instrument, expiry, strikes, lots, entry credit (step 5
   estimate), DTE, broker status (FILLED / REJECTED / N/A-paper). Always log even if broker
   rejected — the paper position is real regardless.
10. Send a Telegram notification via `python3 scripts/telegram.py` for every paper position
    logged (not just on broker fill). Message should include instrument, strikes, lots, estimated
    entry credit, and whether broker filled or was rejected.
