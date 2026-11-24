#!/usr/bin/env bash
# Runs every project's test suite. Python projects need pytest; project 15 needs Node 22.
set -e
for d in projects/*/; do
  if [ -f "$d/test_main.py" ]; then (cd "$d" && python3 -m pytest -q -p no:cacheprovider | tail -1 | sed "s|^|$d: |"); fi
done
(cd projects/15-zavora-sap-b1-orders && npm install --silent && npx vitest run | grep "Tests ")
