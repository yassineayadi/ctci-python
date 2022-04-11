from typing import List
from copy import deepcopy

Matrix = List[List]


def zero_matrix(matrix: Matrix):
    zero_cells = []
    for ridx, row in enumerate(matrix):
        for cidx, col in enumerate(row):
            if col == 0:
                zero_cells.append((ridx, cidx))

    zero_rows, zero_cols = {r for r, c in zero_cells}, {c for r, c in zero_cells}

    new_matrix = deepcopy(matrix)

    for ridx, row in enumerate(matrix):
        if ridx in zero_rows:
            new_matrix[ridx] = [0 for _ in range(len(matrix))]
        for cidx, col in enumerate(row):
            if cidx in zero_cols:
                new_matrix[ridx][cidx] = 0

    return new_matrix


functions = [zero_matrix]
