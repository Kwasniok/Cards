import unittest
from ..neutral_owner import neutral_owner
from ..piece import Piece


class Test_Piece(Piece):
    def __init__(self, name):
        Piece.__init__(self, name=name)


class Test(unittest.TestCase):
    def setUp(self):
        self.context = None

    def test_abstract(self):
        with self.assertRaises(TypeError):
            Piece()

    def test_general(self):
        p = Test_Piece(name="test piece")
        self.assertEqual(p.get_name(self.context), "test piece")
        self.assertEqual(p.get_mill_points(self.context), 0)
        self.assertEqual(p.get_knight_points(self.context), 0)
        self.assertEqual(p.get_win_points(self.context), 0)
