from core.owning import Owned


class Card_Slot(Owned):
    def __init__(self, name, owner, possible_card_types, limit=None):
        Owned.__init__(self, owner)
        self._name = name
        self._owner = owner
        self._possible_card_types = possible_card_types
        self._limit = limit
        self._cards = []

    def __str__(self):
        return self._name

    def __repr__(self):
        return (
            "Card_Slot(name='"
            + self._name
            + "', owner="
            + str(self._owner)
            + ", possible_card_types="
            + str(self._possible_card_types)
            + ", limit="
            + str(self._limit)
            + ", cards=["
            + (", ".join(repr(c) for c in self._cards))
            + "])"
        )

    def __contains__(self, card):
        return card in self._cards

    def get_name(self):
        return self._name

    def get_limit(self):
        return self._limit

    def is_empty(self):
        return len(self._cards) == 0

    def is_full(self):
        return len(self._cards) >= self._limit

    def accepts_card(self, card):
        if card in self._cards:
            return False
        if len(self._cards) >= self._limit:
            return False
        return isinstance(card, tuple(self._possible_card_types))

    def accepts_card_of_type(self, type):
        return issubclass(type, tuple(self._possible_card_types))

    def possible_card_types(self):
        return self._possible_card_types

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
        if not self.accepts_card(card):
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
        self._cards.append(card)

    def remove(self, card):
        self._cards.remove(card)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __iter__(self):
        return iter(self._cards)

    def get_top(self):
        return self._cards[-1]