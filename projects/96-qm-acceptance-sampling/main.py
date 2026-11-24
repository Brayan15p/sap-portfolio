from math import comb
def decide(defects_found, c): return "ACCEPT" if defects_found <= c else "REJECT"
def p_accept(n, c, p):
    return sum(comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(c + 1))
def oc_curve(n, c, rates=(0.005, 0.01, 0.02, 0.05, 0.10)):
    return {r: round(p_accept(n, c, r), 3) for r in rates}
