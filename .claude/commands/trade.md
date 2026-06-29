Evaluate a candidate setup against every guardrail in memory/strategy.md and execute if it clears
all of them.

1. Confirm ADX(14) < 18 on the instrument right now: `python3 scripts/market_data.py adx <X>`
   (re-check, don't rely on a stale pre-market reading - conditions can change by the time this
   routine fires).
2. Confirm no circuit breaker has tripped today: `python3 scripts/risk.py circuit-breaker --capital <current> --day-pnl <today's running P&L>`.
3. Confirm there isn't already an open position on this instrument (check memory/portfolio.md).
4. Get the current spot: `python3 scripts/market_data.py spot <X>`. Pick strikes: short legs 2
   strikes OTM, long legs 4 strikes OTM (strike step verified in memory/strategy.md's table:
   NIFTY 50, BANKNIFTY 100, SENSEX 100 - re-verify against the live Dhan instrument master if a
   `lookup` call comes back empty, steps do get revised).
5. Estimate the net credit (Dhan's sandbox has no live option-chain - see
   memory/signals-learnings.md): `python3 scripts/market_data.py estimate-premium <X> <strike>
   <CE|PE> --dte <days>` for each of the 4 legs, net credit = (short put + short call premiums) -
   (long put + long call premiums). While `TRADING_MODE: paper`, this estimate IS the number to
   log and track exits against - see step 8, sandbox fills don't carry real prices. Once live,
   this estimate becomes sizing-only and the real fill price from step 8 takes over.
6. Size the trade: `python3 scripts/risk.py size-spread --capital <current> --width <strike width> --credit <estimated net credit> --lot-size <current lot size from memory/strategy.md's table>`. If qty_lots is 0, skip - log why.
7. If all checks pass, place all 4 legs: `python3 scripts/dhan.py place-spread --instrument <X> --expiry <date> --short-put <K> --long-put <K> --short-call <K> --long-call <K> --lots <qty>` (this looks up each leg's securityId from Dhan's instrument master itself - if any leg is skipped for "no matching contract found", stop and check the expiry date is actually listed before retrying).
8. **Poll `python3 scripts/dhan.py order-status <orderId>` for each leg until `orderStatus` reads
   `TRADED`** - don't treat the initial response as confirmation. If any leg doesn't fill within a
   couple of checks, you may be left with a partial position; check `orders` and consider
   unwinding the legs that did fill rather than leaving directional risk on accidentally.
   **While `TRADING_MODE: paper` (sandbox): do NOT use `averageTradedPrice` as the real net
   credit.** Dhan's sandbox fills every order at a flat simulated price of 100 regardless of real
   market price (confirmed via Dhan's own docs) - the fill is real, the price is fake. Keep using
   the step-5 estimate as the logged credit and exit-threshold baseline until `TRADING_MODE` flips
   to `live`; only then switch to the real `averageTradedPrice` (and flag that switch in
   memory/signals-learnings.md when it happens).
9. Log the trade (net credit per step 5/8 above, strikes, qty, DTE) to memory/trade-log.md.
10. Send a Telegram notification via scripts/telegram.py only if a trade was actually confirmed `TRADED`.
