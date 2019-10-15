from core.internally_named import Internally_Named
from core.owning import Owned
from core.dice import Dice as Base_Dice
from .neutral_owner import neutral_owner
from .action import action


class Dice(Internally_Named, Owned, Base_Dice):
    def __init__(self, name, outcomes):
        Internally_Named.__init__(self, name)
        Owned.__init__(self, neutral_owner)
        Base_Dice.__init__(self, outcomes)

    def get_name(self):
        return str(self)

    @action
    def on_roll(self, context):
        self.roll()
