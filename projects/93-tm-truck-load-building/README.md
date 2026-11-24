# Tm Truck Load Building

**Area:** SAP TM · Load planning

## Problem and solution

Real case: dispatch must load today's deliveries into the fewest trucks without exceeding weight or volume. First-fit decreasing on two dimensions builds the loads and reports utilization per truck.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
