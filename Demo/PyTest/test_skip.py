import pytest
import sys


@pytest.mark.skip(reason="Not implemented")
def test_dem_1():
    assert True


@pytest.mark.skipif(sys.version_info < (3,6), reason="requires Python 3.6 or higher")
def test_dem_2():
    assert True


def test_dem_3():
    assert True
