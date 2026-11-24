# Fi Aa Depreciation

**Area:** S/4HANA Asset Accounting

## Real-life case

Real case: a hospital buys an ultrasound machine mid-month and later retires part of it. Monthly straight-line depreciation with salvage value, start in the month after capitalization, and partial retirement that reduces future depreciation proportionally.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
