# Co Overhead Assessment

**Area:** S/4HANA Controlling · Assessment cycle (KSU5)

## Real-life case

Real case: the IT cost center (licenses, support) is allocated to hospital departments by number of users, and maintenance by square meters. Cycles run in sequence; the sender ends at zero and the grand total is preserved to the peso.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
