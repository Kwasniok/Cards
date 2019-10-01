from abc import abstractmethod
from core.card import Card


class Expansion_Card(Card):
    def __init__(self, name):
        Card.__init__(self, name)

    @abstractmethod
    def playable(self, context):
        pass


class Action_Card(Expansion_Card):
    def __init__(self, name):
        Expansion_Card.__init__(self, name)


class Building_Card(Expansion_Card):
    def __init__(self, name):
        Expansion_Card.__init__(self, name)

    def mill_points(self, context):
        return 0

    def knight_points(self, context):
        return 0

    def win_points(self, context):
        return 0

    def on_construction(self, context):
        return

    def on_destruction(self, context):
        return


class Small_Building_Card(Expansion_Card):
    def __init__(self, name):
        Building_Card.__init__(self, name)


class Large_Building_Card(Expansion_Card):
    def __init__(self, name):
        Building_Card.__init__(self, name)
