import unittest
import time
from ..update import Updatable
from ..frequency_updater import Frequency_Updater


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

        max_ups = 100
        updater = Frequency_Updater(max_ups=max_ups)
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
        ups_real = float(N) / (t1 - t0)
        self.assertTrue(max_ups > ups_real)
        updater.clear()
