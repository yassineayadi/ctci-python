"""
**Magic Index:**

A magic index in an array A [ 0 ••• n -1] is defined to be an index such that A[i] = i. Given a sorted array of
distinct integers, write a method to find a magic index, if one exists, in array A.

FOLLOW UP:
What if the values are not distinct?
"""


def find_magic_index(arr: list[int], start: int, end: int) -> int:
    if len(arr) == 0:
        return -1
    if start is None and end is None:
        start, end = 0, len(arr)
    middle = (end - start) // 2
    if middle == arr[middle]:
        return middle
    if arr[middle] > middle:
        return find_magic_index(arr, start, middle)
    if arr[middle] < middle:
        return find_magic_index(arr, middle, end)


def find_magic_index_with_non_distinct_values(
    arr: list[int], start: int, end: int
) -> int:
    if start is None and end is None:
        start, end = 0, len(arr)
    middle = (end - start) // 2
    if middle == arr[middle]:
        return middle
    left = find_magic_index_with_non_distinct_values(arr, start, middle)
    right = find_magic_index_with_non_distinct_values(arr, middle, end)
    return left or right
