from chapter08.p05 import recursive_multiply


def test_recursive_multiply():
    assert recursive_multiply(20, 5) == 100
    assert recursive_multiply(7, 3) == 21
    assert recursive_multiply(4, 21) == 84
