# Sd Credit Limit Check

**Area:** SAP SD · Credit management

## Real-life case

Real case: a distributor's customer orders again while having overdue invoices. The check computes credit exposure (open receivables + open orders + this order) and blocks if it exceeds the limit or if any invoice is overdue more than N days. A credit manager can release a blocked order once, with a reason.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
