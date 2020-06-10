from abc import ABC, abstractmethod


class RPSPlayerBase(ABC):
    
    def __init__(self, interface, history):
        self.interface = interface
        self.history = history
    
    @abstractmethod
    def move(self) -> str:
        """Produce a move, encoded as 'r', 'p' or 's'."""
        raise NotImplementedError

    @abstractmethod
    def __repr__(self) -> str:
        """Human readable name of this player."""
        raise NotImplementedError


