# Contract Price Escalation

**Area:** MM/SD · Contract price adjustment

## Problem and solution

Real case: multi-year service contracts in Colombia adjust yearly by IPC (CPI) or a formula with labor and materials weights. Computes the new price per anniversary with a cap, and the back-billing when the adjustment is applied late.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
