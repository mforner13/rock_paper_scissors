from rock_paper_scissors import *

import pytest

@pytest.mark.parametrize("player_one_move, player_two_move, winner", [
    ("rock", "scissors", 1),
    ("rock", "paper", 2),
    ("rock", "rock", 0),
])
def test_comparator(player_one_move, player_two_move, winner):
    assert comparator(player_one_move, player_two_move) == winner


class TestInputOutcome:  #Ask Jonathan why it needed the same arguments as parametrize when not in a class
    def test_outcome_correct_format(self):
        assert outcome_correct_format("rock", "paaaper") == 1





