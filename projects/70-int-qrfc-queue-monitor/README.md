# Int Qrfc Queue Monitor

**Area:** Integration · qRFC/bgRFC queues (SMQ1/SMQ2)

## Problem and solution

Problem: one failed LUW blocks the whole queue and thousands of orders wait behind it. Finds blocked queues, the first erroneous entry, how many entries wait behind it and how old the oldest entry is.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
