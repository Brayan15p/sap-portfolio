import re
TAXONOMY = {"43 IT": {"laptop": 3, "licencia": 3, "servidor": 3, "software": 2, "toner": 1},
            "47 Cleaning": {"aseo": 3, "detergente": 3, "limpieza": 2, "escoba": 2},
            "42 Medical": {"guantes": 2, "jeringa": 3, "gasa": 3, "quirurgico": 3},
            "44 Office": {"papel": 2, "resma": 3, "toner": 2, "esfero": 3}}
def classify(text):
    words = re.findall(r"\w+", text.lower()); scores = {c: sum(k.get(w, 0) for w in words) for c, k in TAXONOMY.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "UNCLASSIFIED"
def cube(lines):
    out = {}
    for l in lines:
        c = classify(l["text"]); out[c] = round(out.get(c, 0) + l["amount"], 2)
    return dict(sorted(out.items(), key=lambda kv: -kv[1]))
