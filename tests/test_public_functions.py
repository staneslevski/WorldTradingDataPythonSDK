from project_base.public.base import WorldTradingData, RequestObject
from .utils import random_string


def test_request_object_has_all_attrs():
    # has property 'http'
    token = random_string(10)
    request_object = RequestObject(token)
    assert hasattr(request_object, 'http')


def test_world_trading_data_class():
    token = random_string(10)
    wtd = WorldTradingData(token)
