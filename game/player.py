from core.internally_named import Internally_Named
from core.owning import Owner
from .hand import Hand
from .realm import Realm


class Player(Internally_Named, Owner):
    def __init__(self, name, color):
        Internally_Named.__init__(self, name)
        Owner.__init__(self)
        self._color = color
        self._hand = Hand(name="hand of " + name, owner=self)
        self._realm = Realm(name="realm of " + name, owner=self)

    def get_name(self):
        return str(self)

    def get_color(self):
        return self._color

    def change_color(self, color):
        self._color = color

    def get_hand(self):
        return self._hand

    def get_realm(self):
        return self._realm

    def get_mill_points(self, context):
        return self._realm.get_mill_points(context)

    def get_knight_points(self, context):
        return self._realm.get_knight_points(context)

    def get_win_points(self, context):
        return self._realm.get_win_points(context)
