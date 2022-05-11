from chapter05.p03 import flip_bit_to_win


def test_flip_bit_to_win():
    assert flip_bit_to_win(1255) == 4
    assert flip_bit_to_win(1463) == 6
