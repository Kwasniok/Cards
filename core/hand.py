from .owning import Owned


class Hand(Owned):
    def __init__(self, name, owner, limit=3):
        self.owner(owner)
        self._name = name
        self._cards = []

    def __str__(self):
        return self._name

    def add_card(self, card):
        self._cards.append(card)

    def remove_card(self, card):
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
