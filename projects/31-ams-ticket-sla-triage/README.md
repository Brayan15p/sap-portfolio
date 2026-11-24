# Ams Ticket Sla Triage

**Area:** SAP AMS · Support operations

## Real-life case

Real case: an AMS team receives SAP incidents. Priority comes from an impact x urgency matrix; the SLA clock only runs in business hours (Mon-Fri 8-18) and pauses while waiting for the customer; tickets near breach are escalated.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Business rules are proven by `test_main.py`. Parameters (tax rates, UVT, tolerances) are illustrative and must come from configuration in a real system.
