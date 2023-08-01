import pytest
from problem1_func import find_gcd

@pytest.mark.parametrize("a, b, denom",
                         [(6, 3, 3), (8, 4, 4), (8, 6, 2),
                          (60, 35, 5), (56, 8, 8), (8, 56, 8)])

def test_gcd(a, b, denom):
    assert find_gcd(a, b) == denom

@pytest.mark.parametrize("a, b, denom",
                         [("", True, 3), ("a", "b", 0), ("six", "one", 1), (0, 2, 0), (-4, -2, 2)])

def test_gcd_arg_types(a, b, denom):
    with pytest.raises(Exception):
        find_gcd(a, b)
