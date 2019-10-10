from ..neutral_owner import neutral_owner
from ..piece import Piece


class Mill_Piece(Piece):
    def __int__(self, owner=neutral_owner):
        Piece.__int__(self, "mill", owner)

    def get_mill_points(self, context):
        return 1
