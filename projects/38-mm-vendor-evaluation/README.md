# Mm Vendor Evaluation

**Area:** SAP MM · Vendor evaluation

## Real-life case

Real case: procurement must justify which supplier keeps the contract. Each vendor is scored on price (vs. best price), on-time delivery (days late per GR), quality (rejected quantity) with configurable weights; vendors below a threshold are flagged for review.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates, tiers and parameters are illustrative and come from configuration in a real system.
