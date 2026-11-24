# Fi Co Withholding Taxes

**Area:** S/4HANA Finance · Colombia localization

## Real-life case

Real case: a Colombian company pays a supplier invoice and must withhold retención en la fuente, ReteIVA and ReteICA. Retefuente only applies above a minimum base expressed in UVT; ReteIVA is a share of the IVA; ReteICA depends on the municipality rate (per mil). The calculator returns each withholding, the net payable and the journal lines.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
