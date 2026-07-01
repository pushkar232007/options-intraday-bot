# Portfolio Snapshot

_Last updated: 2026-07-01 ~15:15 IST (EOD square-off: NIFTY IC #1 force-closed for +₹30; flat, no open positions)._

- **Mode:** paper (broker: Dhan Sandbox → migrating to Upstox)
- **Cash (tracked virtual):** ₹1,00,029.90
- **Realized P&L (all-time):** ₹29.90
- **Today's P&L:** +₹29.90 realized (NIFTY IC #1 closed at cost-to-close 71.78 vs 72.01 entry credit).
  Circuit breaker not tripped.

---

## Open Paper Positions

| # | Instrument | Expiry | Short Put | Long Put | Short Call | Long Call | Lots | Entry Credit | Entry Date | DTE at Entry | Broker Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | — | — |

_No open positions — all squared off at EOD._

---

## Closed Paper Positions (all-time)

| # | Instrument | Expiry | Strikes (SP/LP/SC/LC) | Lots | Entry Credit | Exit Cost | Realized P&L | Entry Date | Exit Date | Reason |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NIFTY | 2026-07-07 | 23950/23850/24150/24250 | 2 | 72.01/unit | 71.78/unit | +₹29.90 | 2026-07-01 | 2026-07-01 | EOD_SQUAREOFF |

Position #1 close (2026-07-01 EOD): cost-to-close 71.78/unit via Black-Scholes (spot ~24,008,
VIX 13.3, DTE 6): buy-back SP23950PE 125.50 + SC24150CE 111.20 − sell LP23850PE 87.72 −
LC24250CE 77.20 = 71.78/unit. Realized = (72.01−71.78)×130 = **+₹29.90**. Broker close not
possible (DH-905 blocks current weekly securityIds) — paper close is authoritative.

---

## Notes

**Missed trades (broker blocked, paper position NOT logged at the time — pre-restructure):**
- 2026-07-01 ~09:34 IST: SENSEX ADX 17.09, IC 76600/76400/77000/77200, entry blocked by
  sandbox margin (₹934k locked by expired sid=71472 artifact). Not logged as paper position
  (portfolio.md-first logic not yet deployed at that time).
- 2026-07-01 ~11:43 IST: NIFTY ADX 16.08, IC 23800/23900/24100/24200, 2 lots, ~₹3,637 max
  loss. Blocked by DH-905 (sandbox OMS rejects current weekly securityIds — instrument
  universe appears frozen). Not logged as paper position (same reason — fix not yet deployed).

**Broker status (Dhan sandbox):** Two stacked blockers as of 2026-07-01 make sandbox unusable
— DH-906 margin locked (₹934k utilizedAmount) AND DH-905 unknown securityIds for current
weekly contracts. Migrating to Upstox. Until migration completes, broker column will show
REJECTED but paper positions will be tracked here regardless.

From the next qualifying setup onward, portfolio.md is written FIRST and broker order is
best-effort only.
