from ..action import action, Action_Invokation_Error
from ..phase import Turn_Phase, turn_phase_library


class Begin_Turn_Phase(Turn_Phase):
    def __init__(self):
        Turn_Phase.__init__(
            self,
            name="begin turn phase",
            initially_active=True,
            required_previous_phases=["end turn phase"],
        )

    @action(Turn_Phase.on_activate_is_invokable)
    def on_activate(self, context):
        Turn_Phase.on_activate(self, context)
        context.game_state.switch_active_player()


turn_phase_library.register(Begin_Turn_Phase)


class Dice_Roll_Phase(Turn_Phase):
    def __init__(self):
        Turn_Phase.__init__(
            self,
            name="dice roll phase",
            required_previous_phases=["begin turn phase"],
        )


turn_phase_library.register(Dice_Roll_Phase)


class Event_Phase(Turn_Phase):
    def __init__(self):
        Turn_Phase.__init__(
            self,
            name="event phase",
            required_previous_phases=["dice roll phase"],
        )


turn_phase_library.register(Event_Phase)


class Resource_Increment_Phase(Turn_Phase):
    def __init__(self):
        Turn_Phase.__init__(
            self,
            name="resource increment phase",
            required_previous_phases=["event phase"],
        )


turn_phase_library.register(Resource_Increment_Phase)


class Main_Phase(Turn_Phase):
    def __init__(self):
        Turn_Phase.__init__(
            self,
            name="main phase",
            required_previous_phases=["resource increment phase"],
        )


turn_phase_library.register(Main_Phase)


class Discard_Phase(Turn_Phase):
    def __init__(self):
        Turn_Phase.__init__(
            self, name="discard phase", required_previous_phases=["main phase"]
        )


turn_phase_library.register(Discard_Phase)


class Draw_Phase(Turn_Phase):
    def __init__(self):
        Turn_Phase.__init__(
            self, name="draw phase", required_previous_phases=["discard phase"]
        )


turn_phase_library.register(Draw_Phase)


class End_Turn_Phase(Turn_Phase):
    def __init__(self):
        Turn_Phase.__init__(
            self, name="end turn phase", required_previous_phases=["draw phase"]
        )


turn_phase_library.register(End_Turn_Phase)
