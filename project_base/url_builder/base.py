class UrlBuilder:
    # Dunder methods
    def __init__(self):
        base_url = "https://api.worldtradingdata.com/api/v1"
        self.__base_url = base_url
        self.__query_string_params = {}
        self.__category = ""
        self.__url = base_url

    # Static methods
    @staticmethod
    def build_query_string_param(key, value):
        return ''.join([key, '=', value])

    # Private methods
    def __count_question_marks(self):
        return self.__url.count('?')

    def __build_category(self):
        if len(self.__category) != 0:
            return ''.join(['/', self.__category])
        else:
            return ''

    def __build_query_string(self):
        if len(self.__query_string_params) != 0:
            temp_qs_dict = self.__query_string_params.copy()
            query_string = '?'
            while len(temp_qs_dict) > 0:
                item = temp_qs_dict.popitem()
                key = item[0]
                value = item[1]
                pair_string = ''.join([key, '=', value])
                query_string = ''.join([query_string, pair_string])
                if len(temp_qs_dict) != 0:
                    query_string = ''.join([query_string, '&'])
            return query_string
        else:
            return ''

    def __build_url(self):
        base_url = self.__base_url
        category = self.__build_category()
        query_string = self.__build_query_string()
        return ''.join([base_url, category, query_string])

    # Interface function with no other purpose except to expose internal state
    def release_url(self):
        return self.__build_url()

    # Public Methods
    def add_single_query_string_param(self, key, value):
        qs_dict = {key: value}
        self.__query_string_params.update(qs_dict)

    def add_multiple_query_string_params(self, params_as_dict):
        for key in params_as_dict:
            self.add_single_query_string_param(key, params_as_dict[key])

    def has_query_string(self):
        return len(self.__query_string_params) > 0

    def set_request_category(self, category):
        self.__category = category
