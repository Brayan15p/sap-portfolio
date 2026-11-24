def sync(fetch_page, checkpoint: dict, apply, page_size=2, fail_after_pages=None):
    """fetch_page(after_ts, after_code, n) -> items sorted by (updated, code)."""
    pages = 0
    while True:
        batch = fetch_page(checkpoint.get("ts", ""), checkpoint.get("code", ""), page_size)
        if not batch:
            return checkpoint
        for it in batch:
            apply(it)
            checkpoint["ts"], checkpoint["code"] = it["updated"], it["code"]  # commit per item
        pages += 1
        if fail_after_pages and pages >= fail_after_pages:
            raise ConnectionError("simulated network cut")

def make_source(items):
    def fetch(ts, code, n):
        rest = [i for i in sorted(items, key=lambda i: (i["updated"], i["code"])) if (i["updated"], i["code"]) > (ts, code)]
        return rest[:n]
    return fetch
