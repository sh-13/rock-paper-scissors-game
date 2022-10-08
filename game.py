"""Rock - Paper - Scissors Game

Choose your choice from Rock/Paper/Scissors to beat the computer.

All the best !!!
"""
import random


def print_start_game_screen():
    """ Game starting banner """
    print(" ----------------------------------------------")
    print("|                                              |")
    print("|          Rock Paper Scissors Game            |")
    print("|                                              |")
    print(" ----------------------------------------------")


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


def print_winning_screen():
    """ player winning banner """
    print(" ----------------------------------------------")
    print("|          \\                      /            |")
    print("|           --- Congratulation ---             |")
    print("|          /                      \\            |")
    print("|               !!! You Won !!!                |")


class Game:
    """ Main game class"""

    def __init__(self):
        self.round_no = 1
        self.computer_score = 0
        self.player_score = 0
        self.computer_choice = None
        self.player_input = None
        self.player_choice = False

    def get_player_input(self):
        """ Get player's input from Rock/Paper/Scissors options. """
        print("|                  Round :", self.round_no,
              "                  |")
        print("|    ---------     ---------     ----------    |")
        print("|   |  ROCK   |   |  PAPER  |   | SCISSORS |   |")
        print("|   | (r / R) |   | (p / P) |   |  (s / S) |   |")
        print("|    ---------     ---------     ----------    |")
        print("|                 QUIT (q / Q)                 |")
        print(" ----------------------------------------------")
        self.player_input = input(" Choose your choice ---> ")

    def verify_player_input(self):
        """ Verify player has input correct choice from Rock/Paper/Scissors. """
        lower_case_player_input = self.player_input.lower()
        if lower_case_player_input in ('r', 'rock'):
            self.player_choice = 1
        elif lower_case_player_input in ('p', 'paper'):
            self.player_choice = 2
        elif lower_case_player_input in ('s', 'scissors'):
            self.player_choice = 3
        elif lower_case_player_input in ('q', 'quit'):
            return "quit"
        else:
            return False
        return True

    def make_computer_choice(self):
        """ Computer choose randomly from Rock(1)/Paper(2)/Scissors(3). """
        self.computer_choice = random.randint(0, 2) + 1

    def evaluate_result_and_update_score(self):
        """ Find the winner based on player and computer's choices and update
            the score of the winner. In case of draw, no one gets point. """
        if self.player_choice == self.computer_choice:
            print("                 Its a Draw !!!                 ")
        elif (self.computer_choice + 1) % 3 == (self.player_choice % 3):
            self.player_score += 1
            print("             You win this round !!!             ")
        else:
            self.computer_score += 1
            print("         Computer wins this round !!!           ")

    def is_game_over(self):
        """ Check if the game is finished. The game is finished when either
            player or computer reaches to 5 points. """
        if self.player_score == 5 or self.computer_score == 5:
            return True
        return False

    def reset_the_game(self):
        """ Reset the game when player wants to restart the game """
        self.player_score = 0
        self.computer_score = 0
        self.round_no = 1

    def restart_game_choice(self):
        """ Option to restart or quit the game after game is over. """
        print("|     RESTART (any key)      QUIT (q / Q)      |")
        print(" ----------------------------------------------")
        restart_choice = input(" Choose your choice ---> ")
        lower_case_restart_choice = restart_choice.lower()
        if lower_case_restart_choice in ('q', 'quit'):
            return "quit"
        self.reset_the_game()
        return "restart"

    def print_score_card(self):
        """ Score card banner """
        print(" ----------------------------------------------")
        print("|     You :", self.player_score, "    Score Card    Computer :",
              self.computer_score, "  |")

    def play_game(self):
        """ Main game code """
        print_start_game_screen()
        while True:
            self.print_score_card()
            self.get_player_input()
            verify_player_input = self.verify_player_input()
            if verify_player_input == "quit":
                break
            if verify_player_input:
                self.make_computer_choice()
                self.evaluate_result_and_update_score()
                self.round_no += 1
            else:
                print_false_input_screen()

            if self.is_game_over():
                if self.player_score == 5:
                    print_winning_screen()
                else:
                    print_losing_screen()

                if self.restart_game_choice() == "quit":
                    break


if __name__ == '__main__':
    game = Game()
    game.play_game()
