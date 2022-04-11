import pytest

from chapter01.p09 import functions

test_cases = [
    ("waterbottle", "erbottlewat", True),
    ("foo", "bar", False),
    ("foo", "foofoo", False),
]


@pytest.mark.parametrize(["left", "right", "expected"], test_cases)
def test_is_substring(left, right, expected):
    for f in functions:
        assert f(left, right) == expected
