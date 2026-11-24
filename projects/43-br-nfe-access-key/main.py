UF = {"SP": "35", "RJ": "33", "MG": "31", "PR": "41", "RS": "43", "BA": "29"}

def mod11_dv(digits: str) -> int:
    s, w = 0, 2
    for d in reversed(digits):
        s += int(d) * w; w = 2 if w == 9 else w + 1
    r = 11 - s % 11
    return 0 if r >= 10 else r

def cnpj_valid(cnpj: str) -> bool:
    n = "".join(c for c in cnpj if c.isdigit())
    if len(n) != 14 or n == n[0] * 14: return False
    def dv(base, weights):
        s = sum(int(a) * b for a, b in zip(base, weights)); r = s % 11
        return "0" if r < 2 else str(11 - r)
    w1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]; w2 = [6] + w1
    return n[12] == dv(n[:12], w1) and n[13] == dv(n[:13], w2)

def build_key(uf, yymm, cnpj, model, series, number, emission_type, code):
    if not cnpj_valid(cnpj): raise ValueError("Invalid CNPJ")
    body = f"{UF[uf]}{yymm}{''.join(c for c in cnpj if c.isdigit())}{model:02d}{series:03d}{number:09d}{emission_type}{code:08d}"
    assert len(body) == 43
    return body + str(mod11_dv(body))

def validate_key(key: str):
    if len(key) != 44 or not key.isdigit(): return False, "must be 44 digits"
    if int(key[-1]) != mod11_dv(key[:43]): return False, "check digit mismatch"
    return True, "ok"
