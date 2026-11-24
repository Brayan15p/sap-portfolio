from datetime import date

def open_items_at(invoices, clearings, key_date: date):
    cleared = {}
    for c in clearings:
        if c["date"] <= key_date:
            cleared[c["invoice"]] = cleared.get(c["invoice"], 0) + c["amount"]
    return {i["id"]: round(i["amount"] - cleared.get(i["id"], 0), 2)
            for i in invoices if i["posting"] <= key_date and i["amount"] - cleared.get(i["id"], 0) > 0}
