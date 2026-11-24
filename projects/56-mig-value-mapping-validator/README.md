# Mig Value Mapping Validator

**Area:** Data migration · Value mapping

## Problem and solution

Problem: legacy codes (payment terms, units, tax codes) must map 1:1 to SAP values. Unmapped or conflicting mappings appear only at load time. Validates the mapping table and the source data against it before any load.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
