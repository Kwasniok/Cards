import unittest
from core.owning import Owner
from core.slot import Slot_Full_Error
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
        class Test_Owner(Owner):
            pass

        self.dummy_owner = Test_Owner()

    def test_general(self):
        c1a = Test_Card1(name="test 1 A")
        c1b = Test_Card1(name="test 1 B")
        c1c = Test_Card1(name="test 1 C")
        c2a = Test_Card2(name="test 2 A")
        pct = [Test_Card1]
        cs = Card_Slot(
            name="test card slot 1",
            owner=self.dummy_owner,
            accepted_base_types=pct,
            limit=2,
        )
        # accepts card_type
        self.assertTrue(cs.accepts_type(Test_Card1))
        self.assertFalse(cs.accepts_type(Test_Card2))
        # empty
        self.assertTrue(cs.is_empty())
        # add/remove
        self.assertTrue(cs.would_accept(c1a))
        cs.add(c1a)
        cs.remove(c1a)
        self.assertTrue(cs.would_accept(c1a))
        cs.add(c1a)
        # wrong type
        self.assertFalse(cs.would_accept(c2a))
        with self.assertRaises(TypeError):
            cs.add(c2a)
        # allreay present
        self.assertFalse(cs.would_accept(c1a))
        with self.assertRaises(ValueError):
            cs.add(c1a)
        self.assertTrue(cs.would_accept(c1b))
        cs.add(c1b)
        # limit reached
        self.assertFalse(cs.would_accept(c1c))
        with self.assertRaises(Slot_Full_Error):
            cs.add(c1c)
        # remove (not present)
        cs.remove(c1c)
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
