import unittest
from ..owning import Owner, Owned


class Test(unittest.TestCase):
    def test_abstract(self):
        with self.assertRaises(TypeError):
            Owned()

    def test_owned(self):
        class Test_Owned(Owned):
            def __init__(self, owner):
                Owned.__init__(self, owner)

        class Test_Owner(Owner):
            def __init__(self):
                Owner.__init__(self)

        owner1 = Test_Owner()
        owner2 = Test_Owner()
        owned = Test_Owned(owner1)
        with self.assertRaises(TypeError):
            Test_Owned(1)
        self.assertEqual(owned.get_owner(), owner1)
        owned.change_owner(owner2)
        self.assertEqual(owned.get_owner(), owner2)
        with self.assertRaises(TypeError):
            owned.change_owner(1)
