# Int Tracking Events Ordering

**Area:** SAP Integration Suite pattern · Logistics

Carrier tracking events arrive out of order; an old event never moves a delivered shipment back to in-transit.

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are covered by the tests in `test_main.py`.
