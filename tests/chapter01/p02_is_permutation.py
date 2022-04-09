import pytest

from chapter01.p02_is_permutation import functions

test_cases = (
    ("dog", "god", True),
    ("abcd", "bacd", True),
    ("3563476", "7334566", True),
    ("wef34f", "wffe34", True),
    ("dogx", "godz", False),
    ("abcd", "d2cba", False),
    ("2354", "1234", False),
    ("dcw4f", "dcw5f", False),
    ("DOG", "dog", False),
    ("dog ", "dog", False),
    ("aaab", "bbba", False),
)


@pytest.mark.parametrize(["left", "right", "expected"], test_cases)
def test_functions(left, right, expected):
    for f in functions:
        assert f(left, right) == expected
