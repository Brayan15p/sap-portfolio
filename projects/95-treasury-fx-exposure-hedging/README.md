# Treasury Fx Exposure Hedging

**Area:** Treasury · FX risk

## Problem and solution

Real case: a Colombian importer has USD payables and some USD receivables. Nets exposure by currency and maturity bucket, applies the hedging policy (e.g. 75% of next 3 months) and proposes forward contracts.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
