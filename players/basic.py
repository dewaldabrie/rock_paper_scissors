from random import randint

from players.base import RPSPlayerBase


class BasicRandBot(RPSPlayerBase):
    """
    This bot produces a random (uniform) move
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.move_map = {
            1: 'r',
            2: 'p',
            3: 's',
        }

    def __repr__(self):
        return "Basic Random Bot"

    def move(self):
        return self.move_map[randint(1, 3)]


class BeatPrevMoveBot(RPSPlayerBase):
    """
    This bot always moves such that it will win if the opponent repeats it's previous move.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # previous opponent move is key, current move is value
        self.move_map = {
            'r': 'p',
            'p': 's',
            's': 'r',
        }

    def __repr__(self):
        return "Beat Your Previous Move Bot"

    def move(self):
        try:
            prev_opponent_move, prev_self_move, _, _ = self.history[-1]
            return self.move_map[prev_opponent_move]
        # On the first move, do something random
        except IndexError:
            return BasicRandBot().move()
