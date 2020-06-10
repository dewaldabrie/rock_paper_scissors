
class RPS:

    def __init__(self, interface, player1_class, player2_class):
        self.interface = interface
        self.state = {
            'player1_name': '',
            'player1_total_score': 0,
            'player1_latest_move': None,
            'player1_latest_point': None,
            'player1_previous_move': None,
            'player1_previous_point': None,
            'player2_name': '',
            'player2_total_score': 0,
            'player2_latest_move': None,
            'player2_latest_point': None,
            'player2_previous_move': None,
            'player2_previous_point': None,
            'num_rounds': 0,
        }
        self.history = []
        self.player1 = player1_class(self.interface, self.history)
        self.player2 = player2_class(self.interface, self.history)
        self.state['player1_name'] = str(self.player1)
        self.state['player2_name'] = str(self.player2)

    def outcome(self, player1_move, player2_move):
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

    def update_state(self, player1_move, player2_move):
        """Update the game state with based on the moves from the players."""
        player1_point, player2_point = self.outcome(player1_move, player2_move)

        self.state['num_rounds'] += 1

        self.state['player1_previous_move'] = self.state['player1_latest_move']
        self.state['player1_previous_point'] = self.state['player1_latest_point']
        self.state['player1_latest_move'] = player1_move
        self.state['player1_latest_point'] = player1_point
        self.state['player1_total_score'] += player1_point

        self.state['player2_previous_move'] = self.state['player2_latest_move']
        self.state['player2_previous_point'] = self.state['player2_latest_point']
        self.state['player2_latest_move'] = player2_move
        self.state['player2_latest_point'] = player2_point
        self.state['player2_total_score'] += player2_point

        return

    def advance(self):

        player1_move = self.player1.move()
        player2_move = self.player2.move()

        self.update_state(player1_move, player2_move)
        self.history.append((
            player1_move,
            player2_move,
            self.state['player1_latest_point'],
            self.state['player2_latest_point'])
        )

        return self.state

