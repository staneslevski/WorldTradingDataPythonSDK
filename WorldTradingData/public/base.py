import urllib3
import json
from WorldTradingData.authenticator.base import AuthenticatedUrlBuilder


class WorldTradingData:
    def __init__(self, api_token):
        self.__api_token = api_token

    def search_stock(self, search_term, params_as_dict=None):
        request = RequestObject(self.__api_token)
        request.set_request_category('stock_search')
        request.add_single_query_string_param('search_term', search_term)
        if params_as_dict is not None:
            request.add_multiple_query_string_params(params_as_dict)
        return request.get()


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
