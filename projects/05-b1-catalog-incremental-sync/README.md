# B1 Catalog Incremental Sync

**Area:** SAP Business One · Integration

Paged, incremental item sync with a persisted checkpoint (UpdateDate + ItemCode). Interrupted runs resume without losing or repeating items.

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are covered by the tests in `test_main.py`.
