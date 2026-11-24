# Fi Duplicate Invoice Detector

**Area:** S/4HANA Finance · AP

Flags potentially duplicate supplier invoices after normalizing vendor, reference, amount and date window, and explains why.

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are covered by the tests in `test_main.py`.
