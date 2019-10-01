import unittest
from ..resource_types import LOGS, BRICKS, GRAIN, IRON, WOOL, GOLD
from ..cards import (
    Road_Card,
    Settlement_Card,
    Town_Card,
    Resource_Card,
    Action_Card,
    Small_Building_Card,
    Large_Building_Card,
    Event_Card,
)


class Test(unittest.TestCase):
    def setUp(self):
        self._context = None
    def test_structure(self):
        cards = [Road_Card(), Settlement_Card(), Town_Card()]
        self.assertTrue(len(cards) > 2)
        for c in cards:
            self.assertTrue(isinstance(str(c), str))
            self.assertTrue(isinstance(c.text(self._context), str))
            # card name in card text (might not be a good idea)
            self.assertTrue(str(c) in c.text(self._context))

    def test_resource(self):
        cards = [
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
            self.assertTrue(isinstance(c.text(self._context), str))
            # card name in card text (might not be a good idea)
            self.assertTrue(str(c) in c.text(self._context))
