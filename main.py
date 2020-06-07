from time import sleep

from human_interfaces.console import ConsoleInterface
from players.basic import BasicRandBot
from players.human import Human
from state import WAIT_FOR_PLAYER_MOVES, FETCHING_OUTCOME



def outcome(player1_move, player2_move):
    points = {
        ('r', 'r'): (0, 0),
        ('r', 'p'): (0, 1),
        ('r', 's'): (1, 0),
        ('p', 'r'): (1, 0),
        ('p', 'p'): (0, 0),
        ('p', 's'): (0, 1),
        ('s', 'r'): (0, 1),
        ('s', 'p'): (1, 0),
        ('s', 's'): (0, 0),
    }
    return points[(player1_move, player2_move)]


def update_state(state, player1_move, player2_move):
    """Update the game state with based on the moves from the players."""
    player1_point, player2_point = outcome(player1_move, player2_move)

    state['num_rounds'] += 1

    state['player1_previous_move '] = state['player1_latest_move']
    state['player1_latest_move'] = player1_move
    state['player1_latest_point'] = player1_point
    state['player1_total_score'] += player1_point

    state['player2_previous_move'] = state['player2_latest_move']
    state['player2_latest_move'] = player2_move
    state['player2_latest_point'] = player2_point
    state['player2_total_score'] += player2_point

    state['state_name'] = WAIT_FOR_PLAYER_MOVES

    return


def show_animation(interface, state):
    state['state_name'] = FETCHING_OUTCOME
    state.update()


if __name__ == '__main__':

    history = []
    human_interface = ConsoleInterface(history)
    player1 = Human(human_interface, history)
    player2 = BasicRandBot(history)

    # Game state encoding
    game_state = {
        'player1_name': str(player1),
        'player1_total_score': 0,
        'player1_latest_move': 0,
        'player1_latest_point': 0,
        'player1_previous_move': None,
        'player2_name': str(player2),
        'player2_total_score': 0,
        'player2_latest_move': 0,
        'player2_latest_point': 0,
        'player2_previous_move': None,
        'state_name': WAIT_FOR_PLAYER_MOVES,
        'num_rounds': 0,
    }

    while True:

        player1_move = player1.move()
        show_animation(human_interface, game_state)
        player2_move = player2.move()

        update_state(game_state, player1_move, player2_move)
        history.append((
            player1_move,
            player2_move,
            game_state['player1_latest_point'],
            game_state['player2_latest_point'])
        )

        human_interface.update(game_state)
