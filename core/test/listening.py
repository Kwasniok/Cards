import unittest
from ..listening import Listenable, listenable


class Test(unittest.TestCase):
    def test_general(self):
        class Test_Listenable(Listenable):
            actionC = None

            def __init__(self):
                Listenable.__init__(self)
                self._actionA = 0
                self._actionB = 0
                self._actionC = 0

            @listenable
            def actionA(self):
                self._actionA += 1

            def actionB(self):
                self._actionB += 1

        class Test_Listener:
            def __init__(self):
                self._actionA = 0
                self._actionB = 0
                self._actionC = 0

            def on_actionA(self):
                self._actionA += 1

            def on_actionB(self):
                self._actionA += 1

            def on_actionC(self):
                self._actionA += 1

        test_listenable = Test_Listenable()
        test_listener = Test_Listener()
        test_listenable.register_listener(
            "actionA", test_listener, Test_Listener.on_actionA
        )
        with self.assertRaises(ValueError):
            test_listenable.register_listener(
                "actionB", test_listener, Test_Listener.on_actionB
            )
        with self.assertRaises(ValueError):
            test_listenable.register_listener(
                "actionC", test_listener, Test_Listener.on_actionC
            )
        # 'call' as actions
        test_listenable.actionA()
        test_listenable.actionB()
        test_listenable.actionC
        # check listener
        self.assertEquals(test_listener._actionA, 1)
        self.assertEquals(test_listener._actionB, 0)
        self.assertEquals(test_listener._actionC, 0)
