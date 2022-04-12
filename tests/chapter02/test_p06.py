import pytest

from chapter02.linkedlist import LinkedList
from chapter02.p06 import functions


test_cases = [
    ([1, 2, 3, 4, 3, 2, 1], True),
    ([1], True),
    (["a", "a"], True),
    ("aba", True),
    ([], True),
    ([1, 2, 3, 4, 5], False),
    ([1, 2], False),
]


@pytest.mark.parametrize(["test_input", "expected"], test_cases)
def test_is_palindrome(test_input, expected):
    linkedlist = LinkedList.from_list(test_input)
    for f in functions:
        assert f(linkedlist) == expected
