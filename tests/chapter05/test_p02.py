import pytest

from chapter05.p02 import float_to_binary_form, PrecisionError

test_cases = [
    (12.375, "01000001010001100000000000000000"),
    (-0.375, "10111110110000000000000000000000"),
]


@pytest.mark.parametrize(["float_number", "binary_form"], test_cases)
def test_bits_to_string(float_number, binary_form):
    assert float_to_binary_form(float_number) == binary_form
    print(binary_form)


def test_bits_to_string_raise_precision_error():
    float_number = 0.10
    with pytest.raises(PrecisionError):
        float_to_binary_form(float_number)
