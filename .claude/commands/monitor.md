Check every open position against the exit rules in memory/strategy.md.

1. `python3 scripts/dhan.py positions` to get current open legs and their live valuations.
2. For each open spread, compute the current cost-to-close (what it'd cost to buy back the legs
   you sold and sell the legs you bought) and compare to the credit received at entry:
   - Cost-to-close <= 50% of entry credit → close now, log as `PROFIT_TARGET`.
   - Cost-to-close >= 2x entry credit → close now, log as `SL`.
   - Otherwise → leave it open, but note its current status in memory/trade-log.md if it's
     gotten meaningfully closer to either threshold since the last check.
3. To close a position, place the opposite legs via `python3 scripts/dhan.py place-spread`
   (or equivalent offsetting orders) - confirm the fill in `positions` afterward.
4. Log every close (or non-action) with the reason to memory/trade-log.md.
5. Send a Telegram notification via scripts/telegram.py only if a position was actually closed.
