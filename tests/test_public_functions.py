from WorldTradingData.public.base import WorldTradingData
import WorldTradingData.public.base as wtd_lib
from .secure import api_token


# def test_world_trading_data_class():
#     wtd = WorldTradingData(api_token)
#     result = wtd.stock_search('AAPL')
#     # print(result)
#     assert type(result) == dict
#     new_result = wtd.stock_search('AAPL', {'output': 'csv'})
#     assert type(new_result) == str
#     new_result = wtd.stock_search('AAPL', {'api_token': 'not_my_token'})
#     assert type(result) == dict


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


# def test_wtd_stock():
#     wtd = WorldTradingData(api_token)
#     result = wtd.stock(['AAPL'])
#     assert type(result) == dict
#     result = wtd.stock(['AAPL', 'GOOG'])
#     assert type(result) == dict
#     result = wtd.stock(['AAPL', 'GOOG'], {'output': 'csv'})
#     assert type(result) == str
#
#
# def test_mutual_fund():
#     wtd = WorldTradingData(api_token)
#     res = wtd.mutual_fund(['AAAAX', 'AAADX', 'AAAGX'])
#     assert type(res) == dict
#     res = wtd.mutual_fund(['AAAAX', 'AAADX', 'AAAGX'], {'output': 'csv'})
#     assert type(res) == str
#     res = wtd.mutual_fund(['AAAAX', 'AAADX', 'AAAGX'], {'sort_by': 'name'})
#     assert type(res) == dict

def test_intraday():
    wtd = WorldTradingData(api_token)
    symbol = 'aapl'
    time_interval = 5
    day_range = 2
    res = wtd.intraday(symbol, time_interval, day_range)
    assert type(res) == dict
    assert 'symbol' in res.keys()
    assert 'stock_exchange_short' in res.keys()
    assert 'timezone_name' in res.keys()
    assert 'intraday' in res.keys()
