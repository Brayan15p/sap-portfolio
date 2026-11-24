# In Gstin Gst Calculator

**Area:** SAP Localization India · GST

## Real-life case

Real case: an Indian invoice must split GST as CGST+SGST when supplier and customer are in the same state, or IGST when interstate. GSTIN carries the state code and a base-36 checksum; an invalid GSTIN blocks input-tax credit for the customer.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates and thresholds are illustrative and must come from maintained tax configuration.
