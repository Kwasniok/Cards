from game.resource_types import *
from game.expansion_cards import register_expansion_card, Small_Building_Card


class Monastery_Card(Small_Building_Card):
    def __init__(self):
        Small_Building_Card.__init__(self, "Monastery")

    def get_text(self, context):
        return "<-protected form robber->"

    def get_cost(self, context):
        return [LOGS, IRON, BRICKS]


register_expansion_card(Monastery_Card, 2)


class Storage_Card(Small_Building_Card):
    def __init__(self):
        Small_Building_Card.__init__(self, "Storage")

    def get_cost(self, context):
        return [LOGS, BRICKS]

    def get_mill_points(self, context):
        return 1


register_expansion_card(Storage_Card, 2)
