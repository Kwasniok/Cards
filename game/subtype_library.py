class Subtype_Library:
    def __init__(self, card_base_class):
        self._card_base_class = card_base_class
        self._card_histogram = {}

    def register(self, card_class, amount):
        if not issubclass(card_class, self._card_base_class):
            raise (
                ValueError(
                    "Cannot register card class "
                    + str(card_class)
                    + " because it is not derived from the card base class "
                    + str(cars_base_class)
                    + "."
                )
            )
        # print("event card registered: " + card_class.__name__)
        self._card_histogram[card_class] = amount

    def get_all(self):
        all_event_cards = []
        for card_type, count in self._card_histogram.items():
            for i in range(count):
                all_event_cards.append(card_type())
        return all_event_cards
