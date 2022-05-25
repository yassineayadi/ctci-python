"""
**Eight Queens:**

Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
diagonals, not just the two that bisect the board.
"""
from copy import deepcopy


def is_valid_diagonal(grid: list[list], row: int, col: int):

    for r, c in zip(range(row + 1, 8), range(col + 1, 8)):
        if grid[r][c] == "Q":
            return False

    for r, c in zip(reversed(range(row)), reversed(range(col))):
        if grid[r][c] == "Q":
            return False

    for r, c in zip(reversed(range(row)), range(col + 1, 8)):
        if grid[r][c] == "Q":
            return False

    for r, c in zip(range(row + 1, 8), reversed(range(col))):
        if grid[r][c] == "Q":
            return False

    return True


def is_valid_row(grid: list[list], row: int):
    current_row = grid[row]
    for place in current_row:
        if place == "Q":
            return False
    return True


def is_valid_column(grid: list[list], col: int):
    current_column = [row[col] for row in grid]
    for place in current_column:
        if place == "Q":
            return False
    return True


def is_valid_placement(grid: list[list], row: int, col: int):
    return (
        is_valid_row(grid, row)
        and is_valid_column(grid, col)
        and is_valid_diagonal(grid, row, col)
    )


def position_is_valid(row, col, board):

    # Check if there are any queens in the rows above this position
    for cur_row in range(row):
        if board[cur_row][col] == "Q":
            return False

    # Check if there are any queens in the cols along this position
    # This is a sanity check since our main function shouldn't add more than
    # one queen at any row
    for cur_col in range(len(board[row])):
        if board[row][cur_col] == "Q":
            return False

    # Check if there is a queen in the upper left diagonal
    cur_row = row
    cur_col = col
    while cur_row >= 0 and cur_col >= 0:
        if board[cur_row][cur_col] == "Q":
            return False
        cur_row -= 1
        cur_col -= 1

    # Check if there is a queen in the upper right diagonal
    cur_row = row
    cur_col = col
    while cur_row >= 0 and cur_col < len(board[row]):
        if board[cur_row][cur_col] == "Q":
            return False
        cur_row -= 1
        cur_col += 1
    return True


def place_queen(grid: list[list], row: int, col: int) -> None:
    # queen = queens.pop()
    grid[row][col] = "Q"


def reset_piece(grid: list[list], row: int, col: int) -> None:
    grid[row][col] = "_"


def place_queens_on_board(grid: list[list]):
    rows = len(grid)
    columns = len(grid[0])
    arrangements = []

    def place(g: list[list], current_row: int):
        if current_row == rows:
            arrangements.append(deepcopy(g))
            return
        for c in range(columns):
            if is_valid_placement(g, current_row, c):
                place_queen(g, current_row, c)
                place(deepcopy(g), current_row + 1)
                reset_piece(g, current_row, c)

    place(grid, 0)
    return arrangements
