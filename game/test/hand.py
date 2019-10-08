import unittest
from core.owning import Owner, Owned
from ..card import Card
from ..hand import Hand


class Test_Card(Card):
    def __init__(self, name, face_up=False):
        Card.__init__(self, name, face_up=face_up)

    def get_text(self):
        return "test"


class Test(unittest.TestCase):
    def setUp(self):
        class Test_Owner(Owner):
            pass

        self.dummy_owner = Test_Owner()

    def test_general(self):
        limit = 2
        h = Hand(name="test hand", owner=self.dummy_owner, limit=limit)
        self.assertTrue(isinstance(h, Owned))
        self.assertTrue(h.size() == 0)
        c1 = Test_Card("test card 1")
        c2 = Test_Card("test card 2")
        c3 = Test_Card("test card 3")
        self.assertFalse(h.is_above_limit())
        self.assertEqual(h.size(), 0)
        self.assertFalse(c1 in h)
        self.assertFalse(c2 in h)
        self.assertFalse(c3 in h)
        h.add(c1)
        self.assertTrue(c1 in h)
        self.assertFalse(h.is_above_limit())
        self.assertEqual(h.size(), 1)
        h.add(c2)
        self.assertTrue(c2 in h)
        self.assertFalse(h.is_above_limit())
        self.assertEqual(h.size(), 2)
        h.add(c3)
        self.assertTrue(c3 in h)
        self.assertTrue(h.is_above_limit())
        self.assertEqual(h.size(), 3)
        h.remove(c3)
        self.assertFalse(c3 in h)
        self.assertFalse(h.is_above_limit())
        self.assertEqual(h.size(), 2)
        with self.assertRaises(ValueError):
            h.remove(c3)
