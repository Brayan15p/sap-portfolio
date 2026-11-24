def parse(idoc_text):
    head, items = {}, []
    for raw in idoc_text.strip().splitlines():
        seg, *fields = raw.split("|")
        kv = dict(f.split("=", 1) for f in fields)
        if seg == "E1EDK01": head.update(kv)
        elif seg == "E1EDKA1" and kv.get("PARVW") == "AG": head["partner"] = kv["PARTN"]
        elif seg == "E1EDP01": items.append({"pos": kv["POSEX"], "qty": float(kv["MENGE"]), "ext_mat": kv["IDTNR"]})
    return head, items

class Inbound:
    def __init__(self, partner_map, material_map):
        self.pm, self.mm, self.status = partner_map, material_map, {}
    def process(self, docnum, idoc_text):
        head, items = parse(idoc_text)
        msgs = []
        sold_to = self.pm.get(head.get("partner"))
        if not sold_to: msgs.append(f"Partner {head.get('partner')} has no customer mapping")
        lines = []
        for it in items:
            mat = self.mm.get(it["ext_mat"])
            if not mat: msgs.append(f"Item {it['pos']}: no material for {it['ext_mat']}")
            lines.append({"material": mat, "qty": it["qty"]})
        if msgs:
            self.status[docnum] = (51, msgs); return 51
        self.status[docnum] = (53, [f"Sales order created for {sold_to} with {len(lines)} items"])
        return 53
