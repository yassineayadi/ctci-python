from chapter05.p06 import get_numbers_of_bits_to_convert


def test_numbers_of_bits_to_convert():
    a = 0b11101  # 29
    b = 0b01111  # 15
    assert get_numbers_of_bits_to_convert(a, b) == 2
