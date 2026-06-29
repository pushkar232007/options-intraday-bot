Evaluate a candidate setup against every guardrail in memory/strategy.md and execute if it clears
all of them.

1. Confirm ADX(14) < 18 on the instrument right now (re-check, don't rely on a stale pre-market
   reading - conditions can change by the time this routine fires).
2. Confirm no circuit breaker has tripped today: `python3 scripts/risk.py circuit-breaker --capital <current> --day-pnl <today's running P&L>`.
3. Confirm there isn't already an open position on this instrument (check memory/portfolio.md).
4. Pick strikes: short legs 2 strikes OTM, long legs 4 strikes OTM (strike step: NIFTY 50,
   BANKNIFTY 100, SENSEX 100 - confirm against the live Dhan option chain's actual strike spacing).
5. Size the trade: `python3 scripts/risk.py size-spread --capital <current> --width <strike width> --credit <net credit from chain> --lot-size <current lot size>`. If qty_lots is 0, skip - log why.
6. If all checks pass, place all 4 legs: `python3 scripts/dhan.py place-spread --instrument <X> --expiry <date> --short-put <K> --long-put <K> --short-call <K> --long-call <K> --lots <qty>`.
7. Log the trade (or the skip and why) to memory/trade-log.md.
8. Send a Telegram notification via scripts/telegram.py only if a trade was actually placed.
