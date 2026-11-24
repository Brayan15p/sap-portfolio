# Ams Short Dump Analyzer

**Area:** SAP AMS · Basis/ABAP support

## Real-life case

Real case: on Monday the support team finds 300 runtime errors (ST22). The analyzer parses dump exports, groups them by exception, program and include line, ranks the top offenders by count and affected users, and suggests the usual first check per exception.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates, tiers and parameters are illustrative and come from configuration in a real system.
