from project_base.url_builder.base import UrlBuilder


class AuthenticatedUrlBuilder(UrlBuilder):
    # Dunder methods
    def __init__(self, auth_token):
        super().__init__()
        self.__authToken = auth_token

    # Private methods
    def __build_auth_token_qs_param(self):
        key = "api_token"
        value = self.__authToken
        return self.build_query_string_param(key, value)

    # Public Methods
    def release_authenticated_url(self):
        self.add_single_query_string_param('api_token', self.__authToken)
        return super().release_url()
