# Mig Custom Code S4 Scanner

**Area:** S/4HANA migration · Custom code analysis

## Problem and solution

Problem: Z-programs that read BSEG, MKPF/MSEG or KONV, call XD01/XK01, or SELECT inside loops compile in S/4HANA but return nothing or crawl. Scans ABAP source and reports findings with line, severity and the recommended replacement.

## Run

```bash
pytest -q
```

Python 3.11+, standard library only. Parameters are illustrative.
