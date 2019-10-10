from ..neutral_owner import neutral_owner
from ..piece import Piece, piece_library


class Mill_Piece(Piece):
    def __init__(self, owner=neutral_owner):
        Piece.__init__(self, name="mill", owner=owner)

    def get_win_points(self, context):
        return 1


piece_library.register(Mill_Piece, amount=1)


class Knight_Piece(Piece):
    def __init__(self, owner=neutral_owner):
        Piece.__init__(self, name="knight", owner=owner)

    def get_win_points(self, context):
        return 1


piece_library.register(Knight_Piece, amount=1)
