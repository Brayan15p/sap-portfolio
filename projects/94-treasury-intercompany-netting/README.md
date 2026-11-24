# Treasury Intercompany Netting

**Area:** Treasury · Multilateral netting

## Problem and solution

Real case: 5 subsidiaries owe each other; settling every invoice means dozens of bank transfers and FX spreads. Multilateral netting computes each entity's net position and the minimal set of payments to settle the group.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
