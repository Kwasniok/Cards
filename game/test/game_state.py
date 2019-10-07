import unittest
from ..neutral_zone import Neutral_Zone


class Test(unittest.TestCase):
    def test_general(self):
        g = Neutral_Zone(name="test game state")
