# Portfolio Snapshot

_Last updated: 2026-07-02 ~later intraday IST (both ICs HELD — SENSEX #2 ≈ −₹584, NIFTY #3 ≈ −₹65; 2 open positions; BANKNIFTY qualified on ADX but skipped — 26 DTE)._

- **Mode:** paper (broker: Dhan Sandbox — switching to Dhan Live when ready for real trading)
- **Cash (tracked virtual):** ₹1,00,029.90 (unchanged — paper cash updates on close with realized P&L)
- **Realized P&L (all-time):** ₹29.90
- **Today's P&L:** ₹0 realized so far (2 open ICs; unrealized ≈ −₹584 SENSEX #2 at cost-to-close 165.99/unit, ≈ −₹65 NIFTY #3 at cost-to-close 68.25/unit → combined ≈ −₹649). Circuit breaker not tripped.

---

## Open Paper Positions

| # | Instrument | Expiry | Short Put | Long Put | Short Call | Long Call | Lots | Entry Credit | Entry Date | DTE at Entry | Broker Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | SENSEX | 2026-07-09 | 77100 | 76900 | 77500 | 77700 | 6 (120 qty) | 161.12/unit | 2026-07-02 | 7 | REJECTED (DH-906 BSE conn.) |
| 3 | NIFTY | 2026-07-07 | 24000 | 23900 | 24200 | 24300 | 2 (130 qty) | 67.75/unit | 2026-07-02 | 5 | REJECTED (DH-905 unknown sid) |

**Exit levels for IC #2:** PROFIT_TARGET cost-to-close ≤ 80.56/unit; SL ≥ 322.24/unit; else forced EOD square-off.
Max defined loss 6×(200−161.12)×20 = ₹4,665.60 (≤5% cap). Credit collected 161.12×120 = ₹19,334.40.

**Exit levels for IC #3:** PROFIT_TARGET cost-to-close ≤ 33.88/unit; SL ≥ 135.50/unit; else forced EOD square-off.
Max defined loss 2×(100−67.75)×65 = ₹4,192.50 (≤5% cap). Credit collected 67.75×130 = ₹8,807.50.

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
weekly contracts. Broker column will show REJECTED but paper positions are tracked here
regardless — broker is best-effort only in paper mode. When switching to real trading,
live Dhan credentials (Client ID 1112363387, api.dhan.co) replace sandbox credentials.

From the next qualifying setup onward, portfolio.md is written FIRST and broker order is
best-effort only.
