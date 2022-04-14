import pytest

from chapter03.p04 import SortedStack

test_cases = [
    ((4, 5, 6, 2, 1), (6, 5, 4, 2, 1)),
    (("a", "c", "d", "d"), ("d", "d", "c", "a")),
]


@pytest.mark.parametrize(["test_input", "expected"], test_cases)
def test_sortedstack(test_input, expected):
    sortedstack = SortedStack()
    sortedstack.push_multiple(*test_input)
    for sort, exp in zip(sortedstack, expected):
        assert sort == exp
