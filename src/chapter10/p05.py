"""
Sparse Search:
Given a sorted array of strings that is interspersed with empty strings, write a method to find the location of a given
string.
"""


def get_nearest_non_empty_entry(array: list[str], idx):
    distance = 0
    nearest_non_empty_entry = ""
    while nearest_non_empty_entry == "":
        if array[idx - distance] != "":
            return idx - distance
        if array[idx + distance] != "":
            return idx + distance
        distance += 1


def search_sorted_sparce_space(array: list[str], key: str, start: int, end: int):
    if start > end:
        return -1
    midpoint = (start + end) // 2
    if array[midpoint] == "":
        midpoint = get_nearest_non_empty_entry(array, midpoint)
    if key == array[midpoint]:
        return midpoint
    elif key < array[midpoint]:
        return search_sorted_sparce_space(array, key, start, midpoint - 1)
    else:
        return search_sorted_sparce_space(array, key, midpoint + 1, end)
