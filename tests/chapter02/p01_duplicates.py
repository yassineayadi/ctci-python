import pytest
from chapter02.linkedlist import LinkedList
from chapter02.p01_duplicates import functions

test_cases = (
    ([], []),
    ([1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 2], [1, 2, 3]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3]),
)


@pytest.mark.parametrize(["test_input", "expected"], test_cases)
def test_remove_duplicates(test_input, expected):
    linkedlist = LinkedList.from_list(test_input)
    for f in functions:
        result = f(linkedlist)
        arr = result.to_list()
        print(result, expected)
        assert arr == expected
