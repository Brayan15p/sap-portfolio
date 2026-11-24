# B1 Partial Deliveries

**Area:** SAP Business One · Sales

Tracks open quantity per sales-order line across partial deliveries (Orders → DeliveryNotes, BaseEntry/BaseLine). Over-delivery is rejected.

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are covered by the tests in `test_main.py`.
