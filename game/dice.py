from core.dice import Dice as Base_Dice


class Dice(Base_Dice):
    def __init__(self, name, outcomes):
        Base_Dice.__init__(self, outcomes)
        self._name = name

    def get_name(self):
        return name
