from core.directions import RIGHT, LEFT
from core.owning import Owned
from core.card_slot import Card_Slot
from .cards import Road_Card, Settlement_Card


class Realm(Owned):
    def __init__(self, name, owner, size=9):
        Owned.__init__(self, owner=owner)
        self._name = name
        self._structures = []

    def extend(self, card, direction):
        if card in self._structures:
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

        if len(self._structures) == 0:
            if isinstance(card, Road_Card):
                self._structures.append(card)
            else:
                raise ValueError(
                    "Card `"
                    + str(card)
                    + "` cannot be added to realm `"
                    + str(self)
                    + "` because the first card needs to be a `"
                    + str(Road_Card)
                    + "`."
                )
        else:
            if direction == RIGHT:
                neighbor_index = -1
                insert_index = len(self._structures)
            elif direction == LEFT:
                neighbor_index = 0
                insert_index = 0
            else:
                raise ValueError(
                    "Could not add "
                    + str(card)
                    + " to realm `"
                    + str(self)
                    + "` because of the invalid direction `"
                    + str(direction)
                    + "` (must be either `"
                    + str(LEFT)
                    + "` or `"
                    + str(RIGHT)
                    + "`)"
                )
            if isinstance(card, Road_Card):
                neighbor_type = Settlement_Card
            if isinstance(card, Settlement_Card):
                neighbor_type = Road_Card
            if isinstance(self._structures[neighbor_index], neighbor_type):
                self._structures.insert(insert_index, card)
            else:
                raise ValueError(
                    "Could not add "
                    + str(card)
                    + " at "
                    + str(direction)
                    + " to realm `"
                    + str(self)
                    + "` because of mismatching neighoring card"
                    + "` (neigbor must be a `"
                    + str(neighbor_type)
                    + "`)."
                )

    def upgrade(self, settlement, card):
        if not settlement in self._structures:
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
