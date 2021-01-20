from play import Play
from json import dumps

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s:%(message)s')

stream_handler = logging.StreamHandler()

logger.addHandler(stream_handler)

play_game = Play()


def run():
    moves = play_game.read_moves()

    for knight, direction in moves:
        knight = getattr(play_game, knight)
        play_game.arena.move_knight(knight, direction)


def save_state(knights, items):

    game_results = {}
    for knight in knights:
        knight_score = [
            [knight.position.x, knight.position.y]
            if knight.position else None,
            knight.status
        ]
        if knight.item:
            knight_score.extend(
                [knight.item.full_name,
                 knight.attack_score,
                 knight.base_Score
                 ]
            )
        else:
            knight_score.extend([
                None,
                knight.attack_score,
                knight.defence_score
            ])
        game_results[knight.name] = knight_score

    for item in items:
        item_loc = (
            [item.position.x, item.position.y]
            if item.position else None,
            item.position.knight is not None
        )
        game_results[item.full_name] = item_loc
    return game_results


def write_to_file(state):
    logger.info('Game finished! \nWriting results on final_state.json')
    with open('./final_state.json.', 'w') as f:
        f.writelines(dumps(state))


if __name__ == '__main__':
    (
        arena,
        knight_r,
        knight_y,
        knight_b,
        knight_g,
        axe,
        dagger,
        magic_staff,
        helmet

    ) = play_game.set_board()

    knights = [knight_r, knight_y, knight_b, knight_g]
    items = [axe, dagger, magic_staff,  helmet]

    play_game.arena.render_arena()
    run()
    game_state = save_state(knights, items)
    write_to_file(game_state)
