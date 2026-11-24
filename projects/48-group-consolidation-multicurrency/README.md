# Group Consolidation Multicurrency

**Area:** SAP Group Reporting · Consolidation

## Real-life case

Real case: a Colombian holding consolidates subsidiaries in Mexico (MXN) and the US (USD). Balance sheets are translated at closing rate, P&L at average rate, equity at historical rate; the difference goes to the cumulative translation adjustment (CTA). Intercompany receivables/payables and sales/purchases are eliminated; a mismatch is reported instead of silently plugged.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates and thresholds are illustrative and must come from maintained tax configuration.
