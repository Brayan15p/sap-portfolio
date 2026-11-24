import re
from datetime import date

def norm_ref(ref: str) -> str:
    s = re.sub(r"[^0-9A-Z]", "", ref.upper())
    return re.sub(r"(?<![0-9])0+(?=[0-9])", "", s)   # drop leading zeros of each number

def find_duplicates(invoices, days=10):
    hits = []
    for i, a in enumerate(invoices):
        for b in invoices[i + 1:]:
            if a["vendor"] != b["vendor"] or a["amount"] != b["amount"]:
                continue
            same_ref = norm_ref(a["ref"]) == norm_ref(b["ref"])
            close = abs((a["date"] - b["date"]).days) <= days
            if same_ref or close:
                reasons = ["same vendor", "same amount"] + (["same normalized reference"] if same_ref else []) + ([f"dates within {days} days"] if close else [])
                hits.append({"pair": (a["id"], b["id"]), "reasons": reasons})
    return hits
