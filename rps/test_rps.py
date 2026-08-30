import unittest
from unittest.mock import patch
import builtins
import random
import sys
from .rps import RPS

class TestRPS(unittest.TestCase):
    def test_initialization(self):
        rps = RPS()
        self.assertEqual(rps.moves , {'rock':'🌑' , 'paper': '📄' , 'scissors':'✂'})
        self.assertEqual(rps.valid_moves , ['rock' , 'paper' , 'scissors'])

    # @patch('builtins.print')
    # @patch('builtins.input' , return_value='invalid')
    # def test_invalid_move(self , mock_input , mock_print):
    #     rps = RPS()
    #     with patch.object(rps , 'play_game' , return_value=None) as mock_play_game:
    #         rps.play_game()
    #         mock_print.assert_any_call('Invalid moves ...')
    #         mock_play_game.assert_called()
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['invalid', 'exit'])
    def test_invalid_move(self, mock_input, mock_print):
        rps = RPS()
        with self.assertRaises(SystemExit):
            rps.play_game()
        mock_print.assert_any_call('Invalid moves ...')

    @patch('builtins.input', return_value='exit')
    @patch('builtins.print')
    def test_exit_game(self , mock_print, mock_input):
        rps = RPS()
        with self.assertRaises(SystemExit):
            rps.play_game()
        mock_print.assert_called_with('Thanks for playing!')

    @patch('builtins.print')
    def test_check_move_tie(self , mock_print):
        rps = RPS()
        rps.check_move('rock' , 'rock')
        mock_print.assert_any_call('It is a tie')

    @patch('builtins.print')
    def test_check_move_user_win(self , mock_print):
        rps = RPS()

        rps.check_move(user_move='rock' , ai_move='scissors')
        mock_print.assert_any_call('You win')

        rps.check_move(user_move='paper', ai_move='rock')
        mock_print.assert_any_call('You win')

        rps.check_move(user_move='scissors', ai_move='paper')
        mock_print.assert_any_call('You win')

    @patch('builtins.print')
    def test_check_move_ai_win(self, mock_print):
        rps = RPS()
        rps.check_move(user_move='rock' , ai_move='paper')
        mock_print.assert_any_call('AI win')

    @patch('builtins.print')
    def test_display_move(self , mock_print):
        rps = RPS()
        rps.display_move('rock' , 'scissors')
        mock_print.assert_any_call('You : 🌑')
        mock_print.assert_any_call('AI : ✂')

    @patch('builtins.input', return_value='rock')
    @patch('random.choice', return_value='scissors')
    @patch('builtins.print')
    def test_play_game_valid(self , mock_print, mock_input, mock_random):
        rps = RPS()
        rps.play_game()

        mock_print.assert_any_call('You : 🌑')
        mock_print.assert_any_call('AI : ✂')
        mock_print.assert_any_call('You win')





