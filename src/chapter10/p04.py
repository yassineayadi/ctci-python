"""
**Sorted Search, No Size:**
You are given an array like data structure Listy which lacks a size method. It does, however, have an elementAt ( i)
method that returns the element at index i in 0( 1) time. If i is beyond the bounds of the data structure, it returns -1.
(For this reason, the data structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
find the index at which an element x occurs. If x occurs multiple times, you may return any index.

(Page 161).
"""


def get_approximate_size_of_array(arr: list[int]):
    size = 2
    while arr[size] != -1:
        size = size * 2
    return size


def binary_search(arr: list[int], key: int, start: int, end: int):
    midpoint = (start + end) // 2
    if key == arr[midpoint]:
        return midpoint
    if start > end:
        return -1

    if arr[midpoint] == -1:
        # search left if out of bound
        return binary_search(arr, key, start, midpoint - 1)
    elif key > arr[midpoint]:
        # search right if key > midpoint
        return binary_search(arr, key, midpoint + 1, end)
    else:
        # search left if key < midpoint
        return binary_search(arr, key, start, midpoint - 1)


def binary_search_with_unknown_size(arr: list[int], key: int):
    size = get_approximate_size_of_array(arr)
    return binary_search(arr, key, 0, size)
