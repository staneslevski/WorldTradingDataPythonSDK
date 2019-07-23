import re


class UrlBuilder:
    # Dunder methods
    def __init__(self):
        self.url = "https://api.worldtradingdata.com/api/v1"

    # Static methods
    @staticmethod
    def build_query_string_param(key, value):
        return ''.join([key, '=', value])

    # Private methods
    def __add_qs_base(self):
        self.url = ''.join([self.url, "?"])

    def __add_ampersand(self):
        self.url = ''.join([self.url, '&'])

    def __count_question_marks(self):
        pattern = re.compile('\?')
        question_marks_list = pattern.findall(self.url)
        return len(question_marks_list)

    # Public Methods
    def add_single_query_string_param(self, query_string_param):
        num = self.__count_question_marks()
        if num == 0:
            self.__add_qs_base()
        else:
            self.__add_ampersand()

        self.url = ''.join([self.url, query_string_param])

    def add_multiple_query_string_params(self, params_as_list):
        for param in params_as_list:
            self.add_single_query_string_param(param)

    # Interface function with no other purpose except to expose internal state
    def release_url(self):
        return self.url

    # Interface function with no other purpose except to expose internal state
    def has_query_string(self):
        num = self.__count_question_marks()
        return num > 0

