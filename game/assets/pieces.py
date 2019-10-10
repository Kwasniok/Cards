from ..neutral_owner import neutral_owner
from ..piece import Piece


class Mill_Piece(Piece):
    def __init__(self, owner=neutral_owner):
        Piece.__init__(self, name="mill", owner=owner)

    def get_win_points(self, context):
        return 1
