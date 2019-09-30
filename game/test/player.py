import unittest
from core.color import BLACK, WHITE
from ..player import Player


class Test(unittest.TestCase):
    def test_general(self):
        p = Player(name="player", color=BLACK)
