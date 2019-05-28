
def input_moves(player:int):
    player_move = input(f"Player {player}, what's your first move? ").lower()
    return player_move


def input_validator(word):
    accepted_inputs = {
        "rock": True,
        "paper": True,
        "scissors": True,
        "yes": True,
    }
    if word in accepted_inputs:
        return accepted_inputs.get(word)
    else:
        return False


def comparator(player_one, player_two):

    if player_one == player_two:
        return 0
    else:
        pass

    if player_one == "rock":
        if player_two == "scissors":
            return 1
        elif player_two == "paper":
            return 2
        else:
            pass

    if player_one == "scissors":
        if player_two == "paper":
            return 1
        elif player_two == "rock":
            return 2
        else:
            pass

    if player_one == "paper":
        if player_two == "rock":
            return 1
        elif player_two == "scissors":
            return 2
        else:
            pass


def player_input(player_no):
    player_input = input_moves(player_no)
    while not input_validator(player_input):
        print("Try again!")
        player_input = input_moves(player_no)
    return player_input


def play_again():
    player_wanna_play = input("Do you want to play again?").lower()
    return input_validator(player_wanna_play)


def main():
    # Run input_moves to get player 1 move, if wrong ask to input again till input is rock, paper or scissors. Repeat for player 2.
    player_wanna_play = True
    while player_wanna_play:
        player_one = player_input(1)
        player_two = player_input(2)
        comparator(player_one, player_two)
        if comparator(player_one, player_two) == 1:
            print("Player 1 wins!")
        elif comparator(player_one, player_two) == 2:
            print("Player 2 wins!")
        elif comparator(player_one, player_two) == 0:
            print("It's a draw!")
        else:
            print("error")
        player_wanna_play = play_again()

if __name__ == '__main__':
    main()


