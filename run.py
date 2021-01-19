from play import Play


play_game = Play()


def run():
    moves = play_game.read_moves()

    for (knight, direction) in moves:
        knight = play_game.knight
        play_game.arena.move_knight(knight, direction)


if __name__ == '__main__':
    arena, *rest = play_game.set_board()
    play_game.arena.render_arena()
    run()
