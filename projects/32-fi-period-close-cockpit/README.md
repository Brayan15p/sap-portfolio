# Fi Period Close Cockpit

**Area:** S/4HANA Finance · Month-end close

## Real-life case

Real case: month-end close has dependent tasks (GR/IR clearing before FX valuation, depreciation before reports). The cockpit computes what can run now, blocks tasks whose predecessors are not done, detects cycles, and refuses to close the period while a critical task is open.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
