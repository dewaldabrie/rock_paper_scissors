from players.basic import BasicRandBot, BeatPrevMoveBot
from rps import RPS


def setup_rps():
    rps = RPS(None, BasicRandBot, BeatPrevMoveBot)
    return rps


def test_prev_move():
    rps = setup_rps()
    rps.advance()
    p1_move = rps.state['player1_latest_move']
    p2_move = rps.state['player2_latest_move']

    assert p1_move in ('r', 'p', 's')
    assert p2_move in ('r', 'p', 's')
    assert rps.state['player1_previous_move'] is None
    assert rps.state['player2_previous_move'] is None

    rps.advance()

    assert rps.state['player1_previous_move'] == p1_move
    assert rps.state['player2_previous_move'] == p2_move


def test_prev_point():
    rps = setup_rps()
    rps.advance()
    p1_point = rps.state['player1_latest_point']
    p2_point = rps.state['player2_latest_point']

    assert p1_point in (0, 1)
    assert p2_point in (0, 1)
    assert rps.state['player1_previous_point'] is None
    assert rps.state['player2_previous_point'] is None

    rps.advance()

    assert rps.state['player1_previous_point'] == p1_point
    assert rps.state['player2_previous_point'] == p2_point


def test_num_rounds():
    rps = setup_rps()

    assert rps.state['num_rounds'] == 0

    rps.advance()

    assert rps.state['num_rounds'] == 1
