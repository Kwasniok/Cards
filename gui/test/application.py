import unittest
import tkinter as tk
from ..application import Application


class Test(unittest.TestCase):
    def setUp(self):
        self._application = None

    def test_general(self):
        self._application = Application()
        self._application.new_window(
            title="test window", width=100, height=100, x=0, y=0
        )
        self._application.destroy()
        self._application = None

    # destroy application when test failed
    def tearDown(self):
        if not (self._application is None):
            self._application.destroy()
            self._application = None
