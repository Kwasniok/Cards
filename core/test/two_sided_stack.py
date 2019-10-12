import unittest
import operator
from functools import reduce
from ..two_sided_stack import Two_Sided_Stack


class Test(unittest.TestCase):
    def test_general(self):
        s = Two_Sided_Stack()
        self.assertTrue(len(s) == 0)
        # cannot pop empty stack
        with self.assertRaises(IndexError):
            s.pop_left()
        with self.assertRaises(IndexError):
            s.pop_right()
        s.push_right(3)
        s.push_left(2)
        s.push_right(4)
        s.push_left(1)
        self.assertEquals(len(s), 4)
        self.assertTrue(2 in s)
        self.assertTrue(4 in s)
        # stack should be 1,2,3,4 (and iterable)
        self.assertTrue(
            reduce(operator.__and__, [x == y for x, y in zip(range(1, 5), s)])
        )
        # slicable
        self.assertEquals(s[2], 3)
        # no deletion
        with self.assertRaises(TypeError):
            del s[0]
        # pop and peek
        s.pop_right()
        self.assertEquals(s.get_right(), 3)
        self.assertEquals(len(s), 3)
        s.pop_left()
        self.assertEquals(s.get_left(), 2)
        self.assertEquals(len(s), 2)
