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
    def test_start_stop(self):
        pulsed_trigger = Pulsed_Trigger(max_pps=1)
        listener = Listener()
        # register listener
        pulsed_trigger.register(listener, Listener.on_pull)
        # test pull
        listener.reset()
        Pulsed_Trigger.pull_all()
        self.assertEquals(listener.pull_count(), 1)
        # stop
        pulsed_trigger.stop()
        listener.reset()
        Pulsed_Trigger.pull_all()
        self.assertEquals(listener.pull_count(), 0)
        # restart
        pulsed_trigger.restart()
        listener.reset()
        Pulsed_Trigger.pull_all()
        self.assertEquals(listener.pull_count(), 1)

    def test_registration(self):
        pulsed_trigger = Pulsed_Trigger(max_pps=5000)
        listener = Listener()
        # register listener
        pulsed_trigger.register(listener, Listener.on_pull)
        # test pull (forced pull)
        listener.reset()
        Pulsed_Trigger.pull_all()
        self.assertEquals(listener.pull_count(), 1)
        # unregister listener
        listener.reset()
        pulsed_trigger.unregister(listener)
        Pulsed_Trigger.pull_all()
        self.assertEquals(listener.pull_count(), 0)

    def test_performance(self):
        pulsed_trigger = Pulsed_Trigger(max_pps=5000)
        listener = Listener()
        # register listener
        pulsed_trigger.register(listener, Listener.on_pull)
        # test pull (forced pull)
        listener.reset()
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
