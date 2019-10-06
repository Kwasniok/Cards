import unittest
import time
from ..pulsed_trigger import Pulsed_Trigger


class Listener:
    def __init__(self):
        self._pulled = 0

    def on_pull(self):
        self._pulled += 1


class Test(unittest.TestCase):
    def test_general(self):
        max_pps = 250
        pulsed_trigger = Pulsed_Trigger(max_pps=max_pps)
        listener = Listener()
        # register listener
        pulsed_trigger.register(listener, Listener.on_pull)
        # pull N times
        N = 25
        i = 0
        t0 = time.time()
        while i < N:
            self.assertEquals(i, listener._pulled)
            if pulsed_trigger.update():
                i += 1
        t1 = time.time()
        # measure actual pull frequency
        real_pps = float(N) / (t1 - t0)
        self.assertTrue(max_pps > real_pps)
        # unregister listener
        pulsed_trigger.unregister(listener)
        # N more pulls
        N = 3
        while N > 0:
            if pulsed_trigger.update():
                N -= 1
        # listener must remain unchanged
        self.assertEquals(i, listener._pulled)
