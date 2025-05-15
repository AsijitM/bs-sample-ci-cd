import pytest

@pytest.mark.module("checkout")
@pytest.mark.priority("medium")
def test_checkout():
    pytest.xfail("Test intentionally marked as expected to fail")
    # assert False  # Simulating a failing test

def test_checkout_2():
    # This test is expected to pass
    assert True
    # assert False  # Uncommenting this line will make the test fail

def test_checkout_3():
    # This test is expected to pass
    assert True
    # assert False  # Uncommenting this line will make the test fail
def test_checkout_4():
    # This test is expected to pass
    assert True
    # assert False  # Uncommenting this line will make the test fail