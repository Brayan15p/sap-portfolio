# Ai Gl Account Suggestion

**Area:** AI · Accounts payable automation

## Problem and solution

Innovation: AP clerks pick the expense account for non-PO invoices by hand. A small Naive Bayes model trained on past invoice texts suggests the GL account with a confidence score; low confidence goes to a human.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
