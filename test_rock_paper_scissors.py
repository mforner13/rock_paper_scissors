from rock_paper_scissors import *

import pytest

def test_rock_beats_scissors():
    rock_input = "rock"
    scissors_input = "scissors"
    play_1_rock(scissors_input)
    assert output == "Player 1 wins this round"


