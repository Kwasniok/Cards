import unittest
from ..game_state import Game_State
from ..player import Player
from ..neutral_zone import Neutral_Zone


class Test(unittest.TestCase):
    def test_general(self):
        game_state = Game_State(name="test game state")
        self.assertEqual(str(game_state), "test game state")
        self.assertEqual(game_state.get_name(), "test game state")
        # getters
        player1 = game_state.get_player1()
        self.assertTrue(isinstance(player1, Player))
        player2 = game_state.get_player2()
        self.assertTrue(isinstance(player2, Player))
        neutral_zone = game_state.get_neutral_zone()
        self.assertTrue(isinstance(neutral_zone, Neutral_Zone))
        # on_prepare_game
        game_state.on_prepare_game(context=None)
        # getters
        player1 = game_state.get_player1()
        self.assertTrue(isinstance(player1, Player))
        player2 = game_state.get_player2()
        self.assertTrue(isinstance(player2, Player))
        neutral_zone = game_state.get_neutral_zone()
        self.assertTrue(isinstance(neutral_zone, Neutral_Zone))
