from abc import ABC, abstractmethod
from game.card import Card
from .resource_types import LOGS, BRICKS, GRAIN, IRON, WOOL, GOLD


class Structure_Card(Card):
    def __init__(self, name):
        Card.__init__(self, name=name)

    def __repr__(self):
        return (
            "Structure_Card(name="
            + repr(self._get_internal_name())
            + ",owner="
            + str(self.get_owner())
            + ",face_up="
            + str(self._face_up)
            + ")"
        )

    def get_title(self, context):
        return self._get_internal_name()


class Road_Card(Structure_Card):
    def __init__(self):
        Card.__init__(self, name="Road")

    def __repr__(self):
        return (
            "Structure_Card(name="
            + repr(self._get_internal_name())
            + ",owner="
            + str(self.get_owner())
            + ",face_up="
            + str(self._face_up)
            + ")"
        )

    def get_cost(self, context):
        return [BRICKS, BRICKS, LOGS]


class Settlement_Card(Structure_Card):
    def __init__(self):
        Card.__init__(self, name="Settlement")

    def __repr__(self):
        return (
            "Settlement_Card(name="
            + repr(self._get_internal_name())
            + ",owner="
            + str(self.get_owner())
            + ",face_up="
            + str(self._face_up)
            + ")"
        )

    def get_cost(self, context):
        return [LOGS, WOOL, BRICKS, GRAIN]

    def get_win_points(self, context):
        return 1


class Town_Card(Structure_Card):
    def __init__(self):
        Card.__init__(self, name="Twon")

    def __repr__(self):
        return (
            "Town_Card(name="
            + repr(self._get_internal_name())
            + ",owner="
            + str(self.get_owner())
            + ",face_up="
            + str(self._face_up)
            + ")"
        )

    def get_cost(self, context):
        return [IRON, IRON, IRON, GRAIN, GRAIN]
