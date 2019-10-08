from abc import abstractmethod
from collections import Counter
from game.card import Card
from .resource_types import *


class Expansion_Card(Card):
    @abstractmethod
    def __init__(self, name):
        Card.__init__(self, name)

    @abstractmethod
    def is_playable(self, context):
        pass


class Action_Card(Expansion_Card):
    @abstractmethod
    def __init__(self, name):
        Expansion_Card.__init__(self, name)


class Building_Card(Expansion_Card):
    @abstractmethod
    def __init__(self, name):
        Expansion_Card.__init__(self, name)

    def is_playable(self, context):
        # TODO: on own turn
        return True

    def on_construction(self, context):
        return

    def on_destruction(self, context):
        return


class Small_Building_Card(Building_Card):
    @abstractmethod
    def __init__(self, name):
        Building_Card.__init__(self, name)


class Large_Building_Card(Building_Card):
    @abstractmethod
    def __init__(self, name):
        Building_Card.__init__(self, name)


expansion_card_histogram = {}


def register_expansion_card(card_class, amount):
    global expansion_card_histogram
    # print("expansion card registered: " + card_class.__name__)
    expansion_card_histogram[card_class] = amount


def get_all_expansion_cards():
    global expansion_card_histogram
    return list(Counter(expansion_card_histogram).elements())
