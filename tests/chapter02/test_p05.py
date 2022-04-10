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
    (123, 123, 246),
    (123, 1, 124),
    (1, 123, 124),
)


@pytest.mark.parametrize(["left_list", "right_list", "expected_sum"], test_cases)
def test_sum_linkedlists(left_list, right_list, expected_sum):
    left_linkedlist = LinkedList.from_list(left_list)
    right_linkedlist = LinkedList.from_list(right_list)
    result = sum_two_linkedlists(left_linkedlist, right_linkedlist)
    assert result.to_list() == expected_sum
