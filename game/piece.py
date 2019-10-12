from abc import abstractmethod
from core.internally_named import Internally_Named
from core.owning import Owned
from .neutral_owner import neutral_owner
from .subtype_library import Subtype_Library


class Piece(Internally_Named, Owned):
    @abstractmethod
    def __init__(self, name, owner=neutral_owner):
        Internally_Named.__init__(self, name=name)
        Owned.__init__(self, owner=owner)

    def __repr__(self):
        return (
            'Piece(name="'
            + str(self)
            + '", owner='
            + str(self.get_owner())
            + ")"
        )

    def get_name(self, context):
        return self._get_internal_name()

    def get_mill_points(self, context):
        return 0

    def get_knight_points(self, context):
        return 0

    def get_win_points(self, context):
        return 0


piece_library = Subtype_Library(Piece)
