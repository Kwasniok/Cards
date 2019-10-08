from core.internally_named import Internally_Named
from core.owning import Owned


class Hand(Internally_Named, Owned):
    def __init__(self, name, owner, limit=3):
        Internally_Named.__init__(self, name)
        Owned.__init__(self, owner=owner)
        self._cards = []
        self._limit = limit

    def get_name(self):
        return str(name)

    def __getitem__(self, index):
        return self._cards[index]

    def __contains__(self, card):
        return card in self._cards

    def add(self, card):
        card.change_owner(self.get_owner())
        self._cards.append(card)

    def remove(self, card):
        if card in self._cards:
            self._cards.remove(card)
        else:
            raise (
                ValueError(
                    "Cannot remove card `"
                    + str(card)
                    + "` from hand `"
                    + str(self)
                    + "`"
                )
            )

    def is_above_limit(self):
        return len(self._cards) > self._limit

    def get_size(self):
        return len(self._cards)

    def get_limit(self):
        return self._limit
