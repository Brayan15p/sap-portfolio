# Grc Sod Conflicts

**Area:** GRC · Segregation of duties

## Problem and solution

Problem: one user who can create a vendor and also pay it is a fraud risk auditors always find. Expands roles to transactions, applies SoD rules (function pairs) and lists conflicts per user with mitigating controls.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
