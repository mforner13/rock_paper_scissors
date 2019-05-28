from rock_paper_scissors import *

import pytest

@pytest.mark.parametrize("player_input, expected_output", [
    ("rock", True),
    ("paper", True),
    ("scissors", True),
    (12, False),
    ("sdlfsdg", False),
])
def test_input_validator(player_input, expected_output):
    assert input_validator(player_input) is expected_output


@pytest.mark.parametrize("player_one_move, player_two_move, winner", [
    ("rock", "scissors", 1),
    ("rock", "paper", 2),
    ("rock", "rock", 0),
])
def test_comparator(player_one_move, player_two_move, winner):
    assert comparator(player_one_move, player_two_move) == winner


class TestMain:
    def test_main(self, monkeypatch):
        monkeypatch.setattr()
