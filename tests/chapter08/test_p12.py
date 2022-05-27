from chapter08.p12 import (
    place_queens_on_board,
    is_valid_placement,
    is_valid_row,
    is_valid_column,
    is_valid_diagonal,
)


def test_place_eight_queens():
    grid = [["_"] * 8 for _ in range(8)]
    arrangements = place_queens_on_board(grid)
    assert len(arrangements) == 92
    print(f"{len(arrangements)=}")


def test_is_valid_row():
    grid: list[list[str]] = [["_"] * 8 for _ in range(8)]  # noqa
    grid[0][0] = "Q"
    assert is_valid_row(grid, 0) is False


def test_is_valid_column():
    grid: list[list[str]] = [["_"] * 8 for _ in range(8)]  # noqa
    grid[0][0] = "Q"
    assert is_valid_column(grid, 0) is False


def test_is_valid_diagonal():
    grid: list[list[str]] = [["_"] * 8 for _ in range(8)]  # noqa
    grid[0][0] = "Q"
    assert is_valid_diagonal(grid, 7, 7) is False
