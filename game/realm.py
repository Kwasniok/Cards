from core.two_sided_stack import Two_Sided_Stack
from core.directions import RIGHT, LEFT
from core.owning import Owned
from core.card_slot import Card_Slot
from .cards import Road_Card, Settlement_Card


class Realm(Owned):
    def __init__(self, name, owner):
        Owned.__init__(self, owner=owner)
        self._name = name
        self._structure_slots = Two_Sided_Stack()
        self._prepare_initial_state()

    def __str__(self):
        return self._name

    def __repr__(self):
        return (
            "Realm(name='"
            + self._name
            + "', owner="
            + str(self.owner())
            + ", structure_slots="
            + repr(self._structure_slots)
            + ")"
        )

    def get_structure_slots(self):
        return self._structure_slots

    def size(self):
        return len(self._structure_slots) - 2

    def _draw_to_str(self):
        s = []
        for slot in self._structure_slots:
            if slot.is_empty():
                s.append("_")
            else:
                card = slot.get_top()
                if isinstance(card, Road_Card):
                    s.append("R")
                if isinstance(card, Settlement_Card):
                    s.append("S")
        return "-".join(s)

    def _prepare_initial_state(self):
        rs = self._add_road_slot(RIGHT)
        srs = self._add_settlement_slot(RIGHT)
        sls = self._add_settlement_slot(LEFT)
        card = Road_Card()
        card.owner(self.owner())
        rs.add(card)
        card = Settlement_Card()
        card.owner(self.owner())
        srs.add(card)
        card = Settlement_Card()
        card.owner(self.owner())
        sls.add(card)
        self._add_road_slot(RIGHT)
        self._add_road_slot(LEFT)

    def _add_road_slot(self, direction):
        slot = Card_Slot(
            name="road slot",
            owner=self._owner,
            possible_card_types=[Road_Card],
            limit=1,
        )
        return self._add_slot(slot, direction)

    def _add_settlement_slot(self, direction):
        slot = Card_Slot(
            name="settlement slot",
            owner=self._owner,
            possible_card_types=[Settlement_Card],
            limit=1,
        )
        return self._add_slot(slot, direction)

    def _add_slot(self, slot, direction):
        if direction is RIGHT:
            self._structure_slots.push_right(slot)
        if direction is LEFT:
            self._structure_slots.push_left(slot)
        return slot

    def extend(self, card, direction):
        if card in [c for slot in self._structure_slots for c in slot]:
            raise ValueError(
                "Card `"
                + str(card)
                + "` cannot be added to realm `"
                + str(self)
                + "` because it is allready present in this realm."
            )
        if not isinstance(card, (Road_Card, Settlement_Card)):
            raise ValueError(
                "Card `"
                + str(card)
                + "` cannot be added to realm `"
                + str(self)
                + "` because it is not a valid strucutre road (must be one of "
                + ", ".join(["`" + str(t) + "`" for t in structure_cards])
                + ")."
            )
        if direction == RIGHT:
            slot = self._structure_slots.get_right()
        if direction == LEFT or len(self._structure_slots) == 1:
            slot = self._structure_slots.get_left()
        slot.add(card)  # trows
        if isinstance(card, Road_Card):
            self._add_settlement_slot(direction)
        if isinstance(card, Settlement_Card):
            self._add_road_slot(direction)

    def upgrade(self, settlement, card):
        if not settlement in self._structure_slots:
            raise (
                ValueError(
                    "Cannot upgrade settlment `"
                    + str(settlment)
                    + "` because it is not in realm `"
                    + str(self)
                    + "`."
                )
            )
        if not isinstance(card, Town_Card):
            raise (
                ValueError(
                    "Cannot upgrade settlment `"
                    + str(settlment)
                    + "` in realm `"
                    + str(self)
                    + "` because `"
                    + str(card)
                    + "` is not a town."
                )
            )
