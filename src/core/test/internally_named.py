import unittest
from ..internally_named import Internally_Named


class Test(unittest.TestCase):
    def test_general(self):
        class Test_Internally_Named(Internally_Named):
            pass

        obj = Test_Internally_Named(name="test name")
        self.assertTrue(str(obj) == "test name")
        self.assertTrue(obj._get_internal_name() == "test name")
        obj._set_internal_name("new test name")
        self.assertTrue(str(obj) == "new test name")
        self.assertTrue(obj._get_internal_name() == "new test name")
