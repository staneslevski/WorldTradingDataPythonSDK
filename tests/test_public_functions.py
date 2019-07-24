from WorldTradingData.public.base import WorldTradingData
from .secure import api_token


def test_world_trading_data_class():
    wtd = WorldTradingData(api_token)
    result = wtd.search_stock('AAPL')
    assert result == "string"
