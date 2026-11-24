# Co Product Cost Estimate

**Area:** SAP CO-PC · Standard cost estimate (CK11N logic)

## Real-life case

Real case: a cosmetics plant needs the standard cost of a cream. Multi-level BOM explosion with component scrap, raw material prices, routing operations times activity rates per work center, and overhead on material; detects a recursive BOM before it hangs the run.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates, tiers and parameters are illustrative and come from configuration in a real system.
