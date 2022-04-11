import pytest
from chapter01.p06 import functions

test_cases = [
    ("aabcccccaaa", "a2b1c5a3"),
    ("abcdef", "abcdef"),
    ("aabb", "aabb"),
    ("aaa", "a3"),
    ("a", "a"),
    ("", ""),
]


@pytest.mark.parametrize(["test_input", "expected"], test_cases)
def test_string_compression(test_input, expected):
    for f in functions:
        result = f(test_input)
        print(result)
        assert result == expected
