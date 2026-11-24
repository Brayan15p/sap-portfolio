# B1 Landed Costs Import

**Area:** SAP Business One · Landed Costs (imports)

## Real-life case

Real case: an importer receives a container. The real cost of each item is FOB price plus freight, insurance (allocated by value), customs duty (by tariff rate on CIF) and port handling (allocated by weight). Without landed costs, margins are fiction. Allocation is exact to the peso and produces the new unit cost per item, like the B1 Landed Costs document.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates, tiers and parameters are illustrative and come from configuration in a real system.
