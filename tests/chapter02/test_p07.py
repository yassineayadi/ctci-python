import pytest

from chapter02.linkedlist import LinkedList
from chapter02.p07 import has_intersection

test_cases = [
    (
        LinkedList.from_list([10, 11, 12, 13, 14, 15, 1, 2, 3]),
        LinkedList.from_list([20, 21, 22, 1, 2, 3]),
        True,
    )
]


@pytest.mark.parametrize(["left", "right", "expected"], test_cases)
def test_has_intersection(left, right, expected):
    assert has_intersection(left, right) is expected
