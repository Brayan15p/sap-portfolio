# Ai Invoice Text Extraction

**Area:** AI · Document capture

## Problem and solution

Innovation: supplier PDFs arrive as text from OCR. Extracts NIT, invoice number, date, subtotal, IVA and total; validates that subtotal + IVA = total before creating the invoice in SAP, otherwise routes to review.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
