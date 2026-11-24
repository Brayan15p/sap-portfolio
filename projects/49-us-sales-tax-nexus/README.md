# Us Sales Tax Nexus

**Area:** SAP Tax · United States sales tax

## Real-life case

Real case: after the Wayfair ruling, a Colombian e-commerce selling into the US owes sales tax in a state once it crosses that state's economic nexus threshold (sales amount and/or number of transactions). The monitor tracks rolling sales per state and alerts before and when nexus is reached.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates and thresholds are illustrative and must come from maintained tax configuration.
