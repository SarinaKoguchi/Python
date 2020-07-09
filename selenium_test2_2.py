# 別解
import pytest
from python2_test2_2 import is_leap_year

def test_is_leap_year():
    divisible_400 = 2000
    divisible_100 = 1900
    divisible_4 = 2020
    other = 2001

    result = is_leap_year(divisible_400)
    assert result == True

    result = is_leap_year(divisible_100)
    assert result == False

    result = is_leap_year(divisible_4)
    assert result == True

    result = is_leap_year(other)
    assert result == False