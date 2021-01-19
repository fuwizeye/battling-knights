from dataclasses import dataclass
from position import Position as Pos


@dataclass
class Item:

    name: str
    rank: int
    position: Pos
    attack: int = 0
    defence: int = 0
