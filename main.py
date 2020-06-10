from settings import human_interface as human_interface_class
from settings import machine_opponent as machine_opponent_class
from players.human import Human as human_class
from rps import RPS


if __name__ == '__main__':
    hmi = human_interface_class(
        engine=RPS,
        player1_class=human_class,  # TODO: support bot on bot gameplay
        player2_class=machine_opponent_class,
    )
    hmi.run()

