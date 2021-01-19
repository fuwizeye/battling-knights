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

        self.red_knight = Knight('R', pos_r)
        self.yellow_knight = Knight('Y', pos_y)
        self.blue_knight = Knight('B', pos_b)
        self.green_knight = Knight('G', pos_g)

        self.axe = Item('A', 1, pos_axe)
        self.dagger = Item('D', 2, pos_dagger)
        self.magic_staff = Item('H', 3, pos_magic_staff)
        self.helmet = ('M', 4, pos_helmet)

        pos_r.knight = self.red_knight
        pos_y.knight = self.yellow_knight
        pos_b.knight = self.blue_knight
        pos_g.knight = self.green_knight

        pos_axe.append(self.axe)
        pos_dagger.append(self.dagger)
        pos_magic_staff.append(self.magic_staff)
        pos_helmet.append(self.helmet)

        return (
            self.arena,
            self.red_knight,
            self.yellow_knight,
            self.blue_knight,
            self.green_knight,
            self.axe,
            self.dagger,
            self.magic_staff,
            self.helmet

        )
