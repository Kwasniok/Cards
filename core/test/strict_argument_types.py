import unittest
from ..strict_argument_types import (
    strict_argument_types,
    Strict_Argument_Type_Error,
)


class Test(unittest.TestCase):
    def test_general(self):
        @strict_argument_types
        def f(a: (int, float), b):
            return a, b

        # wrapping
        self.assertEquals(f(a=7, b=9), (7, 9))
        self.assertEquals(f(a=7.0, b=9), (7.0, 9))
        # non-keyword arguments not permitted
        with self.assertRaises(Strict_Argument_Type_Error):
            f(1, 2)
        # strict types
        with self.assertRaises(Strict_Argument_Type_Error):
            f(a="str not allowed", b="str allowed")
