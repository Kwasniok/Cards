import unittest
from ..update import Updater, Updatable


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

        updater = Updater()
        updater.register(Test_Updatable())
        updatable = Test_Updatable()
        updater.register(updatable)
        updater.register(Test_Updatable())
        with self.assertRaises(TypeError):
            updater.register(1)
        N = 10
        for i in range(N):
            self.assertEquals(i, updatable._counter)
            updater.update_all()
        updater.unregister(updatable)
        updater.update_all()
        self.assertEquals(updatable._counter, N)
        updater.register(updatable)
        updater.clear()
        updater.update_all()
        self.assertEquals(updatable._counter, N)
