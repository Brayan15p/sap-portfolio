def evm(wbs, bac_total=None):
    out = {}
    for w, d in wbs.items():
        ev = d["bac"] * d["pct_complete"]; cpi = ev / d["ac"] if d["ac"] else 1; spi = ev / d["pv"] if d["pv"] else 1
        eac = d["bac"] / cpi if cpi else float("inf")
        out[w] = {"EV": round(ev), "CPI": round(cpi, 2), "SPI": round(spi, 2), "EAC": round(eac), "VAC": round(d["bac"] - eac),
                  "status": "RED" if cpi < 0.9 or spi < 0.9 else "AMBER" if cpi < 1 or spi < 1 else "GREEN"}
    return out
