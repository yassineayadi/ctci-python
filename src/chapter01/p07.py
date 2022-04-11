from typing import List

Matrix = List[List]


def rotate(matrix: Matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])

    new_matrix = [[None] * number_of_columns for _ in range(number_of_rows)]

    for up, down in zip(range(number_of_rows), range(number_of_rows - 1, -1, -1)):
        for idx in range(number_of_rows):
            new_matrix[idx][up] = matrix[down][idx]

    return new_matrix


functions = [
    rotate,
]
