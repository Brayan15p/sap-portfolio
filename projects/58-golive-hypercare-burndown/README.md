# Golive Hypercare Burndown

**Area:** Go-live · Hypercare

## Problem and solution

Problem: after go-live management asks 'are we stabilizing?'. From daily tickets opened/closed it computes backlog, burn rate, days to clear and flags when backlog grows 3 days in a row (Revlon-type warning sign).

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
