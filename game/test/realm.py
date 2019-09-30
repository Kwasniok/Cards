import unittest
from core.directions import RIGHT, LEFT
from core.owning import Owner
from ..cards import Road_Card, Settlement_Card, Town_Card, Resource_Card
from ..resource_types import *
from ..realm import Realm


class Test(unittest.TestCase):
    def setUp(self):
        self.dummy_owner = Owner(name="owner")

    def test_general(self):
        r = Realm(name="realm", owner=self.dummy_owner)
        road1 = Road_Card()
        road2 = Road_Card()
        settlement1 = Settlement_Card()
        settlement2 = Settlement_Card()
        res1 = Resource_Card(LOGS, 1, 0)
        # first strucutre must be a street
        with self.assertRaises(ValueError):
            r.extend(settlement1, RIGHT)
        #  first road needs no direction
        r.extend(road1, None)
        # no reuse of cards
        with self.assertRaises(ValueError):
            r.extend(road1, RIGHT)
        # road needs settlement or town
        with self.assertRaises(ValueError):
            r.extend(road2, RIGHT)
        with self.assertRaises(ValueError):
            r.extend(road2, LEFT)
        # extend to the left and right
        r.extend(settlement1, RIGHT)
        # no reuse of cards
        with self.assertRaises(ValueError):
            r.extend(settlement1, RIGHT)
        # settlement needs road
        with self.assertRaises(ValueError):
            r.extend(settlement2, RIGHT)
        r.extend(settlement2, LEFT)
