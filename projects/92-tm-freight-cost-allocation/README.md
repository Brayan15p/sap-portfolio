# Tm Freight Cost Allocation

**Area:** SAP TM · Freight settlement

## Problem and solution

Real case: one truck carries deliveries for several customers and cost centers. The freight invoice is allocated by chargeable weight (max of real weight and volumetric weight), exact to the peso, so customer profitability is real.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
