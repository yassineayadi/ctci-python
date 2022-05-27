"""
**Othello:**

Othello is played as follows: Each Othello piece is white on one side and black on the other. When a piece is surrounded
by its opponents on both the left and right sides, or both the top and bottom, it is said to be captured and its color
is flipped. On your turn, you must capture at least one of your opponent's pieces. The game ends when either user has
no more valid moves. The win is assigned to the person with the most pieces. Implement the object-oriented design for Othello.
"""

# Objects:
# * Piece
# * Board
# * Player

# Actions:
# * Place Piece
# * Flip color

# Description:
# * Each player starts with a certain number of pieces
# * Each player places a piece on the board one after the other

# Questions:
# * What is a valid move?
# * How big is the board?

from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List


class Color(Enum):
    BLACK = auto()
    WHITE = auto()

    def opposite(self):
        if self == Color.BLACK:
            return Color.WHITE
        else:
            return Color.BLACK


@dataclass
class Piece:
    color: Color

    def flip(self):
        self.color = self.color.opposite()


@dataclass
class Player:
    remaining_pieces: List[Piece]

    def place_piece(self):
        return self.remaining_pieces.pop(0)


@dataclass
class Game:
    NUMBER_OF_PLAYERS = 2
    size: int
    board: List[List[Piece | None]] = field(init=False)
    players: List[Player] = field(init=False)

    def __post_init__(self):
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.players = [Player(1), Player(2)]

    def wins(self):
        if all(player.remaining_pieces == 0 for player in self.players):
            white_count, black_count = self.count_colors()
            if white_count > black_count:
                print(f"White win with {white_count} points")
            else:
                print(f"Black win with {black_count} points")

    def count_colors(
        self,
    ):
        white_count = 0
        black_count = 0
        for x in range(self.size):
            for y in range(self.size):
                if not self.is_empty(x, y):
                    piece = self.board[x][y]
                    if piece.color == Color.BLACK:
                        black_count += 1
                    elif piece.color == Color.WHITE:
                        white_count += 1
        return white_count, black_count

    def place_piece(self, x: int, y: int, player: Player):
        if self.is_empty(x, y):
            piece = player.place_piece()
            self.board[x][y] = piece
            self.evaluate_board()

    def evaluate_board(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.check_if_captured(x, y):
                    self.flip_piece(x, y)

    def flip_piece(self, x: int, y: int):
        piece = self.board[x][y]
        piece.flip()

    def check_if_captured(self, x: int, y: int):
        current_piece = self.board[x][y]
        if current_piece is not None:
            vertical_neighbours = self.vertical_neighbours(x, y)
            horizontal_neighbours = self.horizontal_neighbours(x, y)
            v_number_of_opposite_colors = [
                1
                for n in vertical_neighbours
                if n.color.opposite() == current_piece.color
            ]
            h_number_of_opposite_colors = [
                1
                for n in horizontal_neighbours
                if n.color.opposite() == current_piece.color
            ]
            if any(
                [
                    sum(v_number_of_opposite_colors) >= 2,
                    sum(h_number_of_opposite_colors) >= 2,
                ]
            ):
                return True
        return False

    def vertical_neighbours(self, x: int, y: int):
        return [
            self.top_neighbour(x, y),
            self.bottom_neighbour(x, y),
        ]

    def horizontal_neighbours(self, x: int, y: int):
        return [self.right_neighbour(x, y), self.left_neighbour(x, y)]

    def top_neighbour(self, x: int, y: int):
        return self.board[x][y + 1]

    def bottom_neighbour(self, x: int, y: int):
        return self.board[x][y - 1]

    def left_neighbour(self, x: int, y: int):
        return self.board[x - 1][y]

    def right_neighbour(self, x: int, y: int):
        return self.board[x + 1][y]

    def is_empty(self, x: int, y: int):
        return bool(self.board[x][y] is None)
