"""
**Minesweeper:**

Design and implement a text-based Minesweeper game. Minesweeper is the classic single-player computer game where an NxN
grid has B mines (or bombs) hidden across the grid. The remaining cells are either blank or have a number behind them.
The numbers reflect the number of bombs in the surrounding eight cells. The user then uncovers a cell. If it is a bomb,
the player loses. If it is a number, the number is exposed. If it is a blank cell, this cell and all adjacent blank cells
(up to and including the surrounding numeric cells) are exposed. The player wins when all non-bomb cells are exposed.
The player can also flag certain places as potential bombs. This doesn't affect game play, other than to block the user
from accidentally clicking a cell that is thought to have a bomb.

(Tip for the reader: if you're not familiar with this game, please play a few rounds on line first.)
"""

# Objects
# Mine
# Number
# Blank
# Player
# Cell (Hidden/Shown/Marked)

# Board (NxN)

# Actions:
# Player can mark a cell or uncover a cell
# If a cell is a bomb the player loose
# if there are no more hidden cells which are not bombs the player wins

from dataclasses import dataclass
from enum import Enum
from typing import List


class Value:
    pass


class Number(Value):

    def __init__(self,val):
        self.val = val


class Blank(Value):
    pass


class Bomb(Value):
    pass


class State(Enum):
    SHOWN = "Shown"
    HIDDEN = "Hidden"


@dataclass
class Cell:
    state: State
    value: Value

    def uncover(self):
        self.state = State.SHOWN
        return self.value


class Difficulty(Enum):
    EASY = 5
    MEDIUM = 10
    HARD = 20


def map_values(cell: Cell):
    if cell.state == State.HIDDEN:
        return "0x00002B1C"
    if isinstance(cell.value, Number):
        return cell.value
    if isinstance(cell.value, Bomb):
        return "B"
    if isinstance(cell.value, Blank):
        return " "

def print_matrix(matrix: List[List]):
    for row in matrix:
        print("\n")
        for val in row:
            print(map_values(val),sep=" ", end="")


class Game:
    board: List[List[Cell | None]]

    def __init__(self, size: int, difficulty: Difficulty):
        self.size = size
        self.difficulty = difficulty
        self._init_board(size)

    def _init_board(self, size: int):
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def uncover(self, x: int, y: int):
        cell = self.board[x][y]
        value = cell.uncover()
        if isinstance(value,Bomb):
            print("You lost.")

    def show_board(self):
        print_matrix(self.board)

    
