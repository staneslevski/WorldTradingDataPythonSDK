class UrlBuilder:

    # Dunder methods
    def __init__(self):
        self.url = "https://api.worldtradingdata.com/api/v1"
        self.has_query_string = False

    # Static methods
    @staticmethod
    def build_query_string_param(key, value):
        return ''.join([key, '=', value])

    # Private methods
    def __add_qs_base(self):
        self.url = ''.join([self.url, "?"])
        self.has_query_string = True

    # Public Methods
    def add_single_query_string_param(self, query_string_param):
        self.__add_qs_base()
        self.url = ''.join([self.url, query_string_param])

    def add_multiple_query_string_params(self, params_as_list):
        pass

    def release_url(self):
        return self.url

    # Should be refactored to just return a regex test on url
    def release_has_query_string(self):
        return self.has_query_string

