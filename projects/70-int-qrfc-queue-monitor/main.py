def monitor(queues, now):
    out = []
    for name, entries in queues.items():
        if not entries: continue
        first_err = next((i for i, e in enumerate(entries) if e["status"] == "SYSFAIL"), None)
        oldest = min(e["ts"] for e in entries)
        if first_err is not None:
            out.append({"queue": name, "state": "BLOCKED", "blocking_entry": entries[first_err]["id"], "error": entries[first_err]["error"],
                        "waiting": len(entries) - first_err - 1, "oldest_age_min": (now - oldest) // 60})
        elif (now - oldest) > 1800:
            out.append({"queue": name, "state": "SLOW", "waiting": len(entries), "oldest_age_min": (now - oldest) // 60})
    return sorted(out, key=lambda x: (x["state"] != "BLOCKED", -x["waiting"]))
