from abc import abstractmethod
from .game_object import Game_Object
from .subtype_library import Subtype_Library


class Piece(Game_Object):
    @abstractmethod
    def __init__(self, name):
        Game_Object.__init__(self, name=name)

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
