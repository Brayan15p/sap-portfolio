# Mig Cutover Critical Path

**Area:** Go-live · Cutover planning

## Problem and solution

Problem: cutover weekends fail because nobody knows which task actually drives the go-live time. Computes the critical path (CPM), slack per task and whether the plan fits the downtime window.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
