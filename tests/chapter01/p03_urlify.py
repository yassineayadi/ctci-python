import pytest

from chapter01.p03_urlify import functions

test_cases = [
    ("much ado about nothing      ", "much%20ado%20about%20nothing"),
    ("Mr John Smith       ", "Mr%20John%20Smith"),
    (" a b    ", "%20a%20b"),
    (" a b       ", "%20a%20b%20"),
]


@pytest.mark.parametrize(["test_input", "expected"], test_cases)
def test_functions(test_input, expected):
    for f in functions:
        assert f(test_input) == expected
