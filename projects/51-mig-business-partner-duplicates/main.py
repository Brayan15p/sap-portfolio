import re, unicodedata
from difflib import SequenceMatcher
STOP = {"SAS", "S", "A", "LTDA", "SA", "DE", "LA", "EL", "Y", "CIA", "INC"}
def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().upper()
    return " ".join(w for w in re.sub(r"[^A-Z0-9 ]", " ", s).split() if w not in STOP)
def clusters(records, threshold=0.88):
    parent = list(range(len(records)))
    def find(i):
        while parent[i] != i: parent[i] = parent[parent[i]]; i = parent[i]
        return i
    for i, a in enumerate(records):
        for j in range(i + 1, len(records)):
            b = records[j]
            same_tax = a.get("tax_id") and a.get("tax_id") == b.get("tax_id")
            fuzzy = a["city"] == b["city"] and SequenceMatcher(None, norm(a["name"]), norm(b["name"])).ratio() >= threshold
            if same_tax or fuzzy: parent[find(i)] = find(j)
    groups = {}
    for i in range(len(records)): groups.setdefault(find(i), []).append(records[i])
    out = []
    for g in groups.values():
        if len(g) > 1:
            survivor = max(g, key=lambda r: (sum(1 for v in r.values() if v), r.get("last_activity", "")))
            out.append({"survivor": survivor["id"], "merge": sorted(r["id"] for r in g if r is not survivor)})
    return out
