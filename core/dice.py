from .util import random_pick
from .owning import Owned


class Dice(Owned):
    def __init__(self, name, outcomes):
        self.name = name
        self.coutcomes = outcomes
        self.last_outcome = None

    def __str__(self):
        return self.name

    def number_of_faces(self):
        return len(self.outcomes)

    def roll(self):
        self.last_outcome = random_pick(self.outcomes)
        return self.last_outcome

    def last_outcome(self):
        if self.last_outcome is None:
            raise (
                RuntimeError(
                    "Dice `"
                    + str(self)
                    + "` has no last outcome because it was never rolled."
                )
            )
        else:
            return self.last_outcome
