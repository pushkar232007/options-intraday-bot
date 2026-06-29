# Strategy & Guardrails

_Last updated: 2026-06-29 — initial strategy, validated via backtest, then cross-checked against
a real Dhan Sandbox account (funds/orders/positions tested end-to-end; see corrections below)._

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

- **Instruments:** NIFTY, BANKNIFTY, SENSEX. No individual stock options until this file says
  otherwise (revisit only once this strategy has a real paper-trading track record).
  **Correction (verified 2026-06-29 against Dhan's real instrument master): BANKNIFTY no longer
  has weekly options — it's monthly-only now.** NIFTY and SENSEX still have weekly expiries. The
  backtest's 1-6 DTE range is representative for NIFTY/SENSEX but NOT for BANKNIFTY, which will
  almost always be trading with many more days to expiry than the backtest covered. Treat
  BANKNIFTY trades as unvalidated by the DTE sweep until specifically re-backtested against its
  real monthly cycle — don't assume the same edge transfers.
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
- **Position sizing:** max 5% of capital risked per trade (₹5,000 at ₹1,00,000 capital), sized by
  the spread's own defined max loss — `(strike width - net credit received) × lot size` — not by
  lot count alone.
- **Daily loss circuit breaker:** if the day's realized + open P&L hits -10% of capital (₹10,000),
  stop opening new positions for the rest of that day. Existing positions still get managed/closed
  normally.
- **Exit rule (whichever hits first):**
  1. Profit target: close once the cost to close the spread has decayed to 50% of the credit
     received (lock in half the max profit, don't try to ride it to expiry intraday).
  2. Stop-loss: close if the cost to close grows to 2x the credit received.
  3. Forced EOD square-off: close everything by ~3:15-3:20 PM IST regardless, no exceptions for
     this strategy — a defined-risk spread has no real reason to carry overnight, so the original
     "rare carry-forward" exception is not expected to apply here. If a routine ever has a specific,
     logged reason to consider it anyway, the same 3-condition test from the original spec still
     applies: (a) currently profitable, (b) original thesis intact, (c) stop tightened before holding.
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
- **Expected trade frequency:** ~8-9 trades/month combined across all three instruments in backtest
  (roughly 1 every 3-4 trading days) — NOT daily. This is intentional selectivity, not a bug; don't
  loosen the ADX threshold to manufacture more trades without re-backtesting the change first.
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
