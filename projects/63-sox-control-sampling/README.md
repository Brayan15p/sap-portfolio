# Sox Control Sampling

**Area:** Audit · SOX / internal control testing

## Problem and solution

Problem: auditors test controls on samples; picking them by hand is biased. Selects a reproducible random sample sized by control frequency (AICPA-style table), forces in high-value items, and evaluates exceptions against tolerance.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
