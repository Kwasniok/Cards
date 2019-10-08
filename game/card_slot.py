import math
from core.owning import Owned
from core.internally_named import Internally_Named
from core.slot import Slot


class Card_Slot(Internally_Named, Owned, Slot):
    def __init__(self, name, owner, accepted_base_types, limit=math.inf):
        Internally_Named.__init__(self, name)
        Owned.__init__(self, owner)
        Slot.__init__(
            self, accepted_base_types=accepted_base_types, limit=limit
        )

    def get_name(self):
        return str(self)
