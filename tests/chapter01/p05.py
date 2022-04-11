import pytest
from chapter01.p05 import functions

test_cases = [
    # no changes
    ("pale", "pale", True),
    ("", "", True),
    # one insert
    ("pale", "ple", True),
    ("ple", "pale", True),
    ("pales", "pale", True),
    ("ples", "pales", True),
    ("pale", "pkle", True),
    ("paleabc", "pleabc", True),
    ("", "d", True),
    ("d", "de", True),
    # one replace
    ("pale", "bale", True),
    ("a", "b", True),
    ("pale", "ble", False),
    # multiple replace
    ("pale", "bake", False),
    # insert and replace
    ("pale", "pse", False),
    ("pale", "pas", False),
    ("pas", "pale", False),
    ("pkle", "pable", False),
    ("pal", "palks", False),
    ("palks", "pal", False),
    # permutation with insert shouldn't match
    ("ale", "elas", False),
]


@pytest.mark.parametrize(["left_word", "right_word", "expected"], test_cases)
def test_is_one_away(left_word, right_word, expected):
    for f in functions:
        assert f(left_word, right_word) == expected
