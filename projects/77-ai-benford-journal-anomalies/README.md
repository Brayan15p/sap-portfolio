# Ai Benford Journal Anomalies

**Area:** Audit analytics · Journal entries

## Problem and solution

Innovation: auditors use Benford's law to spot manipulated amounts. Compares first-digit distribution of journal amounts per user against Benford, flags users with high deviation (MAD) and round-number or just-below-approval-limit entries.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
