from main import build_key, validate_key, cnpj_valid

def test_cnpj_check_digits():
    assert cnpj_valid("11.222.333/0001-81")        # textbook valid CNPJ
    assert not cnpj_valid("11.222.333/0001-82")
    assert not cnpj_valid("11111111111111")

def test_key_roundtrip_and_structure():
    k = build_key("SP", "2611", "11.222.333/0001-81", 55, 1, 12345, 1, 98765432)
    assert len(k) == 44 and k.startswith("352611") and validate_key(k) == (True, "ok")

def test_single_digit_tamper_detected():
    k = build_key("SP", "2611", "11222333000181", 55, 1, 12345, 1, 98765432)
    tampered = k[:20] + str((int(k[20]) + 1) % 10) + k[21:]
    assert validate_key(tampered) == (False, "check digit mismatch")
