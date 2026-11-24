# Basis Transport Collision

**Area:** Basis · Transport management (STMS)

## Problem and solution

Problem: two developers change the same object in different transports; importing them in the wrong order overwrites a fix in production. Detects objects in more than one open transport and imports whose sequence would downgrade an object.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
