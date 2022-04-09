import pytest as pytest

from chapter01.p01_is_unique import functions

test_cases = [
    ("abcd", True),
    ("s4fad", True),
    ("", True),
    ("23ds2", False),
    ("hb 627jh=j ()", False),
    ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
    ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
]


@pytest.mark.parametrize(["test_input", "expected"], test_cases)
def test_functions(test_input, expected):
    for f in functions:
        assert f(test_input) == expected
