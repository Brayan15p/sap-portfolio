# Sd Atp Check

**Area:** SAP SD/MM · Available-to-promise

## Real-life case

Real case: a customer asks for 120 units in 3 days. ATP uses stock, planned receipts and already confirmed orders per warehouse, confirms what is possible on the requested date and proposes the rest for a later date, without stealing stock promised to others.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
