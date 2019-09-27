import unittest
from ..owning import Owner, Owned


class Test(unittest.TestCase):
    def test_owner(self):
        o = Owner(name="test owner")

    def test_owned(self):
        class Test_Owned(Owned):
            def __init__(self, owner):
                Owned.__init__(self, owner)

        owner1 = Owner(name="test owner 1")
        owner2 = Owner(name="test owner 2")
        owned = Test_Owned(owner1)
        self.assertEqual(owned.owner(), owner1)
        self.assertEqual(owned.owner(owner2), owner1)
        self.assertEqual(owned.owner(), owner2)
