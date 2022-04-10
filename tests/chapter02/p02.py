import pytest

from chapter02.p02 import functions
from chapter02.linkedlist import LinkedList

test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)


@pytest.mark.parametrize(["test_input", "kth", "expected"], test_cases)
def test_remove_kth_to_the_last(test_input, kth, expected):
    linkedlist = LinkedList.from_list(test_input)
    for f in functions:
        result = f(linkedlist, kth)
        assert result.value == expected
