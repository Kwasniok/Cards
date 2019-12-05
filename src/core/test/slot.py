import unittest
from ..slot import Slot, Slot_Full_Error


class Test_Base:
    pass


class Test_Derived(Test_Base):
    pass


class Test(unittest.TestCase):
    def test_general(self):
        obj_base = Test_Base()
        obj_derived = Test_Derived()
        accepted_base_types = [Test_Base]
        slot = Slot(accepted_base_types=accepted_base_types, limit=2)
        # getter
        self.assertEquals(slot.get_limit(), 2)
        self.assertEquals(
            slot.get_accepted_base_types(), accepted_base_types[:]
        )
        # empty/full (empty)
        self.assertTrue(slot.is_empty())
        self.assertFalse(slot.is_full())
        # accepts_type (empty)
        self.assertTrue(slot.accepts_type(Test_Base))
        self.assertTrue(slot.accepts_type(Test_Derived))
        self.assertFalse(slot.accepts_type(int))
        self.assertFalse(slot.accepts_type(list))
        # would accept
        self.assertTrue(slot.would_accept(obj_base))
        self.assertTrue(slot.would_accept(obj_derived))
        self.assertFalse(slot.would_accept(1))
        self.assertFalse(slot.would_accept([]))
        # add (accepted)
        slot.add(obj_base)
        slot.add(obj_derived)
        # slicable
        self.assertEquals(slot[0], obj_base)
        # add (allready present)
        self.assertFalse(slot.would_accept(obj_base))
        with self.assertRaises(ValueError):
            slot.add(obj_base)
        # add (full)
        self.assertFalse(slot.would_accept(Test_Derived()))
        with self.assertRaises(Slot_Full_Error):
            slot.add(Test_Derived())
        # raise limit
        slot._limit += 1
        # add (wrong type)
        self.assertFalse(slot.would_accept(1))
        with self.assertRaises(TypeError):
            slot.add(1)
        self.assertFalse(slot.would_accept([]))
        with self.assertRaises(TypeError):
            slot.add([])
        # lower limit
        slot._limit -= 1
        # empty/full (full)
        self.assertFalse(slot.is_empty())
        self.assertTrue(slot.is_full())
        # accepts_type (full)
        self.assertTrue(slot.accepts_type(Test_Base))
        self.assertTrue(slot.accepts_type(Test_Derived))
        self.assertFalse(slot.accepts_type(int))
        self.assertFalse(slot.accepts_type(list))
        # __contains__
        self.assertTrue(obj_base in slot)
        self.assertTrue(obj_derived in slot)
        self.assertFalse(1 in slot)
        self.assertFalse([] in slot)
        # __len__
        self.assertEquals(len(slot), 2)
        # remove (present)
        slot.remove(obj_base)
        # remove (not present)
        slot.remove(1)
        # __len__
        self.assertEquals(len(slot), 1)
        # get top
        self.assertTrue(slot.get_top() == obj_derived)
        # pop top
        self.assertTrue(slot.pop_top() == obj_derived)
        # __len__
        self.assertEquals(len(slot), 0)
