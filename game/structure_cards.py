from abc import ABC, abstractmethod
from game.card import Card
from .resource_types import LOGS, BRICKS, GRAIN, IRON, WOOL, GOLD


class Structure_Card(Card):
    def __init__(self, name):
        Card.__init__(self, name=name)

    def title(self, context):
        return self.get_name()

    def text(self, context):
        return (
            self._name
            + " ("
            + " ".join([res.name() for res in self.cost(context)])
            + ")"
        )


class Road_Card(Structure_Card):
    def __init__(self):
        Card.__init__(self, name="Road")

    def cost(self, context):
        return [BRICKS, BRICKS, LOGS]


class Settlement_Card(Structure_Card):
    def __init__(self):
        Card.__init__(self, name="Settlement")

    def cost(self, context):
        return [LOGS, WOOL, BRICKS, GRAIN]

    def win_points(self, context):
        return 1


class Town_Card(Structure_Card):
    def __init__(self):
        Card.__init__(self, name="Twon")

    def cost(self, context):
        return [IRON, IRON, IRON, GRAIN, GRAIN]
