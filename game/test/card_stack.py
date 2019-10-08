import unittest
from ..card_stack import Card_Stack
from ..card import Card


class Test_Card(Card):
    def __init__(self, name):
        Card.__init__(self, name)

    def get_text(self):
        return "test"


class Test(unittest.TestCase):
    def setUp(self):
        self.dummy_card1 = Test_Card(name="test card 1")
        self.dummy_card2 = Test_Card(name="test card 2")
        self.dummy_card3 = Test_Card(name="test card 3")

    def test_general(self):
        s = Card_Stack(name="test card stack")
        self.assertTrue(len(s) == 0)
        self.assertFalse(s.can_pop_top())
        with self.assertRaises(IndexError):
            s.pop_top()
        s.push_top(self.dummy_card1)
        self.assertTrue(s.can_pop_top())
        s.push_top(self.dummy_card2)
        self.assertTrue(s.can_pop_top())
        with self.assertRaises(ValueError):
            s.push_top(self.dummy_card1)
        with self.assertRaises(ValueError):
            s.push_bottom(self.dummy_card1)
        s.push_bottom(self.dummy_card3)
        s.remove(self.dummy_card2)
        s.push_bottom(self.dummy_card2)
