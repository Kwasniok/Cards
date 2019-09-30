import unittest
from core.owning import Owner
from core.card import Card
from core.hand import Hand
from core.dice import Dice
from core.card_stack import Card_Stack
from core.card_slot import Card_Slot
from ..resource_types import LOGS, BRICKS, GRAIN, IRON, WOOL, GOLD
from ..structure_cards import Street_Card, Settlement_Card, Town_Card
from ..resource_cards import Resource_Card


class Test(unittest.TestCase):
    def test_general(self):
        cards = [
            Street_Card(),
            Settlement_Card(),
            Town_Card(),
            Resource_Card(LOGS, 1, 0),
            Resource_Card(BRICKS, 1, 0),
            Resource_Card(GRAIN, 3, 0),
            Resource_Card(IRON, 4, 0),
            Resource_Card(WOOL, 5, 0),
            Resource_Card(GOLD, 3, 0),
        ]
        self.assertTrue(len(cards) > 2)
        for c in cards:
            self.assertTrue(isinstance(str(c), str))
            self.assertTrue(isinstance(c.text(), str))
            # card name in card text (might not be a good idea)
            self.assertTrue(str(c) in c.text())
