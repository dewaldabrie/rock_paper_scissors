"""Provide a player interface via the console."""
from time import sleep

from human_interfaces.base import HumanInterfaceBase


class ConsoleInterface(HumanInterfaceBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.move_name = {
            'r': 'rock',
            'p': 'paper',
            's': 'scissors'
        }
        self.state = {}

    def get_move(self):
        move = input("Rock (r), paper (p), scissors (s)?")
        if move == 'q':
            exit(0)
        return move

    def show_error(self, err_msg):
        print(err_msg)

    def _countdown(self):
        for i in list(range(1,4))[::-1]:
            print(i)
            sleep(1)

    def _display_outcome(self, human_move, bot_move, human_points, bot_points):
        if human_points == 1:
            print('%s beats %s, human wins!' % (self.move_name[human_move], self.move_name[bot_move]))
        elif bot_points == 1:
            print('%s beats %s, bot wins!' % (self.move_name[bot_move], self.move_name[human_move]))
        else:
            print('It\'s a draw!')

    def _display_opponent_move(self, opponent_move):
        print("Bot chose %s" % self.move_name[opponent_move])

    @staticmethod
    def _display_score(player1_total_score, player2_total_score):
        print("Score: human: %d, bot: %d" % (player1_total_score, player2_total_score))

    def update(self):
        # first round
        if self.state['num_rounds'] == 0:
            self._display_score(self.state['player1_total_score'], self.state['player2_total_score'])
        else:
            self._display_opponent_move(self.state['player2_latest_move'])
            sleep(1)
            self._display_outcome(
                self.state['player1_latest_move'],
                self.state['player2_latest_move'],
                self.state['player1_latest_point'],
                self.state['player2_latest_point'],
            )
            sleep(1)
            self._display_score(self.state['player1_total_score'], self.state['player2_total_score'])

    def run(self):
        while True:
            self.state = self.engine.advance()
            self.update()

