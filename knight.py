from dataclasses import dataclass

from position import Position as Pos
from items import Item

# Status of the knight
knight_status = ('LIVE', 'DEAD', 'DROWNED')


@dataclass
class Knight:

    color: str
    position: Pos = None
    status: str = knight_status[0]
    attack_score: int = 1
    defence_score: int = 1
    item: Item = None

    def __post_init__(self):
        if not isinstance(self.position, Pos):
            raise ValueError('value not a position')

    def update_knight_status(self, statusIdx):
        """Updates the status of a knight

        Args:
            statusIdx (int): Index of knight  status
        """

        self.status = knight_status[statusIdx]

    def move(self, direction):

        # self.position.knights = None
        shift_x, shift_y = self.map_direction_to_location(direction)

        self.position.x += shift_x
        self.position.y += shift_y

        if (self.position.x < 0 or self.position.x > 7 or
                self.position.y < 0 or self.position.y > 7):

            self.kill_knight(2)

    def drop_item(self, position):
        """Drops and returns equipped item

        Args:
            position (Pos): location on the board
        """
        if self.item:
            item = self.item
            position.items.append(item)
            self.item = None
        return item
