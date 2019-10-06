import unittest
import time
from ..pulsed_trigger import Pulsed_Trigger


class Listener:
    def __init__(self):
        self._pulled = 0

    def on_pull(self):
        self._pulled += 1

    def reset(self):
        self._pulled = 0


class Test(unittest.TestCase):
    def test_general(self):
        pulsed_trigger = Pulsed_Trigger(max_pps=5000)
        listener = Listener()
        # register listener
        pulsed_trigger.register(listener, Listener.on_pull)
        # measure the pull frequency R times
        R = 10
        for r in range(R):
            # pull N times
            N = 100
            i = 0
            listener.reset()
            pulsed_trigger.restart()
            t0 = time.perf_counter()
            while i < N:
                self.assertEquals(i, listener._pulled)
                if pulsed_trigger.update():
                    i += 1
            t1 = time.perf_counter()
            # measure actual pull frequency
            real_pps = float(N) / (t1 - t0)
            self.assertTrue(pulsed_trigger._max_pps > real_pps)
        # unregister listener
        pulsed_trigger.unregister(listener)
        # N more pulls
        N = 3
        while N > 0:
            if pulsed_trigger.update():
                N -= 1
        # listener must remain unchanged
        self.assertEquals(i, listener._pulled)
