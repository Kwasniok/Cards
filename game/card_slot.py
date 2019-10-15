import math
from core.slot import Slot
from .game_object import Game_Object


class Card_Slot(Game_Object, Slot):
    def __init__(self, name, owner, accepted_base_types, limit=math.inf):
        Game_Object.__init__(self, name=name, owner=owner)
        Slot.__init__(
            self, accepted_base_types=accepted_base_types, limit=limit
        )

    def get_name(self):
        return str(self)
