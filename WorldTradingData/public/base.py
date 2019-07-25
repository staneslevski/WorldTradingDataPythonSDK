import urllib3
import json
from WorldTradingData.authenticator.base import AuthenticatedUrlBuilder


# utility functions
def filter_unwanted_params(params: dict, unwanted_keys: list):
    new_dict = {}
    for (key, value) in params.items():
        if key not in unwanted_keys:
            key = key
            value = params[key]
            new_dict[key] = value
    return new_dict


def reduce_list_to_string(symbol_list: list):
    single_string = symbol_list.pop()
    while len(symbol_list) > 0:
        val = symbol_list.pop()
        single_string = '{single_string},{val}'.format(
            single_string=single_string,
            val=val
        )
    return single_string


def filter_search_params(params):
    unwanted_values = ['api_token', 'search_term']
    return filter_unwanted_params(params, unwanted_values)


# main class
class WorldTradingData:
    def __init__(self, api_token):
        self.__api_token = api_token

    def stock(self, symbol: list, optional_params: dict = None):
        request = RequestObject(self.__api_token)
        request.set_request_category('stock')
        symbol = reduce_list_to_string(symbol)
        request.add_single_query_string_param('symbol', symbol)
        if optional_params is not None:
            unwanted_keys = ['symbol', 'api_token']
            optional_params = filter_unwanted_params(
                optional_params,
                unwanted_keys
            )
            request.add_multiple_query_string_params(optional_params)
        return request.get()

    def mutual_fund(self, symbol: list, optional_params: dict = None):
        request = RequestObject(self.__api_token)
        request.set_request_category('mutualfund')
        symbol = reduce_list_to_string(symbol)
        request.add_single_query_string_param('symbol', symbol)
        if optional_params is not None:
            unwanted_keys = ['api_token', 'symbol']
            optional_params = filter_unwanted_params(
                optional_params,
                unwanted_keys
            )
            request.add_multiple_query_string_params(optional_params)
        return request.get()

    def intraday(
        self,
        symbol: str,
        time_interval: int,
        day_range: int,
        optional_params: dict = None
    ):
        req_params = {
            'symbol': symbol,
            'interval': time_interval,
            'range': day_range
        }
        request = RequestObject(self.__api_token)
        request.set_request_category('intraday')
        request.add_multiple_query_string_params(req_params)
        if optional_params is not None:
            unwanted_keys = [
                'api_token',
                'symbol',
                'interval',
                'range'
            ]
            optional_params = filter_unwanted_params(
                optional_params,
                unwanted_keys
            )
            request.add_multiple_query_string_params(optional_params)
        return request.get()

    def history(self, symbol: str, optional_params: dict = None):
        request = RequestObject(self.__api_token)
        request.set_request_category('history')
        request.add_single_query_string_param('symbol', symbol)
        if optional_params is not None:
            unwanted_keys = ['api_token', 'symbol']
            optional_params = filter_unwanted_params(
                optional_params,
                unwanted_keys
            )
            request.add_multiple_query_string_params(optional_params)
        return request.get()

    def history_multi_single_day(
        self,
        symbol: list,
        date: str,
        optional_params: dict = None
    ):
        symbol = reduce_list_to_string(symbol)
        req_params = {
            'symbol': symbol,
            'date': date,
        }
        request = RequestObject(self.__api_token)
        request.set_request_category('history_multi_single_day')
        request.add_multiple_query_string_params(req_params)
        if optional_params is not None:
            unwanted_keys = [
                'api_token',
                'symbol',
                'date',
            ]
            optional_params = filter_unwanted_params(
                optional_params,
                unwanted_keys
            )
            request.add_multiple_query_string_params(optional_params)
        return request.get()

    def forex(self, base: str):
        request = RequestObject(self.__api_token)
        request.set_request_category('forex')
        request.add_single_query_string_param('base', base)
        return request.get()

    def forex_history(
        self,
        base: str,
        convert_to: str,
        optional_params: dict = None
    ):
        req_params = {
            'base': base,
            'convert_to': convert_to
        }
        request = RequestObject(self.__api_token)
        request.set_request_category('forex_history')
        request.add_multiple_query_string_params(req_params)
        if optional_params is not None:
            unwanted_keys = [
                'api_token',
                'base',
                'convert_to'
            ]
            optional_params = filter_unwanted_params(
                optional_params,
                unwanted_keys
            )
            request.add_multiple_query_string_params(optional_params)
        return request.get()

    def forex_single_day(
        self,
        base: str,
        date: str,
        optional_params: dict = None
    ):
        req_params = {
            'base': base,
            'date': date
        }
        request = RequestObject(self.__api_token)
        request.set_request_category('forex_single_day')
        request.add_multiple_query_string_params(req_params)
        if optional_params is not None:
            unwanted_keys = [
                'api_token',
                'base',
                'date'
            ]
            optional_params = filter_unwanted_params(
                optional_params,
                unwanted_keys
            )
            request.add_multiple_query_string_params(optional_params)
        return request.get()

    def stock_search(self, search_term: str, params_as_dict: dict = None):
        request = RequestObject(self.__api_token)
        request.set_request_category('stock_search')
        request.add_single_query_string_param('search_term', search_term)
        if params_as_dict is not None:
            params_as_dict = filter_search_params(params_as_dict)
            request.add_multiple_query_string_params(params_as_dict)
        return request.get()


# member class
class RequestObject(AuthenticatedUrlBuilder):
    def __init__(self, api_token):
        super().__init__(api_token)
        self.__http = urllib3.PoolManager()

    def get(self):
        # return self.release_authenticated_url()
        url = self.release_authenticated_url()
        r = self.__http.request('GET', url)
        if r.status == 200:
            data = r.data.decode('utf-8')
            if self.check_if_output_is_json():
                data = json.loads(data)
            return data
        else:
            return Exception("How do Python exceptions work?")
