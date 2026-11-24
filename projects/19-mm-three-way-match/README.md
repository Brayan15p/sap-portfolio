# Mm Three Way Match

**Area:** SAP MM / FI-AP · Logistics invoice verification

## Real-life case

Real case (MIRO): a supplier invoices more than what was received or at a higher price. The 3-way match compares PO, goods receipt and invoice per line with quantity and price tolerances, and sets a payment block with the exact reason.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
