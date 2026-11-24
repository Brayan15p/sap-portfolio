# Basis Job Runtime Anomaly

**Area:** Basis / AMS · Proactive monitoring

## Problem and solution

Problem: a job that normally runs 20 minutes takes 3 hours and nobody notices until users complain. Learns each job's runtime baseline (median and MAD, robust to outliers) and flags anomalous runs.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
