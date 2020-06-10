# Rock Paper Scissors Game

Welcome to the `Rock, Paper, Scissors!` game. 


## Running

Run the game by running from the terminal:

`./run.sh`


## Playing

Try to beat the bot by clicking on either of the three buttons in the bottom left.


## Changing Interfaces

This game can be played via the GUI or command line.
To switch to a command line interfaces, update the `human_interface` setting in `settings.py`.


## Adding New Interfaces

New interfaces can be added in the `human_interfaces` package.
All interfaces must implement the interface of `HumanInterfaceBase` in the `human_interfaces.base` module.


## Changing Bots

There are a variety of bots implemented to play against.
To play against a different bot, update the `machine_opponent` setting in `settings.py`.


## Adding New Bots

New bots can be added in the `players` package.
All new bots must implement the interface defined by `RPSPlayerBase` in the `players.base` module.


## Running Tests

From the root project directory, run `pytest`.


