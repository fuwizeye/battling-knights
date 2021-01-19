from dataclasses import dataclass
from operator import attrgetter

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

    def drop_item(self, item, position):
        """Drops and returns equipped item

        Args:
            position (Pos): location on the board
        """
        if self.item:
            item = self.item
            position.items.append(item)
            position.items.sort(key=attrgetter('rank'))
            self.item = None
            return True
