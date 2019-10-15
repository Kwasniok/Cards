from game.structure_card import Structure_Card
from .resource_types import *


class Road_Card(Structure_Card):
    def __init__(self):
        Structure_Card.__init__(self, name="Road")

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
        Structure_Card.__init__(self, name="Settlement")

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
        Structure_Card.__init__(self, name="Town")

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
