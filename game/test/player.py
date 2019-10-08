import unittest
from gui.color import BLACK, WHITE
from ..player import Player


class Test(unittest.TestCase):
    def test_general(self):
        p = Player(name="player", color=BLACK)
        self.assertEqual(p.get_hand().get_owner(), p)
        self.assertEqual(p.get_realm().get_owner(), p)
