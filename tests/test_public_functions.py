from WorldTradingData.public.base import WorldTradingData
from .secure import api_token


def test_world_trading_data_class():
    wtd = WorldTradingData(api_token)
    result = wtd.search_stock('AAPL')
    # print(result)
    assert type(result) == dict
    new_result = wtd.search_stock('AAPL', {'output': 'csv'})
    assert type(new_result) == str
    new_result = wtd.search_stock('AAPL', {'api_token': 'not_my_token'})
    assert type(result) == dict
