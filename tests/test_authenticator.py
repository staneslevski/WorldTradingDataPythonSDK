from project_base.authenticator.base import Authenticator
from . import utils


def test_authenticator_auth_token():
    auth = utils.random_string(10)
    authenticator = Authenticator(auth)
    assert authenticator.authToken == auth

# def test_