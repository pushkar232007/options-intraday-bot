# Portfolio Snapshot

_Last updated: 2026-07-08 intraday-monitor (sell-off run) — flat, 0 open positions, 0 trades; day P&L ₹0. No-trade: risk-off day, all three indices trending HARDER (NIFTY/BANKNIFTY/SENSEX ADX 50.14/42.63/46.53) as spot sold off ~1.3-1.9% and VIX spiked 12.24→15.1; 18 stock qualifiers (ADX<18, daily/static intraday) still all earnings-blocked — only in-range expiry Jul 30 monthly (22 DTE) collides with Q1 season, no name reports cleanly. Capital ₹4,00,000; realized P&L from reset: ₹0._

- **Mode:** paper (broker: Dhan Sandbox — switching to Dhan Live when ready for real trading)
- **Cash (tracked virtual):** ₹4,00,000.00 ← reset 2026-07-07 by Pushkar; covers full strategy margin (3 index condors ₹1.6L–2.2L + multiple simultaneous stock condors ₹1L–2L). Previous balance was ₹2,00,000.
- **Realized P&L (from reset):** ₹0.00
- **Position sizing:** 1 lot per trade (paper mode — sizing formula skipped, would block most stock trades)
- **Circuit breaker:** DISABLED in paper mode — no daily loss cap, run all day regardless of P&L.
- **Today's P&L:** ₹0 (2026-07-08 — no trades)

---

## Open Paper Positions

_None — flat (0 open positions; last ICs squared off at EOD 2026-07-02, no positions opened since)._

---

## Closed Paper Positions (all-time)

| # | Instrument | Expiry | Strikes (SP/LP/SC/LC) | Lots | Entry Credit | Exit Cost | Realized P&L | Entry Date | Exit Date | Reason |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NIFTY | 2026-07-07 | 23950/23850/24150/24250 | 2 | 72.01/unit | 71.78/unit | +₹29.90 | 2026-07-01 | 2026-07-01 | EOD_SQUAREOFF |
| 2 | SENSEX | 2026-07-09 | 77100/76900/77500/77700 | 6 | 161.12/unit | 165.86/unit | −₹568.80 | 2026-07-02 | 2026-07-02 | EOD_SQUAREOFF |
| 3 | NIFTY | 2026-07-07 | 24000/23900/24200/24300 | 2 | 67.75/unit | 68.22/unit | −₹61.10 | 2026-07-02 | 2026-07-02 | EOD_SQUAREOFF |

Position #2 close (2026-07-02 EOD): cost-to-close 165.86/unit via Black-Scholes (spot ~77,511,
VIX 12.26, DTE 7): buy-back SP77100PE 313.73 + SC77500CE 572.17 − sell LP76900PE 247.89 −
LC77700CE 472.15 = 165.86/unit. Realized = (161.12−165.86)×120 = **−₹568.80**. Spot drifted to
77,511, just above the 77500 upper short (call side went slightly ITM). Neither profit target
(≤80.56) nor SL (≥322.24) hit → forced EOD square-off. Broker close not possible (DH-906 BSE
connectivity / DH-905) — paper close is authoritative.

Position #3 close (2026-07-02 EOD): cost-to-close 68.22/unit via Black-Scholes (spot ~24,175,
VIX 12.26, DTE 5): buy-back SP24000PE 61.03 + SC24200CE 137.64 − sell LP23900PE 36.95 −
LC24300CE 93.50 = 68.22/unit. Realized = (67.75−68.22)×130 = **−₹61.10**. Spot 24,175 sat just
above the 24200 upper short. Neither profit target (≤33.88) nor SL (≥135.50) hit → forced EOD
square-off. Broker close not possible (DH-905) — paper close is authoritative.

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
