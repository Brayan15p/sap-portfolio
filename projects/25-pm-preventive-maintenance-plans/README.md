# Pm Preventive Maintenance Plans

**Area:** SAP PM · Preventive maintenance

## Real-life case

Real case: biomedical equipment needs time-based plans (every 90 days) and counter-based plans (every 500 operating hours). The scheduler generates calls inside a horizon, avoids duplicates if the previous order is still open, and shifts the next date from completion.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
