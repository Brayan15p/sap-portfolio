import csv, io
from datetime import date

def validate(csv_text: str, items: set, uoms: set, currencies: set):
    ok, errors = [], []
    for n, row in enumerate(csv.DictReader(io.StringIO(csv_text)), start=2):
        e = []
        if row["item"] not in items: e.append(f"unknown item {row['item']}")
        if row["uom"] not in uoms: e.append(f"unknown UoM {row['uom']}")
        if row["currency"] not in currencies: e.append(f"invalid currency {row['currency']}")
        try:
            price = float(row["price"])
            if price < 0: e.append("price < 0")
        except ValueError:
            e.append(f"price not numeric: {row['price']}")
        try:
            if date.fromisoformat(row["valid_to"]) < date.fromisoformat(row["valid_from"]):
                e.append("valid_to before valid_from")
        except ValueError:
            e.append("dates must be YYYY-MM-DD")
        (errors if e else ok).append({"row": n, "errors": e} if e else row)
    return {"apply": ok if not errors else [], "errors": errors}
