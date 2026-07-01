# Portfolio Snapshot

_Last updated: 2026-07-01 intraday-monitor (mid-session re-fire; broker-verified via funds/orders)._

- **Mode:** paper (Dhan Sandbox)
- **Cash (tracked virtual):** ₹1,00,000.00
- **Open positions:** none. (The net +130 long on NIFTY-Jun2026-24000-CE in the Dhan account is a
  pre-existing sandbox test artifact on an already-expired contract — expiry 2026-06-25 — not a
  strategy position. Its closing SELLs keep getting REJECTED ("Fund Limit Insufficient"), so it
  simply lapses. See trade-log.)
- **Realized P&L (all-time):** ₹0.00
- **Today's P&L:** ₹0.00
- **⚠️ Sandbox margin blocker (new, 2026-07-01):** Dhan sandbox `availableBalance` is only
  **₹65,301.12** (`utilizedAmount` ₹934,698 locked by the un-clearable expired sid=71472 artifact).
  This is far below what a naked short leg needs, so `place-spread` (which leads with the naked
  SELL leg) gets rejected DH-906 — the first qualifying setup (SENSEX, 2026-07-01) could NOT be
  entered because of this. Needs a sandbox account reset/top-up and/or a place-spread leg-ordering
  fix (long legs first) before the next qualifying setup can actually execute. See trade-log
  2026-07-01.
