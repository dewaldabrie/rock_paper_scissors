#!/usr/bin/env bash

# activate virtualenv
if [ ! -d .venv ]
then
    python3 -m virtualenv -p python3.6 .venv
fi
source .venv/bin/activate

# update requirements
pip install -r requirements.txt -q

# run game
python main.py
