from .util import random_pick
from .owning import Owned


class Dice(Owned):
    def __init__(self, name, outcomes):
        self._name = name
        self._outcomes = outcomes
        self._last = None

    def __str__(self):
        return self._name

    def number_of_faces(self):
        return len(self._outcomes)

    def roll(self):
        self._last = random_pick(self._outcomes)
        return self._last

    def last_outcome(self):
        if self._last is None:
            raise (
                RuntimeError(
                    "Dice `"
                    + str(self)
                    + "` has no last outcome because it was never rolled."
                )
            )
        else:
            return self._last
