# Ai Natural Language Report Query

**Area:** Innovation · Natural-language analytics

## Problem and solution

Innovation: managers want to ask 'facturas vencidas de más de 5 millones en Medellín' instead of running a report. Parses the Spanish question into structured filters (status, amount, city, period) and applies them; unknown words are reported, not guessed.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
