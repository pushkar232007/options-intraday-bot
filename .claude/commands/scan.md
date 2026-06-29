Scan NIFTY, BANKNIFTY, and SENSEX for the day's setup conditions, per memory/strategy.md.

For each instrument:
1. Pull the option chain for the nearest weekly expiry: `python3 scripts/dhan.py option-chain <instrument> <expiry>`.
2. Note ADX(14) reading if available from the data, India VIX level, and put-call ratio from the
   chain's OI by strike.
3. Classify: range-bound (ADX < 18 → qualifies for the strategy) vs. trending (skip today).

Do not place any trade from this command - it only informs memory/research-log.md.
