# Ai Payment Date Prediction

**Area:** AI · Receivables

## Problem and solution

Innovation: instead of assuming customers pay on the due date, predicts each invoice's payment date from the customer's history, weighting recent behavior more (exponential decay), with a reliability score.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
