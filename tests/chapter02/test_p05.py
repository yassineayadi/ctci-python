import pytest

from chapter02.linkedlist import LinkedList
from chapter02.p05 import sum_two_linkedlists

test_cases = (
    # all values can either be list of integer or integers
    # a, b, expected_sum
    ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
    # ([0], [0], [0]),
    # ([], [], []),
    ([3, 2, 1], [3, 2, 1], [6, 4, 2]),
    (123, 123, [2, 4, 6]),
    (123, 1, [1, 2, 4]),
    (1, 123, [1, 2, 4]),
)


@pytest.mark.parametrize(["left", "right", "expected_sum"], test_cases)
def test_sum_linkedlists(left, right, expected_sum):
    if isinstance(left, int):
        left_linkedlist = LinkedList.from_integers(left)
    else:
        left_linkedlist = LinkedList.from_list(left)

    if isinstance(right, int):
        right_linkedlist = LinkedList.from_integers(right)
    else:
        right_linkedlist = LinkedList.from_list(right)
    result = sum_two_linkedlists(left_linkedlist, right_linkedlist)
    assert result.to_list() == expected_sum
