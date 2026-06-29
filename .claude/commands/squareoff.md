Force-close every open position, end of day.

1. `python3 scripts/dhan.py square-off-all` to place closing market orders for every net open
   position (computed from `orders`, not `positions` — see the sandbox quirk below).
2. **Do not assume placing the order means it closed.** For each order placed, poll
   `python3 scripts/dhan.py order-status <orderId>` (wait a few seconds between checks, a couple
   of tries) until `orderStatus` reads `TRADED`. In testing, a closing order sat in `PENDING` with
   `filledQty: 0` for over a minute — confirm the actual fill, don't trust the immediate `TRANSIT`
   response.
3. If an order is still stuck after a few checks, do NOT silently move on — message the human via
   scripts/telegram.py describing exactly which position is stuck and why, this is the urgent/
   abnormal case worth interrupting for.
4. `python3 scripts/dhan.py positions` is known to return empty even right after a confirmed fill
   in sandbox testing — don't use it to verify square-off success, use `orders` instead.
5. If anything genuinely passes all three carry-forward conditions in memory/strategy.md (currently
   profitable, original thesis intact, stop tightened), message the human via scripts/telegram.py
   describing exactly what and why, and wait for confirmation rather than deciding alone - this
   should be rare enough that asking is correct.
6. Log the day's final state (confirmed via `orders`, not `positions`) to memory/trade-log.md.
