from abc import abstractmethod
import core.card


class Card(core.card.Card):
    def __init__(self, name, face_up=False):
        core.card.Card.__init__(self, name, face_up)

    @abstractmethod
    def text(self, context):
        pass

    def cost(self, context):
        return []

    def mill_points(self, context):
        return 0

    def knight_points(self, context):
        return 0

    def win_points(self, context):
        return 0