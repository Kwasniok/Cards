from ..piece import Piece, piece_library


class Mill_Piece(Piece):
    def __init__(self):
        Piece.__init__(self, name="mill")

    def get_win_points(self, context):
        return 1


piece_library.register(Mill_Piece, amount=1)


class Knight_Piece(Piece):
    def __init__(self):
        Piece.__init__(self, name="knight")

    def get_win_points(self, context):
        return 1


piece_library.register(Knight_Piece, amount=1)
