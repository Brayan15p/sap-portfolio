# Sd Volume Rebates

**Area:** SAP SD · Rebate agreements

## Real-life case

Real case: a supermarket chain earns a retroactive rebate when yearly purchases cross tiers (2% from 500M, 3% from 1,000M). Monthly accruals are posted at the tier reached so far; when a higher tier is reached the catch-up for previous months is accrued; year-end settlement pays the exact amount.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates, tiers and parameters are illustrative and come from configuration in a real system.
