# Ifrs16 Lease Accounting

**Area:** S/4HANA RE-FX / Lease accounting · IFRS 16

## Real-life case

Real case: a hospital leases an MRI machine for 5 years. Under IFRS 16 it must recognize a lease liability (present value of payments at the incremental borrowing rate) and a right-of-use asset, then each month split the payment into interest and principal and depreciate the asset.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates and thresholds are illustrative and must come from maintained tax configuration.
