import unittest
import tkinter as tk
from ..window import Window
from ..application import Application


class Test(unittest.TestCase):
    def setUp(self):
        self._application = Application()

    def test_general(self):
        w = Window(
            self._application,
            title="test window",
            width=100,
            height=100,
            x=0,
            y=0,
        )
        w.close()
        w.destroy()
        self.assertTrue(hasattr(w, "on_close_requested"))

    def tearDown(self):
        self._application.destroy()
