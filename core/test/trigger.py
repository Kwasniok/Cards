import unittest
from ..trigger import Trigger


class Listener:
    def __init__(self):
        self._pulled = 0

    def on_pull(self):
        self.pulled += 1


class Test(unittest.TestCase):
    def test_general(self):
        trigger = Trigger()
        listner = Listener()
        trigger.pull()
        self.assertEquals(listner._pulled, 0)
        trigger.register(listner)
        trigger.pull()
        self.assertEquals(listner._pulled, 1)
        trigger.unregister(listner)
        trigger.pull()
        self.assertEquals(listner._pulled, 1)
