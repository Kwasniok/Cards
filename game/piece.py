from core.internally_named import Internally_Named
from core.owning import Owned
from .neutral_owner import neutral_owner


class Piece(Internally_Named, Owned):
    def __init__(self, name):
        Internally_Named.__init__(self, name=name)
        Owned.__init__(self, owner=neutral_owner)
