import re
CITIES = {"bogota": "BOG", "medellin": "MED", "cali": "CAL", "barranquilla": "BAQ"}
def parse(q):
    q = q.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    f = {}
    if "vencid" in q: f["status"] = "OVERDUE"
    if "pagad" in q: f["status"] = "PAID"
    m = re.search(r"(mas|menos) de (\d+(?:[.,]\d+)?)\s*(millones|mil)?", q)
    if m:
        n = float(m.group(2).replace(",", ".")) * {"millones": 1e6, "mil": 1e3, None: 1}[m.group(3)]
        f["min_amount" if m.group(1) == "mas" else "max_amount"] = n
    for c, code in CITIES.items():
        if c in q: f["city"] = code
    return f
def run(q, rows):
    f = parse(q)
    def ok(r):
        return (f.get("status") in (None, r["status"]) and r["amount"] > f.get("min_amount", float("-inf"))
                and r["amount"] < f.get("max_amount", float("inf")) and f.get("city") in (None, r["city"]))
    return f, [r for r in rows if ok(r)]
