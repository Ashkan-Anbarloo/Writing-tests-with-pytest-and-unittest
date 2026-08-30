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
    #         mock_print.assert_any_call('Invalid move...')
    #         mock_play_game.assert_called()
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['invalid', 'exit'])
    def test_invalid_move(self, mock_input, mock_print):
        rps = RPS()
        with self.assertRaises(SystemExit):
            rps.play_game()
        mock_print.assert_any_call('Invalid moves ...')

