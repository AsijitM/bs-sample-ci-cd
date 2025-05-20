import pytest

@pytest.mark.module("login")
@pytest.mark.priority("high")
def test_login():
    assert True  # Simulating a passing test

def test_login_failure():
    assert False  # Simulating a failing test