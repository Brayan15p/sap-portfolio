# Mig Business Partner Duplicates

**Area:** S/4HANA migration · Business Partner (CVI)

## Problem and solution

Problem: ECC kept customers and vendors apart; merging them into Business Partners surfaces duplicates with different spellings. Data quality is the most cited migration killer. Finds duplicate clusters by tax id or fuzzy name + city and proposes a survivor.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
