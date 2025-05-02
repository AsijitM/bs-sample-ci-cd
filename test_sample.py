import pytest

@pytest.mark.module("login")
@pytest.mark.priority("high")
def test_login():
    assert True

@pytest.mark.module("checkout")
@pytest.mark.priority("medium")
def test_checkout():
    assert True

