import sys
from src import markers
import pytest


def test_add():
    assert markers.add(1, 2) == 3


# @pytest.mark.skip(reason="No reason ") this skips if there is an exception
@pytest.mark.skip(reason="No reason ")
def test_add2():
    assert markers.add(1, 2) == 4


@pytest.mark.skipif(
    sys.version_info > (3, 11), reason="System version is - " + str(sys.version_info)
)
def test_add3():
    assert markers.add(1, 2) == 3


# if we are just changing the parameters evry time in tests, there is a better way to do it also
@pytest.mark.parametrize(
    "a,b,c", [(1, 2, 3), (2, 2, 4), ("a", "b", "ab")], ids=["1+2", "2+2", "a+b"]
)
def test_add4(a, b, c):
    assert markers.add(a, b) == c
