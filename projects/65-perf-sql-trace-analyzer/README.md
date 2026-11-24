# Perf Sql Trace Analyzer

**Area:** ABAP performance · ST05 SQL trace

## Problem and solution

Interview favorite: 'the report is slow, what do you do?'. Measure first. Parses an SQL trace, finds identical statements executed repeatedly (N+1 / SELECT in loop), full scans and the statements with the most total time.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
