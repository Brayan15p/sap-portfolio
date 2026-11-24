# B1 Price List Importer

**Area:** SAP Business One · Master data

Validates a price-list CSV (currency, UoM, validity, price) before touching SAP. Invalid file → per-row report, nothing applied.

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are covered by the tests in `test_main.py`.
