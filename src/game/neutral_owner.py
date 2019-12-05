from core.owning import Owner
from core.internally_named import Internally_Named


class Neutral_Owner(Internally_Named, Owner):
    def __init__(self):
        Internally_Named.__init__(self, "neutral")
        Owner.__init__(self)


neutral_owner = Neutral_Owner()
