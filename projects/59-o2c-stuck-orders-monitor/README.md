# O2C Stuck Orders Monitor

**Area:** SD · Order-to-cash monitoring

## Problem and solution

Problem (Revlon): orders sit unshipped and nobody sees why. Classifies each open order by the first blocking reason in the O2C chain (incompletion, credit block, delivery block, no ATP confirmation, delivery not picked, not billed) with value at risk.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
