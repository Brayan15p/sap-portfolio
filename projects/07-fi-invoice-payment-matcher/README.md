# Fi Invoice Payment Matcher

**Area:** S/4HANA Finance · AR

Matches incoming payments to open invoices: exact by reference, exact by amount when unique, partial, or REVIEW when ambiguous.

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are covered by the tests in `test_main.py`.
