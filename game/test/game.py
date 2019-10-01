import unittest
from ..game import Game


class Test(unittest.TestCase):
    def test_general(self):
        g = Game(name="test game")
