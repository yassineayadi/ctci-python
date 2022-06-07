"""
Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in
ascending order, write a method to find an element.
"""


def binary_search(array: list[int], key: int, start: int, end: int):
    if start > end:
        return -1
    midpoint = (start + end) // 2
    if key == array[midpoint]:
        return midpoint
    elif key < array[midpoint]:
        return binary_search(array, key, start, midpoint - 1)
    else:
        return binary_search(array, key, midpoint + 1, end)


def reduce_search_space(
    matrix: list[list[int]], key: int
) -> tuple[tuple[int, int], tuple[int, int]]:
    cols = len(matrix[0])
    rows = len(matrix)
    start_col, end_col = 0, cols - 1
    start_row, end_row = 0, rows - 1
    first_column, last_column = [row[0] for row in matrix], [
        row[cols - 1] for row in matrix
    ]
    first_row, last_row = matrix[0], matrix[rows - 1]

    for idx, element in enumerate(first_column):
        if element > key:
            end_row = idx - 1
            break

    for idx, element in enumerate(last_column):
        if element > key:
            start_row = idx
            break

    for idx, element in enumerate(first_row):
        if element > key:
            end_col = idx - 1
            break

    for idx, element in enumerate(last_row):
        if element > key:
            start_col = idx
            break

    return (start_row, end_row), (start_col, end_col)


def simple_search(matrix: list[list[int]], key: int):
    "Iterates through each reach via binary search and returns row idx and column idx."
    for idx, array in enumerate(matrix):
        result = binary_search(array, key, 0, len(array) - 1)
        if result != -1:
            return idx, result
    return -1, -1


def advanced_search(matrix: list[list[int]], key: int):
    (start_row, end_row), (start_col, end_col) = reduce_search_space(matrix, key)
    for row in range(start_row, end_row + 1):
        array = matrix[row]
        result = binary_search(array, key, start_col, end_col)
        if result != -1:
            return row, result
    return -1, -1
