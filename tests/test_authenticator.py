from WorldTradingData.authenticator.base import AuthenticatedUrlBuilder
from . import utils
import re


base_url = "https://api.worldtradingdata.com/api/v1"


def test_release_authenticated_url():
    auth_token = utils.random_string(10)
    url_builder = AuthenticatedUrlBuilder(auth_token)
    url = url_builder.release_authenticated_url()
    qs_param = ''.join(['api_token', '=', auth_token])
    pattern = re.compile(qs_param)
    matched_patterns = pattern.findall(url)
    assert len(matched_patterns) == 1
    assert url.count('?') == 1


def test_add_multiple_query_string_params():
    auth_token = utils.random_string(10)
    auth_qs_param = ''.join(['api_token', '=', auth_token])
    pattern = re.compile('\?')
    url_builder = AuthenticatedUrlBuilder(auth_token)
    starting_url = url_builder.release_url()
    question_marks_list = pattern.findall(starting_url)
    assert len(question_marks_list) == 0
    key1 = "key1"
    key2 = "key2"
    value1 = "value1"
    value2 = "value2"
    qs_param1 = AuthenticatedUrlBuilder.build_query_string_param(key1, value1)
    qs_param2 = AuthenticatedUrlBuilder.build_query_string_param(key2, value2)
    url_builder.add_multiple_query_string_params({key2: value2, key1: value1})
    url = url_builder.release_authenticated_url()
    assert url == ''.join([
        base_url,
        '?',
        auth_qs_param,
        '&',
        qs_param1,
        '&',
        qs_param2
    ])
    question_marks_list = pattern.findall(url)
    assert len(question_marks_list) == 1
