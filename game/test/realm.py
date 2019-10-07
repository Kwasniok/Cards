import unittest
from core.directions import RIGHT, LEFT
from core.owning import Owner
from ..all_cards import Road_Card, Settlement_Card, Town_Card, Resource_Card
from ..expansion_cards import Storage_Card
from ..resource_types import *
from ..realm import Realm


class Test(unittest.TestCase):
    def setUp(self):
        self.dummy_owner = Owner(name="dummy owner")
        self._context = None

    def test_general(self):
        r = Realm(name="realm", owner=self.dummy_owner)
        slot_grid = r.get_card_slot_grid()
        self.assertEquals(len(slot_grid), 0)
        # prepare initial state
        r.on_prepare_initial_state()
        # realm state: S-R-S (R:Road, S:Settlement)
        # check state
        slot_grid = r.get_card_slot_grid()
        self.assertEquals(len(slot_grid), 5)
        card_slot_grid = r.get_card_slot_grid()
        for column in card_slot_grid:
            self.assertEquals(len(column), 5)
        self.assertEquals(slot_grid[0][2].possible_card_types(), [Road_Card])
        self.assertEquals(
            slot_grid[1][2].possible_card_types(), [Settlement_Card]
        )
        self.assertEquals(slot_grid[2][2].possible_card_types(), [Road_Card])
        self.assertEquals(
            slot_grid[3][2].possible_card_types(), [Settlement_Card]
        )
        self.assertEquals(slot_grid[4][2].possible_card_types(), [Road_Card])
        # initial points
        self.assertEquals(r.mill_points(self._context), 0)
        self.assertEquals(r.knight_points(self._context), 0)
        self.assertEquals(r.win_points(self._context), 2)
        # add storage (small building)
        storage_card = Storage_Card()
        storage_card.owner(self.dummy_owner)
        slot_grid[1][1].add(storage_card)
        with self.assertRaises(ValueError):
            slot_grid[2][1].add(storage_card)
        # points with storage
        self.assertEquals(r.mill_points(self._context), 1)
        self.assertEquals(r.knight_points(self._context), 0)
        self.assertEquals(r.win_points(self._context), 2)
