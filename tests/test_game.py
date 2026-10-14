import unittest
from unittest.mock import patch

from game import start_game,check_guess

class TestGuessingGame(unittest.TestCase):

    def test_correct_guess(self):
        self.assertEqual(check_guess(50,50),"correct")

    def test_guess_too_low(self):
        self.assertEqual(check_guess(20,50),"low")

    def test_guess_too_high(self):
        self.assertEqual(check_guess(80,50),"high")

    def test_player_wins(self):
        with patch("builtins.input", return_value="50"):
            with patch("builtins.print"):
                result = start_game(50)

        self.assertTrue(result)

    def test_invalid_input_does_not_consume_attempt(self):
        with patch(
            "builtins.input",
            side_effect=["hello", "101", "50"]
        ):
            with patch("builtins.print"):
                result = start_game(50)

        self.assertTrue(result)

    def test_player_loses_after_seven_wrong_guesses(self):
        with patch("builtins.input", return_value="1"):
            with patch("builtins.print"):
                result = start_game(100)

        self.assertFalse(result)
        
if __name__=="__main__":
    unittest.main()