# Standard rates (illustrative; maintain in tax configuration)
RATES = {"ES": 21, "DE": 19, "FR": 20, "IT": 22, "PT": 23, "NL": 21}
EU = set(RATES)
OSS_THRESHOLD = 10_000  # EUR, EU-wide distance-sales threshold

def determine(seller_country, buyer_country, buyer_vat_id, cross_border_b2c_ytd, net):
    if buyer_country not in EU:
        return {"code": "EXPORT", "rate": 0, "vat": 0, "note": "Export outside the EU, zero-rated"}
    if buyer_country == seller_country:
        r = RATES[seller_country]; return {"code": "DOMESTIC", "rate": r, "vat": round(net * r / 100, 2), "note": ""}
    if buyer_vat_id:
        return {"code": "REVERSE_CHARGE", "rate": 0, "vat": 0, "note": "Reverse charge: VAT due by the recipient"}
    if cross_border_b2c_ytd + net > OSS_THRESHOLD:
        r = RATES[buyer_country]; return {"code": "OSS", "rate": r, "vat": round(net * r / 100, 2), "note": f"OSS, {buyer_country} rate"}
    r = RATES[seller_country]; return {"code": "B2C_ORIGIN", "rate": r, "vat": round(net * r / 100, 2), "note": "Below OSS threshold"}
