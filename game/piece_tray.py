from core.internally_named import Internally_Named
from core.owning import Owned
from .neutral_owner import neutral_owner


class Piece_Tray(Internally_Named, Owned):
    def __init__(self, name, owner=neutral_owner):
        Internally_Named.__init__(self, name)
        Owned.__init__(self, owner)
        self._pieces = []

    def __len__(self):
        return len(self._pieces)

    def __contains__(self, piece):
        return piece in self._pieces

    def __iter__(self):
        return iter(self._pieces)

    def add(self, piece):
        if piece in self._pieces:
            raise (
                ValueError(
                    "Cannot add piece `"
                    + str(piece)
                    + "` card tray `"
                    + str(self)
                    + "` because it is allready in this piece tray."
                )
            )
        else:
            self._pieces.append(piece)

    def remove(self, piece):
        if piece in self._pieces:
            self._pieces.remove(piece)

    def get_mill_points(self, context):
        return sum([piece.get_mill_points(context) for piece in self._pieces])

    def get_knight_points(self, context):
        return sum([piece.get_knight_points(context) for piece in self._pieces])

    def get_win_points(self, context):
        return sum([piece.get_win_points(context) for piece in self._pieces])
