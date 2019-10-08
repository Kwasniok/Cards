from core.owning import Owned


class Card_Stack(Owned):
    def __init__(self, name, cards=None):
        self._name = name
        if cards is None:
            self._cards = []
        else:
            self._cards = cards

    def __str__(self):
        return self._name

    def __len__(self):
        return len(self._cards)

    def __contains__(self, card):
        return card in self._cards

    def __iter__(self):
        return iter(self._cards)

    def can_pop_top(self):
        return len(self._cards) > 0

    def get_top(self):
        return self._cards[-1]

    def pop_top(self):
        card = self._cards[-1]
        self._cards.remove(card)
        return card

    def push_top(self, card):
        if card in self._cards:
            raise (
                ValueError(
                    "Cannot push card `"
                    + str(card)
                    + "` on top of card stack `"
                    + str(self)
                    + "` because it is allready in this stack."
                )
            )
        else:
            self._cards.append(card)

    def push_bottom(self, card):
        if card in self._cards:
            raise (
                ValueError(
                    "Cannot push card `"
                    + str(card)
                    + "` on botttom of card stack `"
                    + str(self)
                    + "` because it is allready in this stack."
                )
            )
        else:
            self._cards.insert(0, card)

    def remove(self, card):
        if card in self._cards:
            self._cards.remove(card)
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
