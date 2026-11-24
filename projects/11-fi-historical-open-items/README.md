# Fi Historical Open Items

**Area:** S/4HANA Finance · AR/AP

Rebuilds open items as of a past key date: payments cleared after the key date do not change the historical balance.

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are covered by the tests in `test_main.py`.
