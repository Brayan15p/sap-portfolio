import re
CHECKS = [
    (r"\b(FROM|UPDATE|INTO)\s+(MKPF|MSEG)\b", "HIGH", "Material documents moved to MATDOC; use I_MaterialDocumentItem / MATDOC"),
    (r"\bFROM\s+KONV\b", "HIGH", "Pricing conditions moved to PRCD_ELEMENTS"),
    (r"\bFROM\s+(BSEG|BSIS|BSAS|BSID|BSAD|BSIK|BSAK)\b", "MEDIUM", "Use ACDOCA / I_JournalEntryItem; index tables are compatibility views"),
    (r"CALL\s+TRANSACTION\s+'(XD0[123]|XK0[123]|FD0[123]|FK0[123])'", "HIGH", "Customer/vendor transactions replaced by BP (Business Partner)"),
    (r"\bSELECT\s+\*", "LOW", "SELECT * : list only needed fields"),
]
def scan(source: str, program="ZPROG"):
    findings, depth = [], 0
    for n, line in enumerate(source.upper().splitlines(), 1):
        code = line.split('"')[0]
        if code.strip().startswith("*"): continue
        if re.search(r"^\s*(LOOP AT|DO\b|WHILE\b)", code): depth += 1
        if re.search(r"^\s*(ENDLOOP|ENDDO|ENDWHILE)", code): depth = max(0, depth - 1)
        for pat, sev, fix in CHECKS:
            if re.search(pat, code): findings.append({"program": program, "line": n, "severity": sev, "fix": fix})
        if depth and re.search(r"\bSELECT\b", code):
            findings.append({"program": program, "line": n, "severity": "HIGH", "fix": "SELECT inside loop: use FOR ALL ENTRIES / JOIN before the loop"})
    return sorted(findings, key=lambda f: ("HIGH", "MEDIUM", "LOW").index(f["severity"]))
