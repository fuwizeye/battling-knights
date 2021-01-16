from dataclasses import dataclass

from position import Position as Pos
from items import Item

# Status of the knight
knight_status = ('LIVE', 'DEAD', 'DROWNED')


@dataclass
class Knight:

    color: str
    position: Pos
    status: str = knight_status[0]
    attack_score: int = 1
    defence_score: int = 1
    item: Item = None

    def update_knight_status(self, statusIdx):
        """Updates the status of a knight

        Args:
            statusIdx (int): Index of knight  status
        """

        self.status = knight_status[statusIdx]
    
    def update_knight_position(self, pos):
        pass
