import pytest

from chapter01.p08 import functions

test_cases = [
    (
        [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0],
        ],
    )
]


@pytest.mark.parametrize(["test_input", "expected"], test_cases)
def test_zero_matrix(test_input, expected):
    for f in functions:
        assert f(test_input) == expected
