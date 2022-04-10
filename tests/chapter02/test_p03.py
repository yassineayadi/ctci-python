import pytest
from chapter02.p03 import functions
from chapter02.linkedlist import LinkedList

tests_cases = [[(10, 20, 30, 40, 50, 60), 30]]


@pytest.mark.parametrize(["test_input", "expected"], tests_cases)
def test_get_middle_node(test_input, expected):
    linkedlist = LinkedList.from_list(test_input)
    for f in functions:
        assert f(linkedlist) == expected
