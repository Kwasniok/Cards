import unittest
import time
from ..pulsed_trigger import Pulsed_Trigger


class Listener:
    def __init__(self):
        self._pulled = 0

    def on_pull(self):
        self._pulled += 1

    def pull_count(self):
        return self._pulled

    def reset(self):
        self._pulled = 0


class Test(unittest.TestCase):
    def test_general(self):
        pulsed_trigger = Pulsed_Trigger(max_pps=5000)
        listener = Listener()
        # register listener
        pulsed_trigger.register(listener, Listener.on_pull)
        # test pull (forced pull)
        Pulsed_Trigger.pull_all()
        self.assertEquals(listener.pull_count(), 1)
        # measure the pull frequency R times
        R = 10
        for r in range(R):
            # pull N times
            N = 100
            i = 0
            listener.reset()
            pulsed_trigger.restart()
            t0 = time.perf_counter()
            while listener.pull_count() < N:
                Pulsed_Trigger.update_all()
            t1 = time.perf_counter()
            # check pull count
            self.assertEquals(N, listener._pulled)
            # measure actual pull frequency
            real_pps = float(N) / (t1 - t0)
            self.assertTrue(pulsed_trigger._max_pps > real_pps)
        # unregister listener
        pulsed_trigger.unregister(listener)
        # n more pulls
        n = 3
        dummy_listener = Listener()
        # register listener
        pulsed_trigger.register(dummy_listener, Listener.on_pull)
        while dummy_listener.pull_count() < n:
            Pulsed_Trigger.update_all()
        # listener must remain unchanged
        self.assertEquals(N, listener._pulled)
