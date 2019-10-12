import unittest
from core.owning import Owner
from ..directions import RIGHT, LEFT
from ..structure_cards import Road_Card, Settlement_Card, Town_Card
from ..resource_card import Resource_Card
from ..expansion_card import Small_Building_Card
from ..resource_types import *
from ..realm import Realm


class Test_Small_Building_Card(Small_Building_Card):
    def __init__(self):
        Small_Building_Card.__init__(self, "test small building card")

    def get_cost(self, context):
        return [LOGS, BRICKS]

    def get_mill_points(self, context):
        return 1


class Test(unittest.TestCase):
    def setUp(self):
        class Test_Owner(Owner):
            pass

        self.dummy_owner = Test_Owner()
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
        self.assertEquals(
            slot_grid[0][2].get_accepted_base_types(), [Road_Card]
        )
        self.assertEquals(
            slot_grid[1][2].get_accepted_base_types(), [Settlement_Card]
        )
        self.assertEquals(
            slot_grid[2][2].get_accepted_base_types(), [Road_Card]
        )
        self.assertEquals(
            slot_grid[3][2].get_accepted_base_types(), [Settlement_Card]
        )
        self.assertEquals(
            slot_grid[4][2].get_accepted_base_types(), [Road_Card]
        )
        # initial points
        self.assertEquals(r.get_mill_points(self._context), 0)
        self.assertEquals(r.get_knight_points(self._context), 0)
        self.assertEquals(r.get_win_points(self._context), 2)
        # add storage (small building)
        small_building_card = Test_Small_Building_Card()
        small_building_card.change_owner(self.dummy_owner)
        slot_grid[1][1].add(small_building_card)
        with self.assertRaises(TypeError):
            slot_grid[2][1].add(small_building_card)
        # points with storage
        self.assertEquals(r.get_mill_points(self._context), 1)
        self.assertEquals(r.get_knight_points(self._context), 0)
        self.assertEquals(r.get_win_points(self._context), 2)
