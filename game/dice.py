from core.dice import Dice as Base_Dice
from .game_object import Game_Object
from .action import action


class Dice(Game_Object, Base_Dice):
    def __init__(self, name, outcomes):
        Game_Object.__init__(self, name=name)
        Base_Dice.__init__(self, outcomes)

    def get_name(self):
        return str(self)

    @action
    def on_roll(self, context):
        self.roll()
