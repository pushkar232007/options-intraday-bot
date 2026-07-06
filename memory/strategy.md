# Strategy & Guardrails

_Last updated: 2026-07-06 — stock universe unlocked for paper trading after Bhavcopy backtest
(89% WR, 248 days, 445 trades). Original index strategy unchanged._

## Mode

- `TRADING_MODE: paper` (Dhan Sandbox) — do not flip to `live` without Pushkar explicitly asking
  for it here.
- Broker: Dhan (DhanHQ), Sandbox mode. ₹1,00,000 starting virtual balance.

## Thesis (validated by backtest — see `backtest/` in this repo)

**Sell defined-risk credit spreads (iron condors) on Nifty/BankNifty/Sensex weekly options,
on days that read as range-bound/low-volatility — do not buy naked options for direction.**

This is the opposite of the original instinct ("buy cheap options for big quick payoffs").
Six versions of naked directional option-buying (opening-range breakout, mean-reversion fade,
ADX-gated breakout, multiple timeframes 1h/15m/5m, multiple days-to-expiry) were backtested and
**all failed** on a large, honest sample (491 trading days via hourly bars) — simple technical
signals don't predict index option moves precisely enough to overcome low win rate + theta decay.
See `memory/signals-learnings.md` for the full account — don't re-litigate this without new
evidence; re-deriving it from scratch wastes a routine's context budget.

Credit spreads, by contrast, were profitable across **every tested DTE (1-6) and every tested
timeframe (1h/15m/5m)** — the first approach to show that kind of cross-parameter consistency
instead of sign-flipping noise. That consistency is the actual signal that this is a real,
structural edge (the volatility risk premium: index option IV tends to run a bit above realized
vol on average) rather than a lucky backtest window.

**Backtest caveat — read this before getting overconfident:** real historical option-chain data
isn't freely available, so the backtest simulated premiums via Black-Scholes from real index price
+ real India VIX, not real bid/ask option quotes. The 2-year backtest window included moderate
stress (VIX up to 28, a few ±3-4% single-day moves) and stayed profitable through it, but **no
true tail event** (2020-COVID-level, VIX 80+, ±8-13% days) occurred in that window. The defined-risk
spread structure plus the daily circuit breaker below are designed to cap damage in such a day,
but that protection is untested in backtest, not proven.

## Hard guardrails (never violate these)

- **Instruments:** NIFTY, BANKNIFTY, SENSEX all trade. **Nifty 50 F&O stock options are now
  also approved for paper trading** — backtested on real NSE Bhavcopy prices (248 days, 89% WR,
  445 trades). See the "Stock universe" section below for the full list, blocklist, and
  stock-specific guardrails. Scan daily via `python3 scripts/market_data.py scan-stocks`.
  **NIFTY and SENSEX are validated** (large backtest sample, robust across every DTE 1-6 and
  timeframe tested — see `memory/signals-learnings.md`). **BANKNIFTY is NOT validated and trades
  in a data-gathering capacity, not a proven-edge one** — re-backtested 2026-06-29 against its
  real monthly expiry calendar (it no longer has weekly options, confirmed against Dhan's
  instrument master) and came back roughly breakeven (+₹1,166 over ~10 months, 31 trades), with
  the trade-level detail showing that's mostly noise (29 of 31 trades drift to EOD with tiny P&L;
  the only two trades with real magnitude were both right before expiry and nearly cancelled each
  other out). A tighter near-the-money structure tuned for its slower long-dated decay was tested
  and made it slightly *worse*, not better — so this isn't a quick-fix situation, it's a data
  problem: there's only a couple of genuine near-expiry data points in the whole window.
  **Decision: trade BANKNIFTY anyway since this is paper money (`TRADING_MODE: paper`), using the
  same structure as NIFTY/SENSEX below, specifically to accumulate real near-expiry data points
  over time.** Tag every BANKNIFTY entry in `memory/trade-log.md` with its DTE-at-entry, and in
  weekly/monthly reviews assess BANKNIFTY's results separately from NIFTY/SENSEX — don't blend them
  into one combined win-rate figure, since BANKNIFTY's sample is known-thin and shouldn't quietly
  inflate or deflate confidence in the validated pair. Revisit whether BANKNIFTY has earned a
  "validated" status once it has accumulated enough of its own near-expiry (≤7 DTE) trades to judge.
- **Structure:** iron condor — sell a put 2 strikes OTM + sell a call 2 strikes OTM, buy a put 4
  strikes OTM + buy a call 4 strikes OTM. Strike step and lot size (verified 2026-06-29 against
  Dhan's instrument master, re-verify periodically as these get revised by the exchange):
  | Instrument | Strike step | Lot size | Index securityId (segment IDX_I) |
  |---|---|---|---|
  | NIFTY | 50 | 65 | 13 |
  | BANKNIFTY | 100 | 30 | 25 |
  | SENSEX | 100 | 20 | 51 |
  Per-contract option securityIds are NOT static like the index IDs above — look them up fresh via
  `python3 scripts/dhan.py lookup <underlying> <expiry> <strike> <CE|PE>` each time, which reads
  Dhan's published instrument master (`scripts/dhan.py` caches it locally; pass `--refresh` if a
  contract isn't found, e.g. after a new expiry has listed).
- **Entry trigger:** only enter when ADX(14) on the entry timeframe reads **below 18** (range-bound/
  chop reading) shortly after the open, once the opening range has printed. Do not enter on a day
  ADX reads as trending — that's exactly the regime this strategy is not designed for.
- **Expiry to trade:** prefer ~2 days to expiry at entry (backtest: best balance of return vs.
  drawdown — DTE=1 had the highest raw return but ~24% max drawdown in backtest; DTE=3+ had
  meaningfully lower drawdown for less return). Avoid trading options expiring same-day if spreads/
  liquidity look thin in the actual Dhan option chain — gamma risk and bid-ask cost near expiry are
  real execution costs the backtest can't see.
- **Position sizing:**
  - **TRADING_MODE: paper → always 1 lot per trade.** No capital-based sizing in paper mode.
    Most stock F&O lots have a minimum 1-lot exposure well above any % cap on paper capital,
    which would skip most trades and defeat the point of paper trading as strategy validation.
    The backtest was lot-size agnostic (assumed every qualifying trade is taken) — paper mode
    matches that assumption: 1 lot, every qualifying setup.
  - **TRADING_MODE: live → 5% of capital per trade**, sized by the spread's own defined max loss
    `(strike width - net credit received) × lot size`. Skip if qty_lots = 0.
- **Paper capital: ₹2,00,000** — reflects realistic live-trading margin requirements
  (NIFTY+BANKNIFTY+SENSEX condors need ₹1.6L–2.2L SPAN margin alone). Used only for P&L
  tracking and return % calculations, not for trade sizing.
- **Daily loss circuit breaker:** DISABLED in `TRADING_MODE: paper` — paper trading is for
  learning, not capital protection, so let every setup run regardless of daily P&L. Re-enable
  at 10% of capital when switching to live trading.
- **Exit rule (whichever hits first):**
  **Index iron condors (NIFTY / BANKNIFTY / SENSEX — intraday):**
  1. Profit target: close once cost-to-close decays to 50% of entry credit.
  2. Stop-loss: close if cost-to-close grows to 2x entry credit.

  **Stock iron condors (Nifty 50 F&O — held 2-7 days):**
  1. Profit target: close once cost-to-close decays to 25% of entry credit (i.e. 75% of
     premium captured). Backtest sweep showed 75% target outperforms 50% for multi-day holds
     — theta has more time to work, no reason to exit early.
  2. Stop-loss: close if cost-to-close grows to 2.5x entry credit. Sweep showed 2.5x SL
     gives 92.4% WR and +₹3,187 vs 89% WR and +₹2,577 at 2.0x — wider SL avoids false
     exits from normal multi-day noise while theta decays the position.
  3. **EOD rule for stocks: carry forward by default.** The backtest holds positions for
     multiple days — that is where the edge comes from. Do NOT force-close stock condors at
     EOD just because the day is ending. Close a stock condor only when one of these
     triggers fires:
     (a) Profit target hit (cost-to-close ≤ 25% of entry credit) — close immediately.
     (b) SL hit (cost-to-close ≥ 2.5x entry credit) — close immediately.
     (c) Expiry day — close by 3:15 PM IST on the expiry date, not before.
     (d) Earnings announced within 5 days of expiry (identified post-entry) — close to avoid
         IV spike; log reason.
     A stock condor that is slightly down on day 1 is normal — theta needs multiple days to
     work. Do NOT close it just because it is not profitable yet. This is the entire premise
     of the multi-day hold backtest (92.4% WR assumed carries across days, not within hours).
  **Sandbox-verified quirk, do not skip this:** a closing order is NOT guaranteed to fill quickly.
  In testing, a BUY filled in ~3 seconds but the matching closing SELL on the same contract sat in
  `PENDING` (filledQty 0) for over a minute and never filled — the order's own `drvExpiryDate` field
  showed a date 4 days in the past relative to the test date, which may be why. **After placing any
  square-off order, poll `python3 scripts/dhan.py order-status <id>` and confirm `orderStatus` is
  actually `TRADED` before considering the position closed — do not assume a `TRANSIT` response
  means done.** If a square-off order is still stuck after a couple of checks, alert via Telegram
  rather than silently moving on. Also: `/positions` returned empty even right after a confirmed
  fill in testing — track open positions from `orders` (filter `orderStatus == TRADED`, net BUY/SELL
  qty per securityId), not from `/positions`.
- **Expected trade frequency:** ~8-9 trades/month from indices alone; ~40 trades/month combined
  once stock scanning is active (backtest: 248 trading days, 445 trades, 89% WR on real Bhavcopy
  prices). Don't loosen the ADX threshold to manufacture more trades — the 18.0 threshold is
  validated; changing it requires a new backtest.

## Stock universe (Nifty 50 F&O scanner)

Rather than trading a fixed list of stocks, the bot scans the entire Nifty 50 F&O universe
daily and enters iron condors on whichever stocks qualify that day (ADX < 18 on daily bars).
This is the same approach as the backtest that produced 89% win rate / 445 trades / 248 days.

**Scan command:** `python3 scripts/market_data.py scan-stocks`
Reports qualifying stocks sorted by ADX (lowest = most range-bound = best candidate).

**Blocklist — never trade these (backtest showed negative edge):**
- AXISBANK: 68% win rate, -₹0.39/share average
- BHARTIARTL: 64% win rate, -₹1.28/share average

**Stock universe scanned (all others):** RELIANCE, HDFCBANK, ICICIBANK, INFY, TCS, SBIN,
KOTAKBANK, BAJFINANCE, HINDUNILVR, LT, ITC, TATAMOTORS, TATASTEEL, WIPRO, HCLTECH, SUNPHARMA,
NTPC, POWERGRID, ADANIENT, ADANIPORTS, BAJAJFINSV, MARUTI, TITAN, ASIANPAINT, DRREDDY, CIPLA,
HINDALCO, JSWSTEEL, HEROMOTOCO, EICHERMOT, TECHM, ULTRACEMCO, GRASIM, COALINDIA, BPCL, ONGC,
INDUSINDBK, APOLLOHOSP, TATACONSUM, NESTLEIND, BEL, HDFCLIFE, SBILIFE, BAJAJ-AUTO, HINDZINC,
VEDL, NMDC, BANKBARODA, PNB, CANBK, SIEMENS, PIDILITIND, DMART.

**Stock-specific guardrails (apply in addition to the index rules above):**
- ADX uses **daily bars** (not hourly) — `scan-stocks` handles this automatically.
- DTE range: **2-7 days** (stocks have weekly + monthly expiry; don't go longer).
- Strike step and lot size: look up fresh from Dhan instrument master via
  `python3 scripts/dhan.py lookup <SYMBOL> <expiry> <strike> CE` — do NOT guess or hardcode,
  stock strike steps vary widely and get revised by SEBI periodically.
- Iron condor structure: same as indices — short legs 2 strike steps OTM, long legs 4 steps OTM.
- Premium estimate: use `hist_vol_pct` from `scan-stocks` output as the IV (pass via `--iv`)
  instead of India VIX — stock IV is higher than VIX and varies by stock.
- OI filter: short legs must have open interest > 1,000 contracts — check via Dhan option chain
  (live) or skip if OI data unavailable (paper mode only).
- Max risk per trade: same 5% of capital as indices.
- Never trade a stock during earnings week (results announcement within 5 days of expiry) —
  IV spike can blow out the condor. Check NSE calendar before entering.

**Top performers from backtest (July 2023 – July 2024) for reference:**
ITC 100% WR, INDUSINDBK 100%, ASIANPAINT 100%, ULTRACEMCO 100%, SBIN 100%, BANKBARODA 100%,
SBILIFE 95%, BAJAJFINSV 95%, TCS 93%, APOLLOHOSP 86%. These had the best historical edge but
any qualifying stock on any given day is a valid trade — don't cherry-pick only these.
- **No naked option buying, no uncapped/undefined-risk positions** unless this file is explicitly
  updated with new backtest evidence justifying it.
- **Paper first.** Do not place a live-money order while `TRADING_MODE` above reads `paper`.

## Research cadence (what each routine should be checking)

- **Pre-market:** scan ADX/IV/India VIX conditions across NIFTY/BANKNIFTY/SENSEX, note which
  instruments look range-bound vs. trending for the day ahead. Draft — don't execute yet.
- **Market open / intraday-monitor:** once the opening range has printed, check ADX(14) on each
  instrument. Below 18 → evaluate selling the iron condor per the guardrails above. Re-check
  periodically (every ~15-30 min) for new qualifying setups and to manage open positions against
  the exit rules.
- **EOD square-off:** force-close everything by ~3:15-3:20 PM IST, log the day, send the Telegram
  summary.
- **Weekly review:** performance vs. backtest expectations (P&L, win rate, trade frequency), flag
  if live results are drifting meaningfully from the ~70-79% backtest win rate — that's the signal
  to slow down and re-examine, not to immediately change the strategy file.

## Watchlist

_(Theta: keep this updated with anything instrument-specific you're tracking — e.g. an instrument
that's been consistently trending and so hasn't qualified for entry in a while.)_
