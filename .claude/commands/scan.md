Scan NIFTY, BANKNIFTY, and SENSEX for the day's setup conditions, per memory/strategy.md.

1. `python3 scripts/market_data.py scan` - gives real spot price, ADX(14), and India VIX for all
   three instruments in one call (Yahoo-Finance-based; Dhan's sandbox 404s on option-chain/quote
   endpoints, see memory/signals-learnings.md, so this is the data source until a live Data API
   subscription exists).
2. Classify each instrument from the `range_bound` field: `true` (ADX < 18) → qualifies for the
   strategy today; `false` → trending, skip today.
3. Put-call ratio isn't available without the Data API subscription - skip it, don't block on it.

Do not place any trade from this command - it only informs memory/research-log.md.
