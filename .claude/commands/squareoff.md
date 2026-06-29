Force-close every open position, end of day.

1. `python3 scripts/dhan.py square-off-all` to close everything via market orders.
2. Confirm via `python3 scripts/dhan.py positions` that nothing remains open.
3. If anything is still open and you believe it genuinely passes all three carry-forward
   conditions in memory/strategy.md (currently profitable, original thesis intact, stop tightened),
   message the human via scripts/telegram.py describing exactly what and why, and wait for
   confirmation rather than deciding alone - this should be rare enough that asking is correct.
4. Log the day's final state to memory/trade-log.md.
