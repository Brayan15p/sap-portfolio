# Mig Cvi Readiness Check

**Area:** S/4HANA migration · CVI readiness

## Problem and solution

Problem: fields optional in ECC are mandatory for Business Partners in S/4HANA; conversion stops on the first bad record. Checks every customer/vendor against the target rules and reports per record and per rule, so cleansing starts months before cutover.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
