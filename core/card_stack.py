from .owning import Owned


class Card_Stack(Owned):
    def __init__(self, name, cards=None):
        self.name = name
        if cards is None:
            self._cards = []
        else:
            self.cards = cards

    def __str__(self):
        return self.name

    def can_pick_top(self):
        return len(self.cards) > 0

    def pick_top(self):
        card = self.cards[-1]
        self.cards.remove(card)
        return card

    def get_cards(self):
        return self.cards

    def pick_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
        else:
            raise (
                ValueError(
                    "Cannot pick card `"
                    + str(card)
                    + "` from card stack `"
                    + str(self)
                    + "` because it not in this stack."
                )
            )
