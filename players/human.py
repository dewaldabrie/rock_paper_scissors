from players.base import RPSPlayerBase


class Human(RPSPlayerBase):

    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return "Human Player"

    def move(self):
        move = self.interface.get_move()
        if self.valid_input(move):
            return move
        else:
            return self.move()

    def valid_input(self, move):
        if move not in ('r', 'p', 's'):
            err_msg = "Unrecognised, move %s, expecting 'r', 'p' or 'q'." % move
            self.interface.show_error(err_msg)
            return False
        return True
