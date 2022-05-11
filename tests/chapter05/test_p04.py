from chapter05.p04 import next_largest_number, previous_smallest_number


def test_next_larger_number():
    assert next_largest_number(0b10110) == 0b11001


def test_next_smallest_number():
    assert previous_smallest_number(0b10110) == 0b10101
