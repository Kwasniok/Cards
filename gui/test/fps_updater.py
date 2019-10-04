import unittest
import time
from ..update import Updatable
from ..fps_updater import FPS_Updater


class Test(unittest.TestCase):
    def test_general(self):
        # abstract class
        with self.assertRaises(TypeError):
            Updatable()

        class Test_Updatable(Updatable):
            def __init__(self):
                Updatable.__init__(self)
                self._counter = 0

            def on_update(self):
                self._counter += 1

        fps_bound = 100
        updater = FPS_Updater(fps_bound=fps_bound)
        updatable = Test_Updatable()
        updater.register(updatable)
        N = 25
        i = 0
        t0 = time.time()
        while i < N:
            self.assertEquals(i, updatable._counter)
            if updater.update_all():
                i += 1
        t1 = time.time()
        fps_real = float(N) / (t1 - t0)
        self.assertTrue(fps_bound > fps_real)
        updater.clear()
