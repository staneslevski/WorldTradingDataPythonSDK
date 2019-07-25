import re
from WorldTradingData.url_builder.base import UrlBuilder

base_url = "https://api.worldtradingdata.com/api/v1"


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
    url_builder.add_single_query_string_param(key, value)
    url = url_builder.release_url()
    assert url == ''.join([base_url, "?", qs_param])
    assert url_builder.has_query_string()


def test_add_multiple_query_string_params():
    pattern = re.compile('\?')
    url_builder = UrlBuilder()
    starting_url = url_builder.release_url()
    question_marks_list = pattern.findall(starting_url)
    assert len(question_marks_list) == 0
    qs_dict = {
        "key4": "value4",
        "key3": "value3",
        "key2": "value2",
        "key1": "value1",
    }
    test_qs = '?key1=value1&key2=value2&key3=value3&key4=value4'
    url_builder.add_multiple_query_string_params(qs_dict)
    url = url_builder.release_url()
    assert url == ''.join([base_url, test_qs])
    question_marks_list = pattern.findall(url)
    assert len(question_marks_list) == 1


def test_set_request_category():
    url_builder = UrlBuilder()
    category = "stock"
    url_builder.set_request_category(category)
    url = url_builder.release_url()
    base_length = len(base_url)
    rem_url = url[base_length:]
    cat_length = len(category)
    assert rem_url[0:cat_length + 1] == ''.join(['/', category])


def test_check_if_output_is_json():
    url_builder = UrlBuilder()
    category = "stock"
    url_builder.set_request_category(category)
    assert url_builder.check_if_output_is_json()
    url_builder.add_single_query_string_param('output', 'json')
    assert url_builder.check_if_output_is_json()
    url_builder.add_single_query_string_param('output', 'csv')
    assert not url_builder.check_if_output_is_json()


