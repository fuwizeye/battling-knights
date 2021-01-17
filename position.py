from dataclasses import dataclass, field


@dataclass
class Position:
    """Knight/item position on the board
    """
    x: int
    y: int
    knight: dict = None
    items: list = field(default_factory=list)
