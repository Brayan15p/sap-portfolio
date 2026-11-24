import re
from itertools import combinations
def apply_payment(amount, open_items, note="", max_items=6):
    mentioned = set(re.findall(r"\d{3,}", note))
    pools = [[i for i in open_items if i["ref"] in mentioned], sorted(open_items, key=lambda i: i["due"])]
    for items in pools:          # 1) only invoices named in the remittance note, 2) any open invoice
        for n in range(1, min(max_items, len(items)) + 1):
            for combo in combinations(items, n):
                if round(sum(i["amount"] for i in combo), 2) == round(amount, 2):
                    return {"status": "MATCHED", "invoices": [i["ref"] for i in combo]}
    return {"status": "UNAPPLIED", "invoices": []}
