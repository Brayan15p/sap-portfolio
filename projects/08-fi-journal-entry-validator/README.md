# Fi Journal Entry Validator

**Area:** S/4HANA Finance · GL

Pre-posting validator for journal entry templates: balance, single currency, mandatory cost center on expense accounts. Errors name the line and the rule.

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are covered by the tests in `test_main.py`.
