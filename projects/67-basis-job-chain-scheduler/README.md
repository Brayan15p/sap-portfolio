# Basis Job Chain Scheduler

**Area:** Basis · Background jobs (SM36/SM37)

## Problem and solution

Problem: nightly jobs (MRP, billing, payment run, BI extract) depend on each other and must finish before 6 a.m. Schedules the chain respecting dependencies and server slots, and reports the jobs that push the chain past the window.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
