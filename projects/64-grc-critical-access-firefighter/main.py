from datetime import datetime, timedelta
CRITICAL = {"SE16N", "SE38", "SM30", "SU01", "PFCG", "SCC4", "SE11"}
def review(sessions, max_hours=4):
    findings = []
    for s in sessions:
        issues = []
        if not s.get("ticket"): issues.append("no ticket")
        if s["end"] - s["start"] > timedelta(hours=max_hours): issues.append("exceeded duration")
        crit = sorted(CRITICAL & set(s["tcodes"]))
        if crit: issues.append(f"critical tcodes {crit}")
        if not s.get("reviewed_at") or s["reviewed_at"] - s["end"] > timedelta(days=2): issues.append("review late or missing")
        if issues: findings.append({"session": s["id"], "issues": issues})
    return findings
