import unittest
from core.owning import neutral_owner
from ..card import Card


class Test(unittest.TestCase):
    def setUp(self):
        self._context = None

    def test_general(self):
        with self.assertRaises(TypeError):
            Card()

        class Derived_Card(Card):
            def __init__(self, name, face_up=False):
                Card.__init__(self, name, face_up)

            def text(self, context):
                return "test card text"

        c = Derived_Card("test card name")
        self.assertEquals(c.owner(), neutral_owner)
        self.assertEquals(c.cost(self._context), [])
        self.assertEquals(c.mill_points(self._context), 0)
        self.assertEquals(c.knight_points(self._context), 0)
        self.assertEquals(c.win_points(self._context), 0)
