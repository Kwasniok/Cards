import unittest
from ..card import Card


class Test_Card(Card):
    def __init__(self, name, face_up=False):
        Card.__init__(self, name, face_up=face_up)


class Test(unittest.TestCase):
    def test_abstract(self):
        # Card is an abstract class.
        with self.assertRaises(TypeError):
            c = Card()

    def test_derived(self):
        c = Test_Card("test derived")

    def test_general(self):
        c = Test_Card("test derived", True)
        c.owner()
        self.assertIsInstance(str(c), str)
        self.assertTrue(c.is_face_up())
        c.toggle_face()
        self.assertFalse(c.is_face_up())
        c.make_face_up()
        self.assertTrue(c.is_face_up())
        c.make_face_down()
        self.assertFalse(c.is_face_up())
