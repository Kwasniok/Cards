import unittest
from ..owning import Owner
from ..card import Card
from ..hand import Hand


class Test_Card(Card):
    def __init__(self, name, face_up=False):
        Card.__init__(self, name, face_up=face_up)

    def text(self):
        return "test"


class Test(unittest.TestCase):
    def setUp(self):
        self.dummy_owner = Owner("dummy")

    def test_general(self):
        limit = 2
        h = Hand(name="test hand", owner=self.dummy_owner, limit=limit)
        c1 = Test_Card("test card 1")
        c2 = Test_Card("test card 2")
        c3 = Test_Card("test card 3")
        self.assertFalse(h.above_limit())
        self.assertEqual(h.size(), 0)
        self.assertFalse(c1 in h)
        self.assertFalse(c2 in h)
        self.assertFalse(c3 in h)
        h.add_card(c1)
        self.assertTrue(c1 in h)
        self.assertFalse(h.above_limit())
        self.assertEqual(h.size(), 1)
        h.add_card(c2)
        self.assertTrue(c2 in h)
        self.assertFalse(h.above_limit())
        self.assertEqual(h.size(), 2)
        h.add_card(c3)
        self.assertTrue(c3 in h)
        self.assertTrue(h.above_limit())
        self.assertEqual(h.size(), 3)
        h.remove_card(c3)
        self.assertFalse(c3 in h)
        self.assertFalse(h.above_limit())
        self.assertEqual(h.size(), 2)
        with self.assertRaises(ValueError):
            h.remove_card(c3)
