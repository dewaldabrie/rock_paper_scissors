import pytest
from players.basic import BeatPrevMoveBot, BasicRandBot

beat = {
    'r': 'p',
    'p': 's',
    's': 'r',
}

@pytest.mark.parametrize(
    "history,expected_move",
    [
        # ((player1_move, player2_move, player1_point, player2_point), expected_move)
        (('r', 'p', 0, 1), 'p'),
        (('p', 'r', 1, 0), 's'),
        (('s', 'r', 1, 0), 'r'),
    ]
)
def test_beat_prev_move_bot(history, expected_move):
    history = [
        history
    ]
    bot = BeatPrevMoveBot(None, history)
    move = bot.move()

    assert move == expected_move


def test_rand_bot():
    """For the same input, we should get a pretty even distribution of outputs."""
    history = [
        # (player1_move, player2_move, player1_point, player2_point)
        ('r', 'p', 0, 1),
    ]

    bot = BasicRandBot(None, history)

    r_moves = p_moves = s_moves = 0
    for i in range(100):
        move = bot.move()
        if move == 'r':
            r_moves += 1
        elif move == 's':
            s_moves += 1
        elif move == 'p':
            p_moves += 1

    assert r_moves > 10
    assert p_moves > 10
    assert s_moves > 10
    assert len(history) == 1

