# Capstone Go Live Readiness Score

**Area:** Capstone · Go-live readiness (lessons from Lidl, Haribo, Revlon)

## Problem and solution

Capstone: most famous SAP failures went live with known red flags: dirty data, broken processes, untested integrations, weak controls, untrained users. This scores go-live readiness from measurable gates (data readiness, critical defects, integration tests, cutover rehearsal fits the window, unmitigated SoD conflicts, training, hypercare staffing). Any hard gate failing means NO-GO regardless of the score.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
