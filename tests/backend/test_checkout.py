import pytest

@pytest.mark.module("checkout")
@pytest.mark.priority("medium")
def test_checkout():
    pytest.xfail("Test intentionally marked as expected to fail")
    # assert False  # Simulating a failing test
