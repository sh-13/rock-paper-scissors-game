import random


def get_user_input(round_no):
    print("|                                              |")
    print("|                  Round :", round_no, "                  |")
    print("|                                              |")
    print("|    ---------     ---------     ----------    |")
    print("|   |  ROCK   |   |  PAPER  |   | SCISSORS |   |")
    print("|   | (r / R) |   | (p / P) |   |  (s / S) |   |")
    print("|    ---------     ---------     ----------    |")
    print("|                 QUIT (q / Q)                 |")
    print(" ----------------------------------------------")
    return input(" Choose your choice ---> ")


def verify_user_input(user_input):
    if user_input == 'r' or user_input == 'R':
        return 1
    elif user_input == 'p' or user_input == 'P':
        return 2
    elif user_input == 's' or user_input == 'S':
        return 3
    elif user_input == 'q' or user_input == 'Q':
        return "quit"
    else:
        return False


def make_computer_choice():
    return random.randint(0, 2)


def evaluate_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (computer_choice + 1) % 3 == (user_choice % 3):
        return "user"
    else:
        return "computer"


def print_game_banner_screen():
    print(" ----------------------------------------------")
    print("|                                              |")
    print("|          Rock Paper Scissors Game            |")


def print_winning_screen():
    print(" ----------------------------------------------")
    print("|          \\                      /            |")
    print("|           --- Congratulation ---             |")
    print("|          /                      \\            |")
    print("|               !!! You Won !!!                |")


def print_losing_screen():
    print(" ----------------------------------------------")
    print("|            \\                    /            |")
    print("|             ------- Oops -------             |")
    print("|            /                    \\            |")
    print("|               !!! You Lose !!!               |")


def print_false_input_screen():
    print(" ----------------------------------------------")
    print("|            \\                    /            |")
    print("|             ------- Oops -------             |")
    print("|            /                    \\            |")
    print("|              !!! Wrong Input !!!             |")


def print_score_card(user_score, computer_score):
    print(" ----------------------------------------------")
    print("|                                              |")
    print("|     You :", user_score, "    Score Card    Computer :", computer_score, "  |")


def restart_game():
    print("|     RESTART (any key)      QUIT (q / Q)      |")
    print(" ----------------------------------------------")
    return input(" Choose your choice ---> ")


def continue_game():
    print("|     CONTINUE (any key)     QUIT (q / Q)      |")
    print(" ----------------------------------------------")
    return input(" Choose your choice ---> ")


def play_game():
    user_score, computer_score, round_no = 0, 0, 1
    while True:
        if round_no == 1:
            print_game_banner_screen()
        computer_choice = make_computer_choice()
        user_input = get_user_input(round_no)
        user_choice = verify_user_input(user_input)
        if not user_choice:
            print_false_input_screen()
            continue_choice = continue_game()
            if continue_choice == 'q' or continue_choice == 'Q':
                break
            elif round_no != 1:
                print_score_card(user_score, computer_score)
        elif user_choice == 'quit':
            break
        else:
            winner = evaluate_result(user_choice, computer_choice)
            if winner == "user":
                user_score += 1
            else:
                computer_score += 1
            round_no += 1
            if user_score == 5 or computer_score == 5:
                if user_score == 5:
                    print_winning_screen()
                else:
                    print_losing_screen()
                user_score, computer_score, round_no = 0, 0, 1
                restart_choice = restart_game()
                if restart_choice == 'q' or restart_choice == 'Q':
                    break
            else:
                print_score_card(user_score, computer_score)


if __name__ == '__main__':
    play_game()
