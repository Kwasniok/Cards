class Subtype_Library:
    def __init__(self, base_class):
        self._base_class = base_class
        self._histogram = {}

    def register(self, card_class, amount=1):
        if not issubclass(card_class, self._base_class):
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
        self._histogram[card_class] = amount

    def get_all(self):
        objects = []
        for clss, count in self._histogram.items():
            for i in range(count):
                objects.append(clss())
        return objects
