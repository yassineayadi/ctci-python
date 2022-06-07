"""
Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal
to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent
integers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an
array of integers, sort the array into an alternating sequence of peaks and valleys.
"""


def is_peak(array: list[int], idx: int) -> bool:
    prv, nxt = idx - 1 if idx > 0 else None, idx + 1 if idx + 1 < len(array) else None
    if prv is not None and nxt is not None:
        return array[prv] <= array[idx] >= array[nxt]
    if prv:
        return array[prv] <= array[idx]
    if nxt:
        return array[idx] >= array[nxt]


def swap(array, a: int, b: int):
    array[a], array[b] = array[b], array[a]


def sort_array_into_peaks_and_valleys(array: list[int]):
    size = len(array)
    for idx in range(size):
        if idx % 2 == 0:
            if not is_peak(array, idx):
                prv, nxt = (
                    idx - 1 if idx > 0 else None,
                    idx + 1 if idx + 1 < len(array) else None,
                )
                if prv is not None and nxt is not None:
                    max_neighbour = prv if array[prv] > array[nxt] else nxt
                    swap(array, idx, max_neighbour)
    return array
