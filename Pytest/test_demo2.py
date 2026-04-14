import pytest


def test_first_me(setup):
    me = "Zero Patience"
    print(me)

@pytest.mark.smoke
@pytest.mark.skip
def test_second_me():
    a = 4
    b=3
    assert a + b == 7, "Test is failed"