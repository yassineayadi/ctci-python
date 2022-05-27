from chapter08.p13 import boolean_parenthesization
from operator import and_ as b_and, or_ as b_or, xor as b_xor


def test_boolean_parenthesization():
    values = [0, 1, 1, 1]
    operators = [b_and, b_or, b_xor]
    max_zeros, max_ones = boolean_parenthesization(values, operators)
    assert max_zeros == 2, max_ones == 1
    print(f"{max_zeros=}, {max_ones=}")
