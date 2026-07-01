# Portfolio Snapshot

_Last updated: 2026-07-01 ~11:43 IST intraday-monitor (broker-verified via funds/orders)._

- **Mode:** paper (Dhan Sandbox)
- **Cash (tracked virtual):** ₹1,00,000.00
- **Open positions:** none. (The net +130 long on NIFTY-Jun2026-24000-CE in the Dhan account is a
  pre-existing sandbox test artifact on an already-expired contract — expiry 2026-06-25 — not a
  strategy position. Its closing SELLs keep getting REJECTED ("Fund Limit Insufficient"), so it
  simply lapses. See trade-log.)
- **Realized P&L (all-time):** ₹0.00
- **Today's P&L:** ₹0.00
- **⚠️ TWO stacked sandbox blockers preventing ALL execution (2026-07-01):** a valid qualifying setup
  (NIFTY, ADX 16.08, sized 2 lots / ₹3,637 max loss) could NOT be entered at ~11:43 IST. Both must be
  cleared by a **Dhan sandbox account reset** before any setup can execute:
  1. **DH-906 margin:** `availableBalance` only **₹65,301.12** (`utilizedAmount` ₹934,698 locked by the
     un-clearable expired sid=71472 artifact). The place-spread leg-ordering fix (long legs first) is
     now in `dhan.py`, but margin is still short.
  2. **DH-905 unknown contracts (NEW, the deeper blocker):** the sandbox OMS rejects the newly-listed
     NIFTY 2026-07-07 securityIds (valid in Dhan's published master, but "bad values" to the sandbox) —
     both BUY and SELL, all 4 legs. The expired sid=71472 by contrast passes input validation. The
     sandbox's tradable instrument universe appears frozen and excludes current weekly expiries.
     **Margin top-up alone will NOT fix this — a full sandbox reset (fresh instrument set) is needed.**
  See trade-log 2026-07-01 ~11:43 IST.
