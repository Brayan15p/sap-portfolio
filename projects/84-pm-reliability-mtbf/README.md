# Pm Reliability Mtbf

**Area:** PM · Reliability engineering

## Problem and solution

Innovation: move maintenance from calendar to risk. From failure history it computes MTBF and MTTR per equipment, availability, and the probability of failing in the next N hours (exponential model); ranks equipment by risk x criticality.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
