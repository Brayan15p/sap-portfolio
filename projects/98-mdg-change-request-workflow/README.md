# Mdg Change Request Workflow

**Area:** SAP MDG · Master data governance

## Problem and solution

Real case: anyone could edit vendor master data, so bad data and fraud got in. A change request workflow: requester creates, data steward validates rules, approver (different person) approves; critical fields (bank, tax id) need a second approval. Every step is audited.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
