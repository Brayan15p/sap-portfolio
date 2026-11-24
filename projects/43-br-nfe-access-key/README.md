# Br Nfe Access Key

**Area:** SAP Localization Brazil · NF-e

## Real-life case

Real case: every Brazilian electronic invoice (NF-e, model 55) carries a 44-digit access key (chave de acesso): state code, year-month, CNPJ, model, series, number, emission type, random code and a modulus-11 check digit. A wrong digit means SEFAZ rejects the invoice and the truck cannot leave the warehouse. This builds and validates keys and validates the CNPJ check digits.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates and thresholds are illustrative and must come from maintained tax configuration.
