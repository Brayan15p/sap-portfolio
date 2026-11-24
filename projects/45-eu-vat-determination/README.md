# Eu Vat Determination

**Area:** SAP Tax determination · European Union

## Real-life case

Real case: a Spanish SaaS sells across Europe. Domestic sales charge Spanish VAT; B2B sales to another EU country with a valid VAT ID are reverse-charged (0% with legal note); B2C cross-border sales above the EU-wide threshold use the customer country rate via OSS; exports outside the EU are zero-rated.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates and thresholds are illustrative and must come from maintained tax configuration.
