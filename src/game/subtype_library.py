class Subtype_Library:
    def __init__(self, base_class):
        self._base_class = base_class
        self._register = []

    def register(self, clss, amount=1, initializer_dict=None):
        if not issubclass(clss, self._base_class):
            raise (
                ValueError(
                    "Cannot register card class "
                    + str(clss)
                    + " because it is not derived from the card base class "
                    + str(cars_base_class)
                    + "."
                )
            )
        # print(
        #     "registered: "
        #     + clss.__qualname__
        #     + " with initializer_dict="
        #     + str(initializer_dict)
        # )
        self._register.append((clss, amount, initializer_dict))

    def get_all(self):
        objects = []
        for (clss, amount, initializer_dict) in self._register:
            if initializer_dict is None:
                initializer_dict = {}
            for i in range(amount):
                objects.append(clss(**initializer_dict))
        return objects
