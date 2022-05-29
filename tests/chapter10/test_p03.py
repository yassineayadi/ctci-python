from chapter10.p03 import find_key_in_rotated_array


def test_find_key_in_sorted_but_pivoted_array():
    array = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    key = 1
    assert find_key_in_rotated_array(array, key, 0, len(array) - 1) == 3
    key = 10
    assert find_key_in_rotated_array(array, key, 0, len(array) - 1) == -1
