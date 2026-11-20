import pytest

from ex1 import fun


@pytest.mark.parametrize("a, b, expected", [
    (48, 18, 6),
    (18, 48, 6),
    (0, 5, 5),
    (5, 0, 5),
    (0, 0, 0),
    (-48, 18, 6),
    (48, -18, 6),
    (-48, -18, 6),
])
def test_fun_returns_positive_gcd(a, b, expected):
    assert fun(a, b) == expected
