from .owning import Owned


class Hand(Owned):
    def __init__(self, name, owner, limit=3):
        self.name = name
        self.owner(owner)
        self.cards = []

    def __str__(self):
        return self.name

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
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
