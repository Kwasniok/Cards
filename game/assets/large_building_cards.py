from game.resource_types import *
from game.expansion_cards import register_expansion_card, Large_Building_Card


class Habour_Card(Large_Building_Card):
    def __init__(self):
        Large_Building_Card.__init__(self, "Habour")

    def get_cost(self, context):
        return [WOOL, IRON, BRICKS]

    def get_mill_points(self, context):
        return 1


register_expansion_card(Habour_Card, 1)
