# Fi Payment Run Proposal

**Area:** S/4HANA Finance · Automatic payment program (F110)

## Real-life case

Real case: every Friday treasury pays suppliers. The proposal takes due items, uses early-payment discount when it pays before the discount date, skips blocked vendors and items, and respects a daily bank limit, prioritizing the largest discount savings.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
