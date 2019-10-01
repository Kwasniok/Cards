from abc import abstractmethod
from core.card import Card


class Event_Card(Card):
    def __init__(self, name):
        Card.__init__(self, name)

    @abstractmethod
    def on_dscovery(self, context):
        pass
