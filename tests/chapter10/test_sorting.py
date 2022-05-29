from chapter10.sorting import (
    counting_sort,
    merge_sort,
    radix_sort, selection_sort,
    bubble_sort,
    quick_sort,
    )


def test_selection_sort():
    arr = [3, 4, 5, 1, 2]
    assert selection_sort(arr) == [1, 2, 3, 4, 5]


def test_bubble_sort():
    arr = [3, 4, 5, 1, 2]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5]


def test_merge_sort():
    arr = [3, 4, 5, 1, 2]
    assert merge_sort(arr) == [1, 2, 3, 4, 5]


def test_quick_sort():
    arr = [8, 7, 6, 1, 0, 9, 2]
    assert quick_sort(arr, 0, 6) == [0, 1, 2, 6, 7, 8, 9]


def test_counting_sort():
    arr = [8, 7, 6, 1, 0, 9, 2]
    assert counting_sort(arr) == [0, 1, 2, 6, 7, 8, 9]
    arr = [8, 7, 2, 1, 0, 9, 2]
    assert counting_sort(arr) == [0, 1, 2, 2, 7, 8, 9]

def test_radix_sort():
    arr = [121, 232, 254, 23, 1, 45, 488]
    assert radix_sort(arr) == [1, 23, 45, 121, 232, 254, 488]
