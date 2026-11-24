# Btp Api Rate Limit Client

**Area:** SAP BTP · Resilient API consumption

## Problem and solution

Real case: SAP APIs (and partners) enforce quotas; a bulk sync gets HTTP 429 and dies. A token-bucket limiter keeps the client under quota, and a retry policy honors Retry-After and exponential backoff with jitter, only for retryable errors.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Factors and thresholds are illustrative.
