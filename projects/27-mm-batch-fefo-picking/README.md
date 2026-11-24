# Mm Batch Fefo Picking

**Area:** SAP MM/WM · Batch management (hospital pharmacy)

## Real-life case

Real case: dispensing a drug must pick First-Expired-First-Out, never expired batches, never batches with less than the minimum remaining shelf life, and never batches under quality block.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
