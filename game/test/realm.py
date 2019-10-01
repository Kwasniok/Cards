import unittest
from core.directions import RIGHT, LEFT
from core.owning import Owner
from ..cards import Road_Card, Settlement_Card, Town_Card, Resource_Card
from ..resource_types import *
from ..realm import Realm


class Test(unittest.TestCase):
    def setUp(self):
        self.dummy_owner = Owner(name="dummy owner")

    def test_general(self):
        r = Realm(name="realm", owner=self.dummy_owner)
        # realm state: S-R-S (R:Road, S:Settlement)
        road1 = Road_Card()
        road2 = Road_Card()
        settlement1 = Settlement_Card()
        settlement2 = Settlement_Card()
        res1 = Resource_Card(LOGS, 1, 0)
        # first extension must be a road
        with self.assertRaises(ValueError):
            r.extend(settlement1, RIGHT)
        with self.assertRaises(ValueError):
            r.extend(settlement1, LEFT)
        # extend with road to the right
        r.extend(road1, RIGHT)
        # realm state: S-R-S-R (R:Road, S:Settlement)
        # no reuse of cards
        with self.assertRaises(ValueError):
            r.extend(road1, RIGHT)
        # road needs settlement or town
        with self.assertRaises(ValueError):
            r.extend(road2, RIGHT)
        # extend with road to the left
        r.extend(road2, LEFT)
        # realm state: R-S-R-S-R (R:Road, S:Settlement)
        # extend with settlement to the right
        r.extend(settlement1, RIGHT)
        # realm state: R-S-R-S-R-S (R:Road, S:Settlement)
        # no reuse of cards
        with self.assertRaises(ValueError):
            r.extend(settlement1, RIGHT)
        # settlement needs road
        with self.assertRaises(ValueError):
            r.extend(settlement2, RIGHT)
        # extend with settlement to the left
        r.extend(settlement2, LEFT)
        # realm state: S-R-S-R-S-R (R:Road, S:Settlement)
        # check state
        structure_slots = r.get_structure_slots()
        self.assertTrue(structure_slots[0].is_empty())
        self.assertTrue(structure_slots[1].is_full())
        self.assertIsInstance(structure_slots[1].get_top(), Settlement_Card)
        self.assertTrue(structure_slots[2].is_full())
        self.assertIsInstance(structure_slots[2].get_top(), Road_Card)
        self.assertTrue(structure_slots[3].is_full())
        self.assertIsInstance(structure_slots[3].get_top(), Settlement_Card)
        self.assertTrue(structure_slots[4].is_full())
        self.assertIsInstance(structure_slots[4].get_top(), Road_Card)
        self.assertTrue(structure_slots[5].is_full())
        self.assertIsInstance(structure_slots[5].get_top(), Settlement_Card)
        self.assertTrue(structure_slots[6].is_full())
        self.assertIsInstance(structure_slots[6].get_top(), Road_Card)
        self.assertTrue(structure_slots[7].is_full())
        self.assertIsInstance(structure_slots[7].get_top(), Settlement_Card)
        self.assertTrue(structure_slots[8].is_empty())
