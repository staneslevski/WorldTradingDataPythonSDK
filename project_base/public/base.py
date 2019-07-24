import urllib3
from project_base.authenticator.base import AuthenticatedUrlBuilder


class WorldTradingData:
    def __init__(self, api_token):
        self.__api_token = api_token

    def search_stock(self, search_term):
        request = RequestObject(self.__api_token)
        request.set_request_category('stock_search')


class RequestObject(AuthenticatedUrlBuilder):
    def __init__(self, api_token):
        super().__init__(api_token)
        self.__http = urllib3.PoolManager()
