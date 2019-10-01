import unittest
from ..game_state import Game_State


class Test(unittest.TestCase):
    def test_general(self):
        g = Game_State(name="test game")
