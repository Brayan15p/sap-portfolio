# Mx Cfdi Totals

**Area:** SAP Localization Mexico · CFDI 4.0

## Real-life case

Real case: a Mexican CFDI is rejected by the PAC if totals do not tie out: line amounts minus discounts, transferred IVA 16% and withheld IVA and ISR (services billed by individuals to companies). This validates RFC format and recomputes every total the PAC checks.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates and thresholds are illustrative and must come from maintained tax configuration.
