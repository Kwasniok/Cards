import unittest
from ..owning import Owner
from ..card import Card
from ..card_slot import Card_Slot


class Test_Card1(Card):
    def __init__(self, name, face_up=False):
        Card.__init__(self, name, face_up=face_up)

    def text(self):
        return "test card type 1"


class Test_Card2(Card):
    def __init__(self, name, face_up=False):
        Card.__init__(self, name, face_up=face_up)

    def text(self):
        return "test card type 2"


class Test(unittest.TestCase):
    def setUp(self):
        self.dummy_owner = Owner("dummy")

    def test_general(self):
        c1a = Test_Card1(name="test 1 A")
        c1b = Test_Card1(name="test 1 B")
        c1c = Test_Card1(name="test 1 C")
        c2a = Test_Card2(name="test 2 A")
        pct = [Test_Card1]
        cs = Card_Slot(
            name="test card slot 1",
            owner=self.dummy_owner,
            possible_card_types=pct,
            limit=2,
        )
        self.assertTrue(cs.accepts_card(c1a))
        cs.add(c1a)
        cs.remove(c1a)
        self.assertTrue(cs.accepts_card(c1a))
        cs.add(c1a)
        # wrong type
        self.assertFalse(cs.accepts_card(c2a))
        with self.assertRaises(ValueError):
            cs.add(c2a)
        # allreay present
        self.assertFalse(cs.accepts_card(c1a))
        with self.assertRaises(ValueError):
            cs.add(c1a)
        self.assertTrue(cs.accepts_card(c1b))
        cs.add(c1b)
        # limit reached
        self.assertFalse(cs.accepts_card(c1c))
        with self.assertRaises(ValueError):
            cs.add(c1c)
        # not present
        with self.assertRaises(ValueError):
            cs.remove(c1c)
        # accepts card_type
        self.assertTrue(cs.accepts_card_of_type(Test_Card1))
        self.assertFalse(cs.accepts_card_of_type(Test_Card2))
        # __contains__
        self.assertTrue(c1a in cs)
        self.assertTrue(c1b in cs)
        self.assertFalse(c1c in cs)
        self.assertFalse(c2a in cs)
        # full
        self.assertTrue(cs.is_full())
        # empty
        cs.remove(c1a)
        cs.remove(c1b)
        self.assertTrue(cs.is_empty())
