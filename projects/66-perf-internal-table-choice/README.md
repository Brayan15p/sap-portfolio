# Perf Internal Table Choice

**Area:** ABAP performance · Internal tables

## Problem and solution

Interview favorite: STANDARD vs SORTED vs HASHED. Simulates READ TABLE cost (comparisons) for each table kind over growing sizes, proving linear vs logarithmic vs constant access, and recommends a kind from the access pattern.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
