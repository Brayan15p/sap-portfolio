# Ams Sla Penalties

**Area:** AMS / Outsourcing · Service credits

## Problem and solution

Real case: an AMS contract pays service credits when monthly SLA compliance falls below target per priority. Computes compliance, credits with a cap on the monthly fee, and which tickets caused the breach.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
