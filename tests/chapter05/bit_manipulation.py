from chapter05.p01 import clear_at, clear_from_to, insert_into


def test_clear_at():
    assert clear_at(4, 0) == 4
    assert clear_at(4, 1) == 4
    assert clear_at(4, 2) == 0


def test_clear_from_to():
    val = clear_from_to(1100, 2, 6)
    print(val)


def test_insert_into():
    larger = int("10000000000", 2)
    smaller = int("10011", 2)
    expected = int("10001001100", 2)
    val = insert_into(
        larger=larger,
        smaller=smaller,
        start=2,
        stop=6,
    )
    assert val == expected
