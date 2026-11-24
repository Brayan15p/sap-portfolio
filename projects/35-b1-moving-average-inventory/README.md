# B1 Moving Average Inventory

**Area:** SAP Business One · Inventory valuation

## Real-life case

Real case: a distributor values stock at moving average. Receipts change the average, issues go out at the current average, returns to vendor reverse at the original receipt price, and a negative-stock issue is refused because it would corrupt the cost for months.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates, tiers and parameters are illustrative and come from configuration in a real system.
