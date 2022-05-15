"""
**Jigsaw**:

Implement an NxN jigsaw puzzle. Design the data structures and explain an algorithm to solve the puzzle.
You can assume that you have a fitsWi th method which, when passed two puzzle edges, returns true if the two
edges belong together.
"""

# Questions:
# Do we have an upper bound? (N*N)
# Are we considering different shapes of jigsaw puzzles or only rectangular ones?

# Objects
# * Piece (Corner Pieces, Side Pieces, Center Pieces)
# * Edge (Enum)
# * Component (multiple fitting pieces together)
# * Pile of Pieces
# * Puzzle (made of multiple pieces)


# Actions
# * PlugPiece
# * FitsTogether

from dataclasses import dataclass, field
from enum import Enum, IntEnum
from typing import Dict, List


class Shape(Enum):
    FLAT = "flat"
    INNER = "inner"
    OUTER = "outer"

    def get_opposite(self):
        if self == Shape.INNER:
            return Shape.OUTER
        if self == Shape.OUTER:
            return Shape.INNER


class PieceType(Enum):
    CORNER = "corner"
    SIDE = "side"
    CENTER = "center"


class Orientation(IntEnum):
    LEFT = 0
    RIGHT = 1
    TOP = 2
    BOTTOM = 3

    def get_opposite(self):
        if self == Orientation.LEFT:
            return Orientation.RIGHT
        if self == Orientation.RIGHT:
            return Orientation.LEFT
        if self == Orientation.TOP:
            return Orientation.BOTTOM
        if self == Orientation.BOTTOM:
            return Orientation.TOP


@dataclass
class Edge:
    parent_piece: "Piece"
    shape: Shape

    def fits_with(self, other: "Edge"):
        return self.shape.get_opposite() == other.shape


@dataclass
class Piece:
    edges: Dict[Orientation, Edge]

    @property
    def type(self):
        flat_edges = [edge for edge in self.edges.values() if edge.shape == Shape.FLAT]
        if len(flat_edges) == 2:
            return PieceType.CORNER
        if len(flat_edges) == 1:
            return PieceType.SIDE
        if len(flat_edges) == 0:
            return PieceType.CENTER

    @property
    def is_corner(self):
        return self.type == PieceType.CORNER

    @property
    def is_side(self):
        return self.type == PieceType.SIDE

    @property
    def is_center(self):
        return self.type == PieceType.CENTER

    def orient_edge(self, edge: Edge, orientation: Orientation):
        current_orientation = self.get_orientation(edge)
        number_of_rotations = orientation - current_orientation
        self.rotate_by(number_of_rotations)

    def get_orientation(self, edge: Edge):
        return next(o for o, e in self.edges if e == edge)

    def get_edge_with_orientation(self, orientation: Orientation):
        return self.edges[orientation]

    def rotate_by(self, number_of_rotations: int):
        new_orientations = {}
        for orientation, edge in self.edges.items():
            new_orientation = Orientation((orientation + number_of_rotations) % 4)
            new_orientations[new_orientation] = edge

    def get_matching_edge(self, target_edge: Edge):
        for edge in self.edges.values():
            if edge.fits_with(target_edge):
                return edge


@dataclass
class Puzzle:
    rows: int
    columns: int
    pieces: List[Piece]
    board: List[List[Piece | None]] = field(init=False)

    def __post_init__(self):
        self.reset_board()

    def reset_board(self):
        self.board = [[None for _ in range(self.rows)] for _ in range(self.columns)]

    @property
    def size(self):
        return self.rows * self.columns

    def set_edge_in_solution(
        self, edge: Edge, row: int, column: int, orientation: Orientation
    ):
        piece = edge.parent_piece
        piece.orient_edge(edge, orientation)
        self.place_piece(row, column, piece)

    @staticmethod
    def orient_top_left_corner(piece: Piece):
        if not piece.is_corner:
            return
        for idx in range(len(piece.edges)):
            orientation, next_orientation = Orientation(idx), Orientation((idx + 1) % 4)
            current_edge = piece.edges[orientation]
            next_edge = piece.edges[next_orientation]
            if current_edge.shape == Shape.FLAT and next_edge.shape == Shape:
                piece.orient_edge(current_edge, orientation.LEFT)

    def place_piece(self, row: int, col: int, piece: Piece):
        if not self.is_empty(row, col):
            self.return_piece(row, col)
        self.board[row][col] = piece
        self.pieces.pop(self.pieces.index(piece))

    def return_piece(self, row: int, column: int):
        piece = self.board[row][column]
        self.pieces.append(piece)
        self.board[row][column] = None

    def is_empty(self, row: int, col: int):
        return bool(self.board[row][col])

    def fit_next_edge(self, pieces_to_search: List[Piece], row: int, col: int):
        if row == 0 and col == 0:
            corner = pieces_to_search[0]
            self.orient_top_left_corner(corner)
            return True
        else:
            piece_to_match = (
                self.board[row - 1][0] if col == 0 else self.board[row][col - 1]
            )
            orientation_to_match = Orientation.BOTTOM if col == 0 else Orientation.RIGHT
            edge_to_match = piece_to_match.get_edge_with_orientation(
                orientation_to_match
            )

            edge = get_matching_edge(edge_to_match, pieces_to_search)
            if not edge:
                return False

            orientation = orientation_to_match.get_opposite()
            self.set_edge_in_solution(edge, row, col, orientation)
            return True


def get_matching_edge(edge: Edge, pieces: List[Piece]):
    for piece in pieces:
        matching_edge = piece.get_matching_edge(edge)
        if matching_edge:
            return matching_edge


def get_piece_list(row: int, col: int, rows: int, columns: int, grouped_pieces: Dict):
    if row == 0 and col == 0 or row == rows - 1 or col == columns - 1:
        return grouped_pieces["corner_pieces"]
    if row == 0 or col == 0 or row == rows - 1 or col == columns - 1:
        return grouped_pieces["side_pieces"]
    else:
        return grouped_pieces["center_pieces"]


def solve_jigsaw_puzzle(puzzle: Puzzle):
    """Solves a jigsaw puzzle.

    Steps:
    (1) group all pieces 3 different groups for (a) corner pieces (b) side pieces (c) center pieces
    (2) loop over each cell in the board
    (3) for every piece and edge which is set, loop over the appropriate group to find a matching piece.

    The first piece can be arbitrarily set (we choose the top left corner).
    """
    grouped_pieces = {
        "corner_pieces": [piece for piece in puzzle.pieces if piece.is_corner],
        "side_pieces": [piece for piece in puzzle.pieces if piece.is_side],
        "center_pieces": [piece for piece in puzzle.pieces if piece.is_center],
    }
    rows = puzzle.rows
    columns = puzzle.columns

    for col in range(columns):
        for row in range(rows):
            pieces = get_piece_list(
                col, row, puzzle.rows, puzzle.columns, grouped_pieces
            )
            if not puzzle.fit_next_edge(pieces, row, col):
                return False
    return True
