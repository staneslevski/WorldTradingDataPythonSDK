from WorldTradingData.url_builder.base import UrlBuilder


class AuthenticatedUrlBuilder(UrlBuilder):
    # Dunder methods
    def __init__(self, auth_token):
        super().__init__()
        self.__authToken = auth_token

    # Public Methods
    def release_authenticated_url(self):
        self.add_single_query_string_param('api_token', self.__authToken)
        return super().release_url()
