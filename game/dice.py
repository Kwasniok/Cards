from core.dice import Dice as Base_Dice
from .game_object import Game_Object
from .action import action, Action_Invokation_Error


class Dice(Game_Object, Base_Dice):
    def __init__(self, name, outcomes):
        Game_Object.__init__(self, name=name)
        Base_Dice.__init__(self, outcomes)

    def get_name(self):
        return str(self)

    @action
    def on_roll(self, context):
        if not "dice roll phase" in context.active_phases:
            raise Action_Invokation_Error(
                "Cannot roll dice "
                + str(self)
                + ": active phase is not roll dice phase."
            )
        self.roll()
