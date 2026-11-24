# Pp Finite Capacity Scheduling

**Area:** SAP PP · Capacity planning

## Real-life case

Real case: sales promises dates the plant cannot meet. Orders are backward-scheduled from their due date across work centers with daily capacity; if an operation does not fit, it is pushed earlier, and if that falls before today the order is flagged as late with the bottleneck.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates, tiers and parameters are illustrative and come from configuration in a real system.
