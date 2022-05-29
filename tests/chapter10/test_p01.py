from chapter10.p01 import merge_two_sorted_arrays


def test_merge_smaller_into_larger_array_with_buffer():
    smaller = [5, 7, 9]
    larger = [1, 2, 3, 4, 6, 8, 10, None, None, None]
    assert merge_two_sorted_arrays(larger, smaller) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
