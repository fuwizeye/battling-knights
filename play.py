import os
import sys
from items import Item
from arena import Arena
from knight import Knight

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class Play:

    @staticmethod
    def read_moves():
        """Reads moves from instruction file
        """
        with open('./moves.txt', 'r') as f:
            moves = [line.rstrip('\n') for line in f]
        if moves[0] == 'GAME-START':
            moves.pop(0)
        if moves[-1] == 'GAME-END':
            moves.pop(-1)

        moves_pairs = tuple(tuple(move.split(':')) for move in moves)

        return moves_pairs

    def set_board(self):

        self.arena = Arena()
        board_pos = self.arena.board

        pos_r = board_pos[0][0]
        pos_y = board_pos[0][7]
        pos_b = board_pos[7][0]
        pos_g = board_pos[7][7]

        pos_axe = board_pos[2][2]
        pos_dagger = board_pos[2][5]
        pos_magic_staff = board_pos[5][2]
        pos_helmet = board_pos[5][5]

        self.R = Knight('R', 'red', pos_r)
        self.Y = Knight('Y', 'yellow', pos_y)
        self.B = Knight('B', 'blue', pos_b)
        self.G = Knight('G', 'green', pos_g)

        self.axe = Item('A', 'axe', 1, pos_axe)
        self.dagger = Item('D', 'dagger', 2, pos_dagger)
        self.magic_staff = Item('M', 'magic_staff', 3, pos_magic_staff)
        self.helmet = Item('H', 'helmet', 4, pos_helmet)

        pos_r.knight = self.R
        pos_y.knight = self.Y
        pos_b.knight = self.B
        pos_g.knight = self.G

        pos_axe.items.append(self.axe)
        pos_dagger.items.append(self.dagger)
        pos_magic_staff.items.append(self.magic_staff)
        pos_helmet.items.append(self.helmet)

        return (
            self.arena,
            self.R,
            self.Y,
            self.B,
            self.G,
            self.axe,
            self.dagger,
            self.magic_staff,
            self.helmet

        )
