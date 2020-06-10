from abc import ABC, abstractmethod
from players.human import Human
from players.basic import BasicRandBot


class HumanInterfaceBase(ABC):

    def __init__(self, engine=None, player1_class=Human, player2_class=BasicRandBot):
        self.engine = engine(self, player1_class, player2_class)

    @abstractmethod
    def get_move(self) -> str:
        """Get the next move and encode as 'r', 'p' or 's'."""
        raise NotImplementedError

    @abstractmethod
    def show_error(self, err_msg):
        """Display an error message to the user related to the user input."""
        raise NotImplementedError

    @abstractmethod
    def update(self):
        """
        Update the user interface based on the latest game state.
        This should update the player scores, number of rounds, etc.
        """
        raise NotImplementedError

    @abstractmethod
    def run(self):
        """
        Run the Interface.
        """
        raise NotImplementedError
