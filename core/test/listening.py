import unittest
from ..listening import Listenable, listenable


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


class Test_Listener_Drived(Test_Listener):
    def __init__(self):
        Test_Listener.__init__(self)
        self._actionA_derived = 0
        self._actionB_derived = 0
        self._actionC_derived = 0

    def on_actionA(self):
        self._actionA_derived += 1

    def on_actionB(self):
        self._actionA_derived += 1

    def on_actionC(self):
        self._actionA_derived += 1


actionA_global = 0
actionB_global = 0
actionC_global = 0


def on_actionA_global(unused):
    global actionA_global
    actionA_global += 1


def on_actionB_global(unused):
    global actionB_global
    actionB_global += 1


def on_actionC_global(unused):
    global actionB_global
    actionB_global += 1


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

        test_listenable = Test_Listenable()
        test_listener = Test_Listener()
        test_listener_derived = Test_Listener_Drived()
        # register normal listener
        test_listenable.register_listener(
            "actionA", test_listener, Test_Listener.on_actionA
        )
        # register derived listener
        test_listenable.register_listener(
            "actionA", test_listener_derived, "on_actionA"
        )
        # register global listener
        test_listenable.register_listener("actionA", None, on_actionA_global)
        ## test unreasonable registrations
        # bad method_name
        with self.assertRaises(ValueError):
            test_listenable.register_listener(
                "actionB", test_listener, Test_Listener.on_actionB
            )
        with self.assertRaises(ValueError):
            test_listenable.register_listener(
                "actionB", None, on_actionB_global
            )
        with self.assertRaises(ValueError):
            test_listenable.register_listener(
                "actionC", test_listener, Test_Listener.on_actionC
            )
        with self.assertRaises(ValueError):
            test_listenable.register_listener(
                "actionC", None, on_actionC_global
            )
        # bad listener_method
        with self.assertRaises(ValueError):
            test_listenable.register_listener("actionA", None, 2)
        with self.assertRaises(ValueError):
            test_listenable.register_listener("actionA", test_listener, 2)
        # bad listener_method (listener == None)
        with self.assertRaises(ValueError):
            test_listenable.register_listener(
                "actionA", None, "on_actionA_global"
            )
        # 'call' as actions
        test_listenable.actionA()
        test_listenable.actionB()
        test_listenable.actionC
        # check listener
        self.assertEquals(test_listener._actionA, 1)
        self.assertEquals(test_listener._actionB, 0)
        self.assertEquals(test_listener._actionC, 0)
        # check derived listener
        self.assertEquals(test_listener_derived._actionA, 0)
        self.assertEquals(test_listener_derived._actionB, 0)
        self.assertEquals(test_listener_derived._actionC, 0)
        self.assertEquals(test_listener_derived._actionA_derived, 1)
        self.assertEquals(test_listener_derived._actionB_derived, 0)
        self.assertEquals(test_listener_derived._actionC_derived, 0)
        # check global
        self.assertEquals(actionA_global, 1)
        self.assertEquals(actionB_global, 0)
        self.assertEquals(actionC_global, 0)
        # unregister
        test_listenable.unregister_listener("actionA", test_listener)
        test_listenable.unregister_listener("actionB", test_listener)
        test_listenable.unregister_listener("actionC", test_listener)
        test_listenable.unregister_listener("actionA", test_listener_derived)
        test_listenable.unregister_listener("actionB", test_listener_derived)
        test_listenable.unregister_listener("actionC", test_listener_derived)
        test_listenable.unregister_listener("actionA", None)
        test_listenable.unregister_listener("actionB", None)
        test_listenable.unregister_listener("actionC", None)
        # 'call' as actions (again)
        test_listenable.actionA()
        test_listenable.actionB()
        test_listenable.actionC
        # check listener (again)
        self.assertEquals(test_listener._actionA, 1)
        self.assertEquals(test_listener._actionB, 0)
        self.assertEquals(test_listener._actionC, 0)
        # check derived listener (agian)
        self.assertEquals(test_listener_derived._actionA, 0)
        self.assertEquals(test_listener_derived._actionB, 0)
        self.assertEquals(test_listener_derived._actionC, 0)
        self.assertEquals(test_listener_derived._actionA_derived, 1)
        self.assertEquals(test_listener_derived._actionB_derived, 0)
        self.assertEquals(test_listener_derived._actionC_derived, 0)
        # check global (again)
        self.assertEquals(actionA_global, 1)
        self.assertEquals(actionB_global, 0)
        self.assertEquals(actionC_global, 0)
