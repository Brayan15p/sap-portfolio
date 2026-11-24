# Ai Demand Forecast Holt

**Area:** AI · Demand planning (IBP)

## Problem and solution

Innovation: MRP is only as good as its forecast. Holt's linear exponential smoothing captures level and trend, picks the best smoothing parameters by backtest error (MAPE) and forecasts the next periods.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
