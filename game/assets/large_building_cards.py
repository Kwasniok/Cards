from game.resource_types import *
from game.expansion_cards import expansion_card_library, Large_Building_Card


class Habour_Card(Large_Building_Card):
    def __init__(self):
        Large_Building_Card.__init__(self, "Habour")

    def get_cost(self, context):
        return [WOOL, IRON, BRICKS]

    def get_mill_points(self, context):
        return 1


expansion_card_library.register(Habour_Card, amount=1)
