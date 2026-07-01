# Portfolio Snapshot

_Last updated: 2026-07-01 (command files restructured — portfolio.md is now the source of truth
for all paper positions, not the broker. Broker orders are best-effort only in TRADING_MODE: paper)._

- **Mode:** paper (broker: Dhan Sandbox → migrating to Upstox)
- **Cash (tracked virtual):** ₹1,00,000.00
- **Realized P&L (all-time):** ₹0.00
- **Today's P&L:** ₹0.00

---

## Open Paper Positions

| # | Instrument | Expiry | Short Put | Long Put | Short Call | Long Call | Lots | Entry Credit | Entry Date | DTE at Entry | Broker Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | — | — |

_No open positions._

---

## Closed Paper Positions (all-time)

| # | Instrument | Expiry | Strikes (SP/LP/SC/LC) | Lots | Entry Credit | Exit Cost | Realized P&L | Entry Date | Exit Date | Reason |
|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | — |

_No closed positions yet._

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
