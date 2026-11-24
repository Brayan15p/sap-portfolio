# Int Idoc Orders Inbound

**Area:** SAP integration · IDoc ORDERS05 inbound

## Real-life case

Real case: a retailer's EDI orders arrive as ORDERS05 IDocs. Segments are parsed, partner and material numbers converted to SAP values, and each IDoc gets SAP-like status 53 (posted) or 51 (error) with messages; status 51 can be reprocessed after master data is fixed.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
