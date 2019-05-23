
def input():
    player_one = input("Player 1, what's your first move? ").lower()
    player_two = input("Player 2, what's your first move? ").lower()

def outcome_correct_format(player_one, player_two):
    if player_one or player_two != "rock" or "scissors" or "paper":
        print("Please enter rock, paper or scissors")
        return 1
    else:
        pass

def comparator(player_one:str, player_two:str):
    return None


def play_1_rock(response):
    if response == "scissors":
        print("Player 1 wins this round")
    elif response == "paper":
        print("Player 2 wins this round")
    elif response == "rock":
        print("It's a draw")
    else:
        pass

def play_1_scissors(response):
    if response == "paper":
        print("Player 1 wins this round")
    elif response == "rock":
        print("Player 2 wins this round")
    elif response == "scissors":
        print("It's a draw")
    else:
        pass

def play_1_paper(response):
    if response == "rock":
        print("Player 1 wins this round")
    elif response == "scissors":
        print("Player 1 wins this round")
    elif response == "paper":
        print("It's a draw")
    else:
        pass

"""if player_1_response == "rock":
    play_1_rock(player_2_response)
elif player_1_response == "scissors":
    play_1_scissors(player_2_response)
elif player_1_response == "paper":
    play_1_paper(player_2_response)
else:
    print("Sorry, please enter either rock, paper or scissors.")"""




#new_game = input("Do you want to play again? ").lower()
