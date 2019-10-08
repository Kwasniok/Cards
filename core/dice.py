from .random import random_pick


class Dice:
    def __init__(self, outcomes):
        self._outcomes = outcomes
        self._last = None

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
