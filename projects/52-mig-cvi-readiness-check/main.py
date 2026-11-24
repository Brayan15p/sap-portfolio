import re
RULES = {
    "name": lambda r: bool(r.get("name")),
    "country": lambda r: bool(re.fullmatch(r"[A-Z]{2}", r.get("country", ""))),
    "tax_id_for_CO": lambda r: r.get("country") != "CO" or bool(re.fullmatch(r"\d{6,10}", r.get("tax_id", ""))),
    "email_format": lambda r: not r.get("email") or bool(re.fullmatch(r"[^@ ]+@[^@ ]+\.[a-z]{2,}", r["email"])),
    "postal_code_for_US": lambda r: r.get("country") != "US" or bool(re.fullmatch(r"\d{5}", r.get("postal", ""))),
}
def readiness(records):
    failures, by_rule = {}, {k: 0 for k in RULES}
    for r in records:
        bad = [k for k, f in RULES.items() if not f(r)]
        if bad: failures[r["id"]] = bad
        for k in bad: by_rule[k] += 1
    pct = round(100 * (len(records) - len(failures)) / len(records), 1) if records else 100.0
    return {"ready_pct": pct, "failures": failures, "by_rule": by_rule}
