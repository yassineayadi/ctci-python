import pytest as pytest

from chapter01.p04 import functions

test_cases = [
    ("aba", True),
    ("aab", True),
    ("abba", True),
    ("aabb", True),
    ("a-bba", True),
    ("a-bba!", True),
    ("Tact Coa", True),
    ("jhsabckuj ahjsbckj", True),
    ("Able was I ere I saw Elba", True),
    ("So patient a nurse to nurse a patient so", False),
    ("Random Words", False),
    ("Not a Palindrome", False),
    ("no x in nixon", True),
    ("azAZ", True),
]


@pytest.mark.parametrize(["test_input", "expected"], test_cases)
def test_palindrome(test_input, expected):
    for f in functions:
        assert f(test_input) == expected