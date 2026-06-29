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
   (long put + long call premiums). This is an estimate for sizing/decision purposes only - the
   real credit comes from the actual fill prices in step 7.
6. Size the trade: `python3 scripts/risk.py size-spread --capital <current> --width <strike width> --credit <estimated net credit> --lot-size <current lot size from memory/strategy.md's table>`. If qty_lots is 0, skip - log why.
7. If all checks pass, place all 4 legs: `python3 scripts/dhan.py place-spread --instrument <X> --expiry <date> --short-put <K> --long-put <K> --short-call <K> --long-call <K> --lots <qty>` (this looks up each leg's securityId from Dhan's instrument master itself - if any leg is skipped for "no matching contract found", stop and check the expiry date is actually listed before retrying).
8. **Poll `python3 scripts/dhan.py order-status <orderId>` for each leg until `orderStatus` reads
   `TRADED`** - don't treat the initial response as confirmation. Read each leg's
   `averageTradedPrice` once filled and compute the REAL net credit received from those - this is
   what gets logged and used for exit-threshold tracking, not the step-5 estimate. If any leg
   doesn't fill within a couple of checks, you may be left with a partial position; check `orders`
   and consider unwinding the legs that did fill rather than leaving directional risk on
   accidentally.
9. Log the trade (real net credit, strikes, qty, DTE) to memory/trade-log.md.
10. Send a Telegram notification via scripts/telegram.py only if a trade was actually confirmed `TRADED`.
