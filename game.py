"""Rock - Paper - Scissors Game

Choose your choice from Rock/Paper/Scissors to beat the computer.

All the best !!!
"""
import random


def get_player_input(round_no):
    """ Get player's input from Rock/Paper/Scissors/Quit options """
    print("|                  Round :", round_no, "                  |")
    print("|    ---------     ---------     ----------    |")
    print("|   |  ROCK   |   |  PAPER  |   | SCISSORS |   |")
    print("|   | (r / R) |   | (p / P) |   |  (s / S) |   |")
    print("|    ---------     ---------     ----------    |")
    print("|                 QUIT (q / Q)                 |")
    print(" ----------------------------------------------")
    return input(" Choose your choice ---> ")


def verify_player_input(player_input):
    """ Verify player has input correct choice """
    if player_input in ('r', 'R'):
        return 1
    if player_input in ('p', 'P'):
        return 2
    if player_input in ('s', 'S'):
        return 3
    if player_input in ('q', 'Q'):
        return "quit"
    return False


def make_computer_choice():
    """ Computer choose randomly from Rock(1)/Paper(2)/Scissors(3) """
    return random.randint(0, 2)


def evaluate_result(player_choice, computer_choice):
    """ Find the winner based on player and computer's choices """
    if player_choice == computer_choice:
        print("                 Its a Draw !!!                  ")
        return "draw"
    if (computer_choice + 1) % 3 == (player_choice % 3):
        print("             You win this round !!!             ")
        return "player"
    print("         Computer wins this round !!!           ")
    return "computer"


def print_start_game_screen():
    """ Game starting banner """
    print(" ----------------------------------------------")
    print("|                                              |")
    print("|          Rock Paper Scissors Game            |")
    print("|                                              |")
    print(" ----------------------------------------------")


def print_winning_screen():
    """ player winning banner """
    print(" ----------------------------------------------")
    print("|          \\                      /            |")
    print("|           --- Congratulation ---             |")
    print("|          /                      \\            |")
    print("|               !!! You Won !!!                |")


def print_losing_screen():
    """ player losing banner """
    print(" ----------------------------------------------")
    print("|            \\                    /            |")
    print("|             ------- Oops -------             |")
    print("|            /                    \\            |")
    print("|               !!! You Lose !!!               |")


def print_false_input_screen():
    """ Wrong input banner """
    print(" ----------------------------------------------")
    print("|            \\                    /            |")
    print("|             ------- Oops -------             |")
    print("|            /                    \\            |")
    print("|              !!! Wrong Input !!!             |")


def print_score_card(player_score, computer_score):
    """ Score card banner """
    print(" ----------------------------------------------")
    print("|     You :", player_score, "    Score Card    Computer :",
          computer_score, "  |")


def restart_game():
    """ Game Restart options """
    print("|     RESTART (any key)      QUIT (q / Q)      |")
    print(" ----------------------------------------------")
    return input(" Choose your choice ---> ")


def continue_game():
    """ Game continue options """
    print("|     CONTINUE (any key)     QUIT (q / Q)      |")
    print(" ----------------------------------------------")
    return input(" Choose your choice ---> ")


def play_game():
    """ Main game code """
    player_score, computer_score, round_no = 0, 0, 1
    print_start_game_screen()
    while True:
        print_score_card(player_score, computer_score)
        computer_choice = make_computer_choice()
        player_input = get_player_input(round_no)
        player_choice = verify_player_input(player_input)
        if not player_choice:
            # If player do not enter correct choice, print wrong input screen
            # and provide choices to continue the game or quit the game
            print_false_input_screen()
            continue_choice = continue_game()
            if continue_choice in ('q', 'Q'):
                break
        elif player_choice == 'quit':
            break
        else:
            # Evaluate the winner and give point to the winner. In draw case,
            # nobody gets point.
            winner = evaluate_result(player_choice, computer_choice)
            if winner == "player":
                player_score += 1
            elif winner == "computer":
                computer_score += 1
            # Increase the round number after each round.
            round_no += 1
            # Whoever reaches 5 points first wins the game, whether it is the
            # player or the computer.
            if player_score == 5 or computer_score == 5:
                if player_score == 5:
                    print_winning_screen()
                else:
                    print_losing_screen()
                # When the game finishes, reset the scores, round counter and
                # provide choices to restart the game or quit the game.
                player_score, computer_score, round_no = 0, 0, 1
                restart_choice = restart_game()
                if restart_choice in ('q', 'Q'):
                    break


if __name__ == '__main__':
    play_game()
