from core.internally_named import Internally_Named
from core.dice import Dice as Base_Dice


class Dice(Internally_Named, Base_Dice):
    def __init__(self, name, outcomes):
        Internally_Named.__init__(self, name)
        Base_Dice.__init__(self, outcomes)

    def get_name(self):
        return str(self)
