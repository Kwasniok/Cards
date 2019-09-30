from .owning import Owned


class Card_Slot(Owned):
    def __init__(self, name, owner, possible_card_types, limit=None):
        self._name = name
        self._owner = owner
        self._possible_card_types = possible_card_types
        self._limit = limit
        self._cards = set()

    def __str__(self):
        return self._name

    def __contains__(self, card):
        return card in self._cards

    def is_empty(self):
        return len(self._cards) == 0

    def is_full(self):
        return len(self._cards) >= self._limit

    def supports(self, card):
        return isinstance(card, tuple(self._possible_card_types))

    def add(self, card):
        if self.is_full():
            raise ValueError(
                "Cannot add card `"
                + str(card)
                + "` of type `"
                + str(type(card))
                + "` to card slot `"
                + str(self)
                + "` (reached limit of "
                + str(self._limit)
                + ")."
            )
        if not self.supports(card):
            raise ValueError(
                "Cannot add card `"
                + str(card)
                + "` of type `"
                + str(type(card))
                + "` to card slot `"
                + str(self)
                + "` (must be one of "
                + ", ".join(
                    "`" + str(t) + "`" for t in self._possible_card_types
                )
                + ")."
            )
        if card in self:
            raise ValueError(
                "Cannot add card `"
                + str(card)
                + "` of type `"
                + str(type(card))
                + "` to card slot `"
                + str(self)
                + "` (card allready is in this stack)."
            )
        self._cards.add(card)

    def remove(self, card):
        self._cards.remove(card)

    def get_cards(self):
        return self._cards
