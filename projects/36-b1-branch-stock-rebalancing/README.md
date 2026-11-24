# B1 Branch Stock Rebalancing

**Area:** SAP Business One · Multi-warehouse

## Real-life case

Real case: a chain with 4 branches has excess stock in one city and stock-outs in another. The planner proposes inventory transfer requests from surplus to deficit branches, keeps each source above its safety stock, and prefers the cheapest route per unit.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates, tiers and parameters are illustrative and come from configuration in a real system.
