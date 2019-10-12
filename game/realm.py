from collections import defaultdict
from core.random import random_pop
from core.two_sided_stack import Two_Sided_Stack
from core.internally_named import Internally_Named
from core.owning import Owned
from .directions import RIGHT, LEFT
from .card_slot import Card_Slot
from .structure_cards import Road_Card, Settlement_Card
from .resource_cards import Resource_Card
from .expansion_card import Building_Card


class Realm(Internally_Named, Owned):
    def __init__(self, name, owner):
        Internally_Named.__init__(self, name)
        Owned.__init__(self, owner=owner)
        self._card_slot_grid = Two_Sided_Stack()

    def get_name(self):
        return str(self)

    def __repr__(self):
        return (
            "Realm(name='"
            + self.get_name()
            + "', owner="
            + str(self.get_owner())
            + ", card_slot_grid="
            + repr(self._card_slot_grid)
            + ")"
        )

    def get_card_slot_grid(self):
        return self._card_slot_grid

    def on_place_initial_resources(self, resource_cards):
        card_types = set([type(c) for c in resource_cards])
        card_slots = []
        for card_slot_column in self._card_slot_grid:
            for card_slot in card_slot_column:
                for card_type in card_types:
                    if card_slot.accepts_type(card_type):
                        card_slots.append(card_slot)
                        break
        if len(resource_cards) != len(card_slots):
            raise (
                ValueError(
                    "Cannot place initial resources. Missmatch in number of available slots ("
                    + str(len(card_slots))
                    + ") and provided cards("
                    + str(len(resource_cards))
                    + ")"
                )
            )
        # walk along all avalable resource slots and fill in randomly chosen
        # initial resource cards
        for slot in card_slots:
            card = random_pop(resource_cards)
            card.change_owner(self.get_owner())
            card.make_face_up()
            slot.add(card)

    def on_prepare_initial_state(self):
        rsc = self._add_road_slot_column(RIGHT)
        srsc = self._add_settlement_slot_column(RIGHT)
        slsc = self._add_settlement_slot_column(LEFT)
        card = Road_Card()
        card.change_owner(self.get_owner())
        card.make_face_up()
        rsc[2].add(card)
        card = Settlement_Card()
        card.change_owner(self.get_owner())
        card.make_face_up()
        srsc[2].add(card)
        card = Settlement_Card()
        card.change_owner(self.get_owner())
        card.make_face_up()
        slsc[2].add(card)
        self._add_road_slot_column(RIGHT)
        self._add_road_slot_column(LEFT)

    def _draw_to_str(self):
        s = ""
        X = len(self._card_slot_grid)
        Y = 5
        symbols = {}
        symbols[Road_Card] = "R"
        symbols[Settlement_Card] = "S"
        for y in range(Y):
            row = []
            for x in range(X):
                slot = self._card_slot_grid[x][y]
                if slot.is_empty():
                    row.append("_")
                else:
                    card = slot.get_top()
                    symbol = "?"
                    for clss, clss_symbol in symbols.items():
                        if isinstance(card, clss):
                            symbol = clss_symbol
                    row.append(symbol)
            row = " ".join(row)
            s += row + "\n"
        return s

    def _add_road_slot_column(self, direction):
        column = [
            Card_Slot(
                name="locked slot",
                owner=self._owner,
                accepted_base_types=[],
                limit=1,
            ),
            Card_Slot(
                name="resource slot",
                owner=self._owner,
                accepted_base_types=[Resource_Card],
                limit=1,
            ),
            Card_Slot(
                name="road slot",
                owner=self._owner,
                accepted_base_types=[Road_Card],
                limit=1,
            ),
            Card_Slot(
                name="resource slot",
                owner=self._owner,
                accepted_base_types=[Resource_Card],
                limit=1,
            ),
            Card_Slot(
                name="locked slot",
                owner=self._owner,
                accepted_base_types=[],
                limit=1,
            ),
        ]
        return self._add_slot_column(column, direction)

    def _add_settlement_slot_column(self, direction):
        column = [
            Card_Slot(
                name="town building slot",
                owner=self._owner,
                accepted_base_types=[Building_Card],
                limit=1,
            ),
            Card_Slot(
                name="building slot",
                owner=self._owner,
                accepted_base_types=[Building_Card],
                limit=1,
            ),
            Card_Slot(
                name="settlement slot",
                owner=self._owner,
                accepted_base_types=[Settlement_Card],
                limit=1,
            ),
            Card_Slot(
                name="building slot",
                owner=self._owner,
                accepted_base_types=[Building_Card],
                limit=1,
            ),
            Card_Slot(
                name="town building slot",
                owner=self._owner,
                accepted_base_types=[Building_Card],
                limit=1,
            ),
        ]
        return self._add_slot_column(column, direction)

    def _add_slot_column(self, column, direction):
        if direction is RIGHT:
            self._card_slot_grid.push_right(column)
        if direction is LEFT:
            self._card_slot_grid.push_left(column)
        return column

    def get_mill_points(self, context):
        ps = 0
        for column in self._card_slot_grid:
            for slot in column:
                for card in slot:
                    ps += card.get_mill_points(context)
        return ps

    def get_knight_points(self, context):
        ps = 0
        for column in self._card_slot_grid:
            for slot in column:
                for card in slot:
                    ps += card.get_knight_points(context)
        return ps

    def get_win_points(self, context):
        ps = 0
        for column in self._card_slot_grid:
            for slot in column:
                for card in slot:
                    ps += card.get_win_points(context)
        return ps
