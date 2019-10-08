from .random import random_pick


class Dice:
    def __init__(self, outcomes):
        self._outcomes = outcomes
        self._last = None
        self.roll()

    def get_number_of_faces(self):
        return len(self._outcomes)

    def roll(self):
        self._last = random_pick(self._outcomes)
        return self._last

    def get_last_outcome(self):
        return self._last
