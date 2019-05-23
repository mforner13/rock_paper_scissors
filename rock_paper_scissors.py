
def input():
    player_one = input("Player 1, what's your first move? ").lower()
    player_two = input("Player 2, what's your first move? ").lower()

def outcome_correct_format(player_one, player_two):
    if player_one or player_two != "rock" or "scissors" or "paper":
        print("Please enter rock, paper or scissors")
        return 1
    else:
        pass


def comparator(player_one, player_two):

    if player_one == player_two:
        print("It's a draw!")
        return 0
    else:
        pass

    if player_one == "rock":
        if player_two == "scissors":
            print("Player 1 wins this round")
            return 1
        elif player_two == "paper":
            print("Player 2 wins this round")
            return 2
        else:
            pass

    if player_one == "scissors":
        if player_two == "paper":
            print("Player 1 wins this round")
            return 1
        elif player_two == "rock":
            print("Player 2 wins this round")
            return 2
        else:
            pass

    if player_one == "paper":
        if player_two == "rock":
            print("Player 1 wins this round")
            return 1
        elif player_two == "scissors":
            print("Player 2 wins this round")
            return 2
        else:
            pass