import unittest
from ..neutral_owner import neutral_owner
from ..piece_tray import Piece_Tray
from ..piece import Piece


class Test_Piece(Piece):
    def __init__(self, name):
        Piece.__init__(self, name=name)

    def get_mill_points(self, context):
        return 1

    def get_knight_points(self, context):
        return 2

    def get_win_points(self, context):
        return 3


class Test(unittest.TestCase):
    def setUp(self):
        self.context = None

    def test_general(self):
        pt = Piece_Tray(name="test piece tray")
        # core.owning
        self.assertEqual(pt.get_owner(), neutral_owner)
        # core.internally_named
        self.assertEqual(str(pt), "test piece tray")
        # empty
        self.assertEqual(pt.get_mill_points(self.context), 0)
        self.assertEqual(pt.get_knight_points(self.context), 0)
        self.assertEqual(pt.get_win_points(self.context), 0)
        self.assertEqual(len(pt), 0)
        # add
        p = Test_Piece(name="test piece")
        pt.add(p)
        with self.assertRaises(ValueError):
            pt.add(p)
        # one piece
        self.assertEqual(pt.get_mill_points(self.context), 1)
        self.assertEqual(pt.get_knight_points(self.context), 2)
        self.assertEqual(pt.get_win_points(self.context), 3)
        self.assertEqual(len(pt), 1)
        self.assertTrue(p in pt)
        self.assertTrue(pt[0] is p)
        xs = []
        for x in pt:
            xs.append(x)
        self.assertEqual(len(xs), 1)
        self.assertTrue(xs[0] is p)
        # remove
        pt.remove(p)
        pt.remove(p)
        # empty
        self.assertEqual(pt.get_mill_points(self.context), 0)
        self.assertEqual(pt.get_knight_points(self.context), 0)
        self.assertEqual(pt.get_win_points(self.context), 0)
        self.assertEqual(len(pt), 0)
