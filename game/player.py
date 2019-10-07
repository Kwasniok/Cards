from core.owning import Owner
from core.hand import Hand
from .realm import Realm


class Player(Owner):
    def __init__(self, name, color):
        Owner.__init__(self, name=name, color=color)
        self._hand = Hand(name="hand of " + name, owner=self)
        self._realm = Realm("realm of " + name, owner=self)

    def get_hand(self):
        return self._hand

    def get_realm(self):
        return self._realm
