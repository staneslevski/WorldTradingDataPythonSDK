from project_base.url_builder.base import UrlBuilder

base_url = "https://api.worldtradingdata.com/api/v1"


# Test internal state
def test_init_function():
    url_builder = UrlBuilder()
    assert url_builder.url == base_url
    assert not url_builder.has_query_string


# Test interface functions on internal state
def test_interface():
    url_builder = UrlBuilder()
    assert url_builder.release_url() == base_url
    assert url_builder.release_has_query_string() == False


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
    assert url_builder.release_has_query_string() == True
