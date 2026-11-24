# Mig Mock Load Reconciliation

**Area:** Data migration · Mock load reconciliation

## Problem and solution

Problem: a migration can 'succeed' while losing records or amounts. After each mock load, legacy and SAP extracts are reconciled per company code and object: counts, totals and the exact keys missing or extra.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
