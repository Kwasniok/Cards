import math
from core.owning import Owned
from core.slot import Slot


class Card_Slot(Owned, Slot):
    def __init__(self, name, owner, accepted_base_types, limit=math.inf):

        Owned.__init__(self, owner)
        Slot.__init__(
            self, accepted_base_types=accepted_base_types, limit=limit
        )
        self._name = name

    def __str__(self):
        return self._name

    def get_name(self):
        return self._name
