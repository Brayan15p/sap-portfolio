def validate(mapping, data, field):
    """mapping: list of (legacy, sap). data: rows with field."""
    problems, seen = [], {}
    for legacy, sap in mapping:
        if legacy in seen and seen[legacy] != sap: problems.append(f"conflict: {legacy} -> {seen[legacy]} and {sap}")
        seen[legacy] = sap
    used = {r[field] for r in data}
    unmapped = sorted(used - seen.keys())
    for u in unmapped: problems.append(f"unmapped value {u!r} used in {sum(1 for r in data if r[field] == u)} rows")
    unused = sorted(seen.keys() - used)
    return {"ok": not problems, "problems": problems, "unused_mappings": unused}
