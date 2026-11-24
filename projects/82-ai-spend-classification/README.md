# Ai Spend Classification

**Area:** Procurement analytics · Spend cube

## Problem and solution

Innovation: 40% of spend sits in 'miscellaneous' because PO texts are free text. Classifies purchase lines into UNSPSC-like segments by weighted keywords and reports spend by category and the unclassified residue.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
