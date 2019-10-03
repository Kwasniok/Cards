import unittest
import tkinter as tk
from ..application import Application
from ..window import Window


class Test(unittest.TestCase):
    def setUp(self):
        self._application = None

    def test_general(self):
        self._application = Application()
        # self._application.run()
        self._application.destroy()
        self._application = None

    # destroy application when test failed
    def tearDown(self):
        if not (self._application is None):
            self._application.destroy()
            self._application = None
