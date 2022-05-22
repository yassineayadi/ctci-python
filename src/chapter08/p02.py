"""
**Robot in a Grid:**

Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can only move in two directions,
right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to
 find a path for the robot from the top left to the bottom right.
"""
from typing import Tuple


def is_free(grid, x: int, y: int) -> bool:
    if x < len(grid) and y < len(grid[0]):
        return grid[x][y]
    else:
        return False


def right(row: int, col: int) -> Tuple[int, int]:
    return row, col + 1


def down(row: int, col: int) -> Tuple[int, int]:
    return row + 1, col


def set_parents(parents, row: int, col: int, parent_row: int, parent_col: int) -> None:
    parents[row][col] = (parent_row, parent_col)


def next_cell(parents, grip, row: int, col: int):
    if is_free(grip, *right(row, col)):
        set_parents(parents, *right(row, col), row, col)
        return right(row, col)
    if is_free(grip, *down(row, col)):
        set_parents(parents, *down(row, col), row, col)
        return down(row, col)
    else:
        tombstone(grip, row, col)
        return parents[row][col]


def tombstone(grid, x: int, y: int):
    grid[x][y] = False


def get_path(grid: list[list[int]]):
    r, c = 0, 0
    rows = len(grid)
    columns = len(grid[0])
    parents: list[list[tuple]] = [[None] * columns for _ in range(rows)]  # noqa
    parents[0][0] = (0, 0)
    while r != rows - 1 or c != columns - 1:
        next_r, next_c = next_cell(parents, grid, r, c)
        r, c = next_r, next_c

    path = []
    while r != 0 or c != 0:
        cell = parents[r][c]
        path.append(cell)
        r, c = cell

    return path[::-1]
