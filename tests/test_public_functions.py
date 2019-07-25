from WorldTradingData.public.base import WorldTradingData
import WorldTradingData.public.base as wtd_lib
from .secure import api_token


# def test_world_trading_data_class():
#     wtd = WorldTradingData(api_token)
#     result = wtd.search_stock('AAPL')
#     # print(result)
#     assert type(result) == dict
#     new_result = wtd.search_stock('AAPL', {'output': 'csv'})
#     assert type(new_result) == str
#     new_result = wtd.search_stock('AAPL', {'api_token': 'not_my_token'})
#     assert type(result) == dict

def test_wtd_stock():
    wtd = WorldTradingData(api_token)
    result = wtd.stock(['AAPL'])
    assert type(result) == dict
    result = wtd.stock(['AAPL', 'GOOG'])
    assert type(result) == dict
    result = wtd.stock(['AAPL', 'GOOG'], {'output': 'csv'})
    assert type(result) == str


def test_filter_unwanted_params():
    params = {
        'foo': 'bar',
        'horrible': 'do no keep me'
    }
    unwanted_keys = ['horrible']
    filtered = wtd_lib.filter_unwanted_params(params, unwanted_keys)
    assert len(filtered) == 1
    assert filtered == {'foo': 'bar'}


def filter_search_params():
    params = {
        'api_token': 'this is not my token',
        'search_by': 'symbol'
    }
    filtered = wtd_lib.filter_search_params(params)
    assert filtered == {'search_by': 'symbol'}


def test_reduce_list_to_string():
    symbols_list = ['AAPL', 'GOOG']
    symbols_string = 'GOOG,AAPL'
    result = wtd_lib.reduce_list_to_string(symbols_list)
    assert result == symbols_string
