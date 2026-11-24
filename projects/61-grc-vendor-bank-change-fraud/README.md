# Grc Vendor Bank Change Fraud

**Area:** FI-AP · Fraud detection

## Problem and solution

Problem: the classic payment fraud is changing a vendor's bank account and paying right after. Flags payments to an account changed within N days before payment, changes made by the same user who released the payment, and accounts shared by different vendors.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
