import math
BENFORD = {d: math.log10(1 + 1 / d) for d in range(1, 10)}
def first_digit(x): return int(str(abs(x)).lstrip("0.")[0])
def analyze(entries, approval_limit, mad_threshold=0.015):
    by_user = {}
    for e in entries: by_user.setdefault(e["user"], []).append(e["amount"])
    out = {}
    for u, amts in by_user.items():
        digits = [first_digit(a) for a in amts if a]
        obs = {d: digits.count(d) / len(digits) for d in range(1, 10)}
        mad = sum(abs(obs[d] - BENFORD[d]) for d in range(1, 10)) / 9
        below = sum(1 for a in amts if 0.95 * approval_limit <= a < approval_limit)
        rounds = sum(1 for a in amts if a % 1000 == 0)
        out[u] = {"mad": round(mad, 4), "flag": mad > mad_threshold or below / len(amts) > 0.02, "just_below_limit": below, "round_amounts": rounds}
    return out
