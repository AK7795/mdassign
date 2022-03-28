import m1
import pytest

@pytest.mark.skip(reason = "currently no need to execute this")
def test_ar():
    a = 10
    b = 5
    r = m1.ar(a, b)
    assert a*b == r

@pytest.mark.myproject
def test_pr():
    a = 10
    b = 5
    r = m1.pr(a, b)
    assert 2*(a+b) == r

@pytest.mark.myproject
def test_asq():
    b = 5
    r = m1.asq(b)
    assert b*b == r
