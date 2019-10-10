from game.resource_types import *
from game.expansion_cards import expansion_card_library, Small_Building_Card


class Monastery_Card(Small_Building_Card):
    def __init__(self):
        Small_Building_Card.__init__(self, "Monastery")

    def get_cost(self, context):
        return [LOGS, IRON, BRICKS]


expansion_card_library.register(Monastery_Card, amount=2)


class Storage_Card(Small_Building_Card):
    def __init__(self):
        Small_Building_Card.__init__(self, "Storage")

    def get_text(self, context):
        return "<-protected form robber->"

    def get_cost(self, context):
        return [LOGS, BRICKS]

    def get_mill_points(self, context):
        return 1


expansion_card_library.register(Storage_Card, amount=2)
