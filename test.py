"""Testing file

Test various functionalities of Rock - Paper - Scissors Game
"""
import unittest
from game import Game


class Test(unittest.TestCase):
    """ Main unit testing class"""

    def setUp(self):
        self.game = Game()

    def test_verify_player_input(self):
        """ Test the functionality of the verify_player_input method"""
        # Assume player has input 'r' for Rock
        self.game.player_input = 'r'
        self.assertEqual(True, self.game.verify_player_input())

        # Assume player has input 'paper' for Paper
        self.game.player_input = 'paper'
        self.assertEqual(True, self.game.verify_player_input())

        # Assume player has input 'SciSSors' for Scissors
        self.game.player_input = 'SciSSors'
        self.assertEqual(True, self.game.verify_player_input())

        # Assume player has input wrong word. It could be any string
        self.game.player_input = 'any'
        self.assertEqual(False, self.game.verify_player_input())

    def test_verify_computer_choice(self):
        """ Test the functionality of the make_computer_choice method"""
        # Computer make random choice from 0-2.
        self.game.make_computer_choice()
        self.assertEqual(True, self.game.computer_choice in [1, 2, 3])

    def test_verify_round_winner(self):
        """ Test the functionality of evaluate_result method by verifying all
            possible combination of the player and computer's choices """
        # Player's choice is Rock(1)
        self.game.player_choice = 1
        self.game.computer_choice = 1
        self.assertEqual("draw", self.game.evaluate_result_and_update_score())
        self.game.computer_choice = 2
        self.assertEqual("computer",
                         self.game.evaluate_result_and_update_score())
        self.game.computer_choice = 3
        self.assertEqual("player", self.game.evaluate_result_and_update_score())

        # Player's choice is Paper(2)
        self.game.player_choice = 2
        self.game.computer_choice = 1
        self.assertEqual("player", self.game.evaluate_result_and_update_score())
        self.game.computer_choice = 2
        self.assertEqual("draw", self.game.evaluate_result_and_update_score())
        self.game.computer_choice = 3
        self.assertEqual("computer",
                         self.game.evaluate_result_and_update_score())

        # Player's choice is Scissors(3)
        self.game.player_choice = 3
        self.game.computer_choice = 1
        self.assertEqual("computer",
                         self.game.evaluate_result_and_update_score())
        self.game.computer_choice = 2
        self.assertEqual("player", self.game.evaluate_result_and_update_score())
        self.game.computer_choice = 3
        self.assertEqual("draw", self.game.evaluate_result_and_update_score())

    def test_verify_score_management(self):
        """ Test the score management functionality """
        # Initial score for player and computer are 0
        self.assertEqual(0, self.game.player_score)
        self.assertEqual(0, self.game.computer_score)

        # Check computer's score updates after computer wins
        self.game.player_choice = 1
        self.game.computer_choice = 2
        self.assertEqual("computer",
                         self.game.evaluate_result_and_update_score())
        self.assertEqual(1, self.game.computer_score)
        self.assertEqual(0, self.game.player_score)

        # Check player's score updates after player wins
        self.game.player_choice = 3
        self.game.computer_choice = 2
        self.assertEqual("player", self.game.evaluate_result_and_update_score())
        self.assertEqual(1, self.game.computer_score)
        self.assertEqual(1, self.game.player_score)

        # Check the draw case
        self.game.player_choice = 1
        self.game.computer_choice = 1
        self.assertEqual("draw", self.game.evaluate_result_and_update_score())
        self.assertEqual(1, self.game.computer_score)
        self.assertEqual(1, self.game.player_score)

        # Try to reach score of Player : Computer = 2 : 3 and test
        self.game.player_choice = 3
        self.game.computer_choice = 1
        self.assertEqual("computer",
                         self.game.evaluate_result_and_update_score())
        self.game.computer_choice = 2
        self.assertEqual("player", self.game.evaluate_result_and_update_score())

        self.game.player_choice = 2
        self.game.computer_choice = 3
        self.assertEqual("computer",
                         self.game.evaluate_result_and_update_score())

        self.assertEqual(3, self.game.computer_score)
        self.assertEqual(2, self.game.player_score)

    def test_verify_game_winner(self):
        """ Test the game over functionality. Player wins the game when player
            reaches to 5 points. """
        self.assertEqual(0, self.game.computer_score)
        self.assertEqual(0, self.game.player_score)
        self.assertEqual(False, self.game.is_game_over())

        self.game.player_choice = 3
        self.game.computer_choice = 2
        self.assertEqual("player", self.game.evaluate_result_and_update_score())
        self.assertEqual(1, self.game.player_score)
        self.assertEqual(False, self.game.is_game_over())

        self.assertEqual("player", self.game.evaluate_result_and_update_score())
        self.assertEqual("player", self.game.evaluate_result_and_update_score())
        self.assertEqual("player", self.game.evaluate_result_and_update_score())
        self.assertEqual(False, self.game.is_game_over())

        self.assertEqual("player", self.game.evaluate_result_and_update_score())
        self.assertEqual(0, self.game.computer_score)
        self.assertEqual(5, self.game.player_score)
        self.assertEqual(True, self.game.is_game_over())
