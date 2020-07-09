import pytest
from python2_test2 import check_leap_year

def test_check_leap_year():
    leep_year = 2020
    not_leep_year = 2019

    result = check_leap_year(leep_year)
    assert result == True

    result = check_leap_year(not_leep_year)
    assert result == False