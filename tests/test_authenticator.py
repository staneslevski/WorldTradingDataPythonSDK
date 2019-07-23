from project_base.authenticator.base import AuthenticatedUrlBuilder
from . import utils
import re


base_url = "https://api.worldtradingdata.com/api/v1"


def test_authenticate_url():
    auth_token = utils.random_string(10)
    url_builder = AuthenticatedUrlBuilder(auth_token)
    url_builder.authenticate_url()
    url = url_builder.release_url()
    qs_param = ''.join(['api_token', '=', auth_token])
    pattern = re.compile(qs_param)
    matched_patterns = pattern.findall(url)
    assert len(matched_patterns) == 1
    pattern = re.compile('\?')
    matched_patterns = pattern.findall(url)
    assert len(matched_patterns) == 1


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
    url_builder.add_multiple_query_string_params([qs_param1, qs_param2])
    url_builder.authenticate_url()
    url = url_builder.release_url()
    assert url == ''.join([
        base_url,
        '?',
        qs_param1,
        '&',
        qs_param2,
        '&',
        auth_qs_param
    ])
    question_marks_list = pattern.findall(url)
    assert len(question_marks_list) == 1
