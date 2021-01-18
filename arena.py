from dataclasses import dataclass, field
from operator import attrgetter
from position import Position as Pos

from fight import Battle


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

    def _assign_position(self, knight, new_position):

        knight.position = new_position
        new_position.knight = knight
        if knight.item:
            knight.item.position = new_position

    def _map_direction_to_location(self, direction):

        switcher = {
            'N': (-1, 0),
            'E': (0, 1),
            'S': (1, 0),
            'W': (0, -1)

        }

        x, y = switcher[direction]

        return x, y

    def move_knight(self, knight, direction):

        shift_x, shift_y = self._map_direction_to_location(direction)
        knight.position.x += shift_x
        knight.position.y += shift_y

        if (knight.position.x < 0 or knight.position.x > 7 or
                knight.position.y < 0 or knight.position.y > 7):

            item, last_position = Battle.kill_knight(2)

            # add logger to log item and position

        else:
            pos_x = knight.position.x
            pos_y = knight.position.y
            pos = self.board[pos_x][pos_y]

            if self.is_square_with_item(pos):
                self._assign_position(knight, pos)
                pos.items.sort(key=attrgetter('rank'))
                if not knight.item:
                    knight.item = pos.items[0]
