# Fi Bank Statement Reconciliation

**Area:** S/4HANA Finance · Bank accounting

## Real-life case

Real case: the treasurer loads the daily bank statement. Lines are matched to open customer invoices by reference or exact amount; bank fees and GMF (4x1000) are posted automatically to expense; the rest goes to a clarification worklist.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
