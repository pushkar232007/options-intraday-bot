Check every open position against the exit rules in memory/strategy.md.

1. `python3 scripts/dhan.py orders` to determine current open legs — filter to `orderStatus ==
   "TRADED"` and net BUY/SELL quantity per `securityId`. **`python3 scripts/dhan.py positions` is
   known to return empty even right after a confirmed fill in sandbox testing — don't rely on it.**
2. For each open spread, estimate the current cost-to-close using `python3 scripts/market_data.py
   estimate-premium <X> <strike> <CE|PE> --dte <days remaining>` for each of the 4 legs (Dhan's
   sandbox has no live option-chain to read real prices from - see memory/signals-learnings.md;
   this BS-based estimate off real spot+VIX is the same approach the backtest validated). Compare
   the estimated cost-to-close to the entry credit logged in trade-log.md. **While
   `TRADING_MODE: paper`, that logged entry credit is itself the step-5 estimate from trade.md, not
   a real fill price** — Dhan's sandbox fills every order at a flat fake price of 100 regardless of
   real market price (see memory/signals-learnings.md), so trusting `averageTradedPrice` here would
   be wrong. Both sides of this comparison are consistently estimate-based until `TRADING_MODE`
   flips to `live`, which is expected and fine.
   - Cost-to-close <= 50% of entry credit → close now, log as `PROFIT_TARGET`.
   - Cost-to-close >= 2x entry credit → close now, log as `SL`.
   - Otherwise → leave it open, but note its current status in memory/trade-log.md if it's
     gotten meaningfully closer to either threshold since the last check.
3. To close a position, place the opposite legs via `python3 scripts/dhan.py place-order
   --security-id <id> --txn <BUY|SELL> --qty <lots*lot_size>` for each leg. **Then poll
   `python3 scripts/dhan.py order-status <orderId>` until `orderStatus` reads `TRADED` — a closing
   order sat `PENDING` with `filledQty: 0` for over a minute in testing, don't assume the initial
   `TRANSIT` response means it's done.**
4. Log every close (or non-action) with the reason to memory/trade-log.md.
5. Send a Telegram notification via scripts/telegram.py only if a position was actually closed
   (confirmed `TRADED`, not just placed).
