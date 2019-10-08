import unittest
from core.owning import Owned
from ..neutral_owner import neutral_owner
from ..card import Card


class Test(unittest.TestCase):
    def setUp(self):
        self._context = None

    def test_is_abstract(self):
        with self.assertRaises(TypeError):
            Card()

    def test_general(self):
        class Derived_Card(Card):
            def __init__(self, name, face_up=False):
                Card.__init__(self, name, face_up)

            def text(self, context):
                return "test card text"

        c = Derived_Card("test card name", face_up=True)
        self.assertTrue(isinstance(c, Owned))
        self.assertEquals(c.get_owner(), neutral_owner)
        # facing
        self.assertTrue(c.is_face_up())
        c.toggle_face()
        self.assertFalse(c.is_face_up())
        c.make_face_up()
        self.assertTrue(c.is_face_up())
        c.make_face_down()
        self.assertFalse(c.is_face_up())
        # default card properties
        self.assertEquals(c.cost(self._context), [])
        self.assertEquals(c.mill_points(self._context), 0)
        self.assertEquals(c.knight_points(self._context), 0)
        self.assertEquals(c.win_points(self._context), 0)
