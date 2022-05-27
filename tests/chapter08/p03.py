from chapter08.p03 import find_magic_index, find_magic_index_with_non_distinct_values


def test_find_magic_index():
    arr = [-1, 1, 3, 6, 7]
    assert find_magic_index(arr, 0, 5) == 1


def test_find_magic_index_with_non_distinct_values():
    arr = [-1, 1, 1, 3, 3]
    assert find_magic_index_with_non_distinct_values(arr, 0, 5) == 1
