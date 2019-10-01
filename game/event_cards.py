from abc import abstractmethod
from game.card import Card


class Event_Card(Card):
    def __init__(self, name):
        Card.__init__(self, name)

    @abstractmethod
    def on_discovery(self, context):
        pass
