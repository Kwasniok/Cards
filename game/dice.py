from core.dice import Dice as Base_Dice
from .game_object import Game_Object
from .action import action, Action_Invokation_Error


class Dice(Game_Object, Base_Dice):
    def __init__(self, name, outcomes):
        Game_Object.__init__(self, name=name)
        Base_Dice.__init__(self, outcomes)

    def get_name(self):
        return str(self)

    def on_roll_is_invokable(self, context):
        if not "dice roll phase" in context.active_phases:
            return False
        return True

    @action(on_roll_is_invokable)
    def on_roll(self, context):
        self.roll()
