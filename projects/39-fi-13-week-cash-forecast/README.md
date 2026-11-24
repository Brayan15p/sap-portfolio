# Fi 13 Week Cash Forecast

**Area:** S/4HANA Finance · Cash management

## Real-life case

Real case: the CFO asks if payroll can be paid in week 6. The 13-week forecast projects collections using each customer's real payment behavior (average days late), supplier payments by due date, fixed outflows, and flags the first week cash goes below the minimum.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Rates, tiers and parameters are illustrative and come from configuration in a real system.
