from WorldTradingData.public.base import WorldTradingData
from .secure import api_token


def test_world_trading_data_class():
    wtd = WorldTradingData(api_token)
    result = wtd.search_stock('AAPL')
    # print(result)
    assert result == {"message":"Your account has a max limit of 5. Upgrade your account to increase your limit.","total_returned":5,"total_results":6,"total_pages":2,"limit":5,"page":1,"data":[{"symbol":"AAPL","name":"Apple Inc.","currency":"USD","price":"208.67","stock_exchange_long":"NASDAQ Stock Exchange","stock_exchange_short":"NASDAQ"},{"symbol":"AAPL.BA","name":"APPLE INC CEDEAR","currency":"ARS","price":"897.00","stock_exchange_long":"Buenos Aires Stock Exchange","stock_exchange_short":"BCBA"},{"symbol":"AAPL.MI","name":"Apple Inc.","currency":"EUR","price":"186.16","stock_exchange_long":"Milan Stock Exchange","stock_exchange_short":"MIL"},{"symbol":"AAPL.MX","name":"Apple Inc.","currency":"MXN","price":"3971.31","stock_exchange_long":"Mexican Stock Exchange","stock_exchange_short":"MEX"},{"symbol":"AAPL.SW","name":"Apple Inc.","currency":"CHF","price":"0.00","stock_exchange_long":"SIX Swiss Exchange","stock_exchange_short":"SIX"}]}
    new_result = wtd.search_stock('AAPL', {'output': 'csv'})
