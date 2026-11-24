def reconcile(legacy, sap, key="id", amount="amount", group="company"):
    out = {}
    for g in sorted({r[group] for r in legacy} | {r[group] for r in sap}):
        L = {r[key]: r for r in legacy if r[group] == g}; S = {r[key]: r for r in sap if r[group] == g}
        diff_amount = [k for k in L.keys() & S.keys() if round(L[k][amount], 2) != round(S[k][amount], 2)]
        out[g] = {"count_legacy": len(L), "count_sap": len(S),
                  "total_legacy": round(sum(r[amount] for r in L.values()), 2), "total_sap": round(sum(r[amount] for r in S.values()), 2),
                  "missing_in_sap": sorted(L.keys() - S.keys()), "extra_in_sap": sorted(S.keys() - L.keys()),
                  "amount_mismatch": sorted(diff_amount)}
        out[g]["ok"] = not (out[g]["missing_in_sap"] or out[g]["extra_in_sap"] or diff_amount)
    return out
