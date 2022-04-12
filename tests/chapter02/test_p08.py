import pytest

from chapter02.linkedlist import LinkedList
from chapter02.p08 import is_circular


def create_circular_reference(linkedlist: LinkedList):
    linkedlist.tail.next = linkedlist.head
    return linkedlist


test_cases = [
    (create_circular_reference(LinkedList.from_list(["A", "B", "C", "D", "E"])), True)
]


@pytest.mark.parametrize(["test_input", "expected"], test_cases)
def test_is_circular(test_input, expected):
    assert is_circular(test_input) is expected
