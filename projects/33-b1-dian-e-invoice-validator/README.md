# B1 Dian E Invoice Validator

**Area:** SAP Business One · Colombia electronic invoicing (DIAN)

## Real-life case

Real case: every B1 invoice in Colombia must be a DIAN electronic invoice. Before sending it to the technology provider, this validator checks the NIT check digit (DIAN modulus-11 algorithm), recomputes taxes by rate group, verifies totals and builds the CUFE (SHA-384 over the fields defined in the DIAN technical annex). A wrong CUFE or total means a rejected invoice and a customer that cannot pay.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates, tiers and parameters are illustrative and come from configuration in a real system.
