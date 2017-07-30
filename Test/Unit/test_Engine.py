import Engine.shortener
import pytest
import redis
from Errors import Exceptions

@pytest.fixture(scope="session", autouse=True)
def DB():
    return redis.Redis(host="localhost", port=6379, decode_responses=True)


@pytest.fixture(autouse=True)
def shortner():
    return Engine.shortener.Shortener()


def test_generate_key_pass():
    key = shortner().generate_key()
    assert len(key) == 8 and str.isalpha(key)


def test_key_not_in_db():
    key = "abc"
    assert shortner().confirm_not_in_db(key) is False


def test_key_in_db():
    key = "uYjPUWjP"
    assert shortner().confirm_not_in_db(key)


def test_return_value():
    key = "uYjPUWjP"
    assert shortner().get_value_from_key(key) == "http://www.google.com"

"""temporary key, used in testing"""
_temp_key = ""
_temp_value = "http://www.codeproject.com"

def test_set_value():
    _temp_key = test_generate_key_pass()

    assert shortner().set_value(_temp_key, _temp_value)

def test_set_value_malformed_url():
    with pytest.raises(Exceptions.UrlMalformedException):
        _temp_key = test_generate_key_pass()
        _temp_value = "abc"
        assert shortner().set_value(_temp_key, _temp_value)

