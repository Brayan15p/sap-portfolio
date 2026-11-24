from main import best_forecast
def test_trend_is_captured():
    s = [100 + 10 * i for i in range(12)]
    r = best_forecast(s)
    assert r["mape"] < 1 and abs(r["forecast"][0] - 220) < 2
