import Engine.shortener
import pytest
import redis


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





