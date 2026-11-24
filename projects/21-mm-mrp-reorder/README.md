# Mm Mrp Reorder

**Area:** SAP MM/PP · Material requirements planning

## Real-life case

Real case: a hospital pharmacy must not run out of a critical drug. MRP projects stock day by day with demand, open POs and lead time, and proposes orders respecting safety stock, minimum lot and rounding to the supplier's pack size.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
