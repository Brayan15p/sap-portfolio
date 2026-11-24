# Fi Fx Revaluation

**Area:** S/4HANA Finance · Foreign currency valuation (FAGL_FCV)

## Real-life case

Real case: an importer has open USD supplier invoices at month end. Each item is revalued at the closing TRM; the unrealized gain/loss is posted and reversed on day 1 of the next month.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
