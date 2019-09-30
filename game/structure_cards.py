from abc import ABC, abstractmethod
from core.card import Card
from .resource_types import LOGS, BRICKS, GRAIN, IRON, WOOL, GOLD


class Structure_Card(Card):
    def __init__(self, name):
        Card.__init__(self, name=name)

    def text(self):
        return (
            self._name
            + " ("
            + " ".join([res.name() for res in self.price()])
            + ")"
        )

    @abstractmethod
    def price(self):
        pass


class Road_Card(Structure_Card):
    def __init__(self):
        Card.__init__(self, name="Road")

    def price(self):
        return [BRICKS, BRICKS, LOGS]


class Settlement_Card(Structure_Card):
    def __init__(self):
        Card.__init__(self, name="Settlement")

    def price(self):
        return [LOGS, WOOL, BRICKS, GRAIN]


class Town_Card(Structure_Card):
    def __init__(self):
        Card.__init__(self, name="Twon")

    def price(self):
        return [IRON, IRON, IRON, GRAIN, GRAIN]
