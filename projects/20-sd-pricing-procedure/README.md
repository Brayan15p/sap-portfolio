# Sd Pricing Procedure

**Area:** SAP SD · Pricing (condition technique)

## Real-life case

Real case: a wholesaler prices with a base price, a customer-specific discount, volume scales and IVA, with the access sequence customer+material → price list → material. Returns every condition step like the pricing screen in a sales order.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
