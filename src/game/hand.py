from .game_object import Game_Object


class Hand(Game_Object):
    def __init__(self, name, owner, limit=3):
        Game_Object.__init__(self, name, owner=owner)
        self._cards = []
        self._limit = limit

    def get_name(self):
        return self._get_internal_name()

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

    def is_empty(self):
        return len(self._cards) == 0

    def is_full(self):
        return len(self._cards) == self._limit
