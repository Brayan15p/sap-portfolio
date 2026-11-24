# Grc Critical Access Firefighter

**Area:** GRC · Emergency access

## Problem and solution

Problem: firefighter (emergency) IDs with SAP_ALL are used and nobody reviews the log. Checks each session: ticket reference, duration limit, critical transactions used, and whether the review was done within 2 days.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
