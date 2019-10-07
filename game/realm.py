from collections import defaultdict
from core.two_sided_stack import Two_Sided_Stack
from core.directions import RIGHT, LEFT
from core.owning import Owned
from core.card_slot import Card_Slot
from .all_cards import Road_Card, Settlement_Card, Resource_Card, Building_Card


class Realm(Owned):
    def __init__(self, name, owner):
        Owned.__init__(self, owner=owner)
        self._name = name
        self._card_slot_grid = Two_Sided_Stack()

    def __str__(self):
        return self._name

    def __repr__(self):
        return (
            "Realm(name='"
            + self._name
            + "', owner="
            + str(self.owner())
            + ", card_slot_grid="
            + repr(self._card_slot_grid)
            + ")"
        )

    def get_card_slot_grid(self):
        return self._card_slot_grid

    def size(self):
        return len(self._card_slot_grid)

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

    def on_prepare_initial_state(self):
        rsc = self._add_road_slot_column(RIGHT)
        srsc = self._add_settlement_slot_column(RIGHT)
        slsc = self._add_settlement_slot_column(LEFT)
        card = Road_Card()
        card.owner(self.owner())
        rsc[2].add(card)
        card = Settlement_Card()
        card.owner(self.owner())
        srsc[2].add(card)
        card = Settlement_Card()
        card.owner(self.owner())
        slsc[2].add(card)
        self._add_road_slot_column(RIGHT)
        self._add_road_slot_column(LEFT)

    def _add_road_slot_column(self, direction):
        column = [
            Card_Slot(
                name="locked slot",
                owner=self._owner,
                possible_card_types=[],
                limit=1,
            ),
            Card_Slot(
                name="resource slot",
                owner=self._owner,
                possible_card_types=[Resource_Card],
                limit=1,
            ),
            Card_Slot(
                name="road slot",
                owner=self._owner,
                possible_card_types=[Road_Card],
                limit=1,
            ),
            Card_Slot(
                name="resource slot",
                owner=self._owner,
                possible_card_types=[Resource_Card],
                limit=1,
            ),
            Card_Slot(
                name="locked slot",
                owner=self._owner,
                possible_card_types=[],
                limit=1,
            ),
        ]
        return self._add_slot_column(column, direction)

    def _add_settlement_slot_column(self, direction):
        column = [
            Card_Slot(
                name="town building slot",
                owner=self._owner,
                possible_card_types=[Building_Card],
                limit=1,
            ),
            Card_Slot(
                name="building slot",
                owner=self._owner,
                possible_card_types=[Building_Card],
                limit=1,
            ),
            Card_Slot(
                name="settlement slot",
                owner=self._owner,
                possible_card_types=[Settlement_Card],
                limit=1,
            ),
            Card_Slot(
                name="building slot",
                owner=self._owner,
                possible_card_types=[Building_Card],
                limit=1,
            ),
            Card_Slot(
                name="town building slot",
                owner=self._owner,
                possible_card_types=[Building_Card],
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

    def mill_points(self, context):
        ps = 0
        for column in self._card_slot_grid:
            for slot in column:
                for card in slot:
                    ps += card.mill_points(context)
        return ps

    def knight_points(self, context):
        ps = 0
        for column in self._card_slot_grid:
            for slot in column:
                for card in slot:
                    ps += card.knight_points(context)
        return ps

    def win_points(self, context):
        ps = 0
        for column in self._card_slot_grid:
            for slot in column:
                for card in slot:
                    ps += card.win_points(context)
        return ps
