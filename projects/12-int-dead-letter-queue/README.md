# Int Dead Letter Queue

**Area:** SAP Integration Suite pattern

Failed messages are kept with error and correlation id; after fixing the mapping, only the affected messages are reprocessed.

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are covered by the tests in `test_main.py`.
