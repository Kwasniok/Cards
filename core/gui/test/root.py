import unittest
import tkinter as tk
from ..root import Root


class Test(unittest.TestCase):
    def test_general(self):
        r = Root.get_root()
        self.assertIsInstance(r, tk.Tk)
        # singleton
        self.assertTrue(r is Root.get_root())
        Root.register_application(1)
        with self.assertRaises(RuntimeError):
            Root.register_application(2)
        Root.unregister_application()
        Root.register_application(2)
        Root.unregister_application()

    def tearDown(self):
        Root.unregister_application()
