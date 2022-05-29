"""
Search in Rotated Array:
Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array.
You may assume that the array was originally sorted in increasing order.
"""


def is_left_sorted(arr: list[int], start, midpoint):
    return arr[start] <= arr[midpoint]


def find_key_in_rotated_array(array: list[int], key: int, start: int, end: int):
    if start > end:
        return -1
    midpoint = (start + end) // 2
    if array[midpoint] == key:
        return midpoint

    if is_left_sorted(array, start, midpoint):
        if array[start] < key < array[midpoint]:
            return find_key_in_rotated_array(array, key, start, midpoint - 1)
        else:
            return find_key_in_rotated_array(array, key, midpoint + 1, end)
    else:
        if array[midpoint]< key < array[start]:
            return find_key_in_rotated_array(array, key, midpoint + 1, end)
        else:
            return find_key_in_rotated_array(array, key, start, midpoint - 1)
