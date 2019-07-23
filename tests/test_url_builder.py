import re
from project_base.url_builder.base import UrlBuilder

base_url = "https://api.worldtradingdata.com/api/v1"


# Test internal state
def test_init_function():
    url_builder = UrlBuilder()
    assert url_builder.url == base_url


# Test interface functions on internal state
def test_interface():
    url_builder = UrlBuilder()
    assert url_builder.release_url() == base_url
    assert not url_builder.has_query_string()


def test_build_query_string_param():
    key = "key"
    value = "value"
    qs_param = UrlBuilder.build_query_string_param(key, value)
    assert qs_param == "key=value"


def test_add_single_query_string_param():
    url_builder = UrlBuilder()
    key = "key"
    value = "value"
    qs_param = UrlBuilder.build_query_string_param(key, value)
    url_builder.add_single_query_string_param(qs_param)
    url = url_builder.release_url()
    assert url == ''.join([base_url, "?", qs_param])
    assert url_builder.has_query_string()


def test_add_multiple_query_string_params():
    pattern = re.compile('\?')
    url_builder = UrlBuilder()
    starting_url = url_builder.release_url()
    question_marks_list = pattern.findall(starting_url)
    assert len(question_marks_list) == 0
    key1 = "key1"
    key2 = "key2"
    value1 = "value1"
    value2 = "value2"
    qs_param1 = UrlBuilder.build_query_string_param(key1, value1)
    qs_param2 = UrlBuilder.build_query_string_param(key2, value2)
    url_builder.add_multiple_query_string_params([qs_param1, qs_param2])
    url = url_builder.release_url()
    assert url == ''.join([base_url, '?', qs_param1, ',', qs_param2])
    question_marks_list = pattern.findall(url)
    assert len(question_marks_list) == 1
