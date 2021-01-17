from dataclasses import dataclass, field
from position import Position as Pos


@dataclass
class Arena:
    board: list = field(default_factory=list)

    def __init__(self):

        board = []
        for x in range(0, 8):
            row = [Pos(x, y) for y in range(0, 8)]
            board.append(tuple(row))
        self.board = tuple(board)

    def is_empty_square(self, location):
        """Checks if the given location is empty

        Args:
            location (Pos): location/position on the board
        """

        return (len(location.items) == 0) and (location.knight is None)

    def is_square_with_item(self, location):
        """[summary]

        Args:
            location ([type]): [description]
        """
        return len(location.items) > 0

    def is_square_with_a_knight(self, location):
        """Checks whether there is a knight on a given square
        """
        return location.knight is not None
