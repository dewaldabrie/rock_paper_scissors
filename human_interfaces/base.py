from abc import ABC, abstractmethod


class HumanInterfaceBase(ABC):

    def __init__(self, move_history):
        self.move_history = move_history

    @abstractmethod
    def get_move(self) -> str:
        """Get the next move and encode as 'r', 'p' or 's'."""
        raise NotImplementedError

    @abstractmethod
    def show_error(self, err_msg):
        """Display an error message to the user related to the user input."""
        raise NotImplementedError

    @abstractmethod
    def update(self, state):
        """
        Update the user interface based on the latest game state.
        This should update the player scores, number of rounds, etc.
        """
        raise NotImplementedError

