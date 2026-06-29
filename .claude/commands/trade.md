Evaluate a candidate setup against every guardrail in memory/strategy.md and execute if it clears
all of them.

1. Confirm ADX(14) < 18 on the instrument right now (re-check, don't rely on a stale pre-market
   reading - conditions can change by the time this routine fires).
2. Confirm no circuit breaker has tripped today: `python3 scripts/risk.py circuit-breaker --capital <current> --day-pnl <today's running P&L>`.
3. Confirm there isn't already an open position on this instrument (check memory/portfolio.md).
4. Pick strikes: short legs 2 strikes OTM, long legs 4 strikes OTM (strike step verified in
   memory/strategy.md's table: NIFTY 50, BANKNIFTY 100, SENSEX 100 - re-verify against the live
   Dhan instrument master if a `lookup` call comes back empty, steps do get revised).
5. Size the trade: `python3 scripts/risk.py size-spread --capital <current> --width <strike width> --credit <net credit from chain> --lot-size <current lot size from memory/strategy.md's table>`. If qty_lots is 0, skip - log why.
6. If all checks pass, place all 4 legs: `python3 scripts/dhan.py place-spread --instrument <X> --expiry <date> --short-put <K> --long-put <K> --short-call <K> --long-call <K> --lots <qty>` (this looks up each leg's securityId from Dhan's instrument master itself - if any leg is skipped for "no matching contract found", stop and check the expiry date is actually listed before retrying).
7. **Poll `python3 scripts/dhan.py order-status <orderId>` for each leg until `orderStatus` reads
   `TRADED`** - don't treat the initial response as confirmation. If any leg doesn't fill within a
   couple of checks, you may be left with a partial position; check `orders` and consider
   unwinding the legs that did fill rather than leaving directional risk on accidentally.
8. Log the trade (or the skip and why) to memory/trade-log.md.
9. Send a Telegram notification via scripts/telegram.py only if a trade was actually confirmed `TRADED`.
