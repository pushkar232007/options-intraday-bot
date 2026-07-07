Evaluate a candidate setup against every guardrail in memory/strategy.md and execute if it clears
all of them. Works for both index instruments (NIFTY/BANKNIFTY/SENSEX) and stock F&O symbols.

---

## For index instruments (NIFTY / BANKNIFTY / SENSEX)

1. Confirm ADX(14) < 18 on the instrument right now: `python3 scripts/market_data.py adx <X>`
   (re-check, don't rely on a stale pre-market reading — conditions can change).
2. **Circuit breaker: SKIP this check while TRADING_MODE: paper** — it is disabled in paper
   mode (strategy.md). When live, confirm no circuit breaker has tripped:
   `python3 scripts/risk.py circuit-breaker --capital <current> --day-pnl <today's running P&L>`.
3. Confirm there isn't already an open position on this instrument (check memory/portfolio.md
   "Open Paper Positions" table — source of truth in TRADING_MODE: paper).
4. Get spot: `python3 scripts/market_data.py spot <X>`. Pick strikes: short legs 2 strike steps
   OTM, long legs 4 strike steps OTM (strike step: NIFTY 50, BANKNIFTY 100, SENSEX 100 per
   memory/strategy.md).
5. Estimate net credit: `python3 scripts/market_data.py estimate-premium <X> <strike> <CE|PE>
   --dte <days>` for each of the 4 legs (uses India VIX as IV). Net credit = (short put +
   short call) − (long put + long call).
6. **Size: TRADING_MODE: paper → always 1 lot. Skip the risk.py sizing formula entirely.**
   Most stock lots have a minimum 1-lot exposure that exceeds any % cap on ₹50K paper capital,
   so the formula would skip most trades and break strategy validation. Paper mode = 1 lot always.
   (Capital: ₹4,00,000 paper — for P&L tracking only, not sizing.)
   TRADING_MODE: live only: `python3 scripts/risk.py size-spread --capital <current>
   --width <strike width> --credit <net credit> --lot-size <lot size>`. Skip if qty_lots = 0.

---

## For stock symbols (any symbol from the stock universe in memory/strategy.md)

1. Stock qualifying data comes from `scan-stocks` (already run by the pre-market / intraday
   routine). Pull the stock's `adx14_daily` and `hist_vol_pct` from that output. **Do not
   re-fetch ADX mid-day for stocks** — daily-bar ADX doesn't change intraday, use the
   morning scan reading.
2. **Circuit breaker: SKIP while TRADING_MODE: paper** (disabled in paper mode). When live only:
   confirm no circuit breaker has tripped today (same check as index step 2 above).
3. Confirm no open position on this stock symbol in memory/portfolio.md.
4. **Check earnings:** never enter a stock iron condor if the company reports earnings within
   5 days of the chosen expiry. Skip and log reason if so.
5. Find expiry: target DTE 2-30 days (monthly expiry only — last Thursday of month; no stock
   weeklies exist in India). Look up available expiries via
   `python3 scripts/dhan.py lookup <SYMBOL> <nearest-expiry> <approx-atm-strike> CE` — try
   available monthly expiries to find one with DTE 2-30.
6. Get strike step and lot size from the lookup result above (the instrument master has exact
   values — do NOT guess).
7. Get spot: use `hist_vol_pct` from the scan output, and estimate net credit:
   `python3 scripts/market_data.py estimate-premium <SYMBOL> <strike> <CE|PE> --dte <days>
   --iv <hist_vol_pct>` for each of the 4 legs.
8. **Size: TRADING_MODE: paper → always 1 lot** (same reason as index step 6 above).
   TRADING_MODE: live only: `python3 scripts/risk.py size-spread --capital <current>
   --width <strike width> --credit <net credit> --lot-size <lot size from step 6>`.
   Skip if qty_lots = 0.

---

## Steps 7-10 apply to both index and stock trades

7. **Log the paper position to memory/portfolio.md immediately** — add a row to the "Open Paper
   Positions" table with: instrument, expiry, strikes (short put / long put / short call / long
   call), lots, entry credit (step 5/7 estimate), entry date, DTE.
   **This happens regardless of whether the broker order succeeds or fails.**
   In TRADING_MODE: paper, portfolio.md is the source of truth, not the broker.
8. Attempt the broker order (best-effort only, never blocks the paper trade):
   `python3 scripts/dhan.py place-spread --instrument <X> --expiry <date> --short-put <K>
   --long-put <K> --short-call <K> --long-call <K> --lots <qty>`. If the broker rejects,
   log the rejection reason in memory/trade-log.md but **do not unwind the paper position**.
   When live (TRADING_MODE: live), broker fill is required — abort if it fails.
9. Log the trade to memory/trade-log.md: instrument, expiry, strikes, lots, entry credit,
   DTE, broker status (FILLED / REJECTED / N/A-paper). Always log even if broker rejected.
10. Send a Telegram notification via `python3 scripts/telegram.py` for every paper position
    logged. Message should include instrument, strikes, lots, estimated entry credit, and
    whether broker filled or was rejected.
