from ..action import action, Action_Invokation_Error
from ..phase import Phase, phase_library


class Begin_Turn_Phase(Phase):
    def __init__(self):
        Phase.__init__(
            self,
            name="begin turn phase",
            initially_active=True,
            required_previous_phases=["end turn phase"],
        )

    @action
    def on_activate(self, context):
        Phase.on_activate(self, context)
        context.game_state.switch_active_player()


phase_library.register(Begin_Turn_Phase)


class Dice_Roll_Phase(Phase):
    def __init__(self):
        Phase.__init__(
            self,
            name="dice roll phase",
            required_previous_phases=["begin turn phase"],
        )


phase_library.register(Dice_Roll_Phase)


class Event_Phase(Phase):
    def __init__(self):
        Phase.__init__(
            self,
            name="event phase",
            required_previous_phases=["dice roll phase"],
        )


phase_library.register(Event_Phase)


class Resource_Increment_Phase(Phase):
    def __init__(self):
        Phase.__init__(
            self,
            name="resource increment phase",
            required_previous_phases=["event phase"],
        )


phase_library.register(Resource_Increment_Phase)


class Main_Phase(Phase):
    def __init__(self):
        Phase.__init__(
            self,
            name="main phase",
            required_previous_phases=["resource increment phase"],
        )


phase_library.register(Main_Phase)


class Discard_Phase(Phase):
    def __init__(self):
        Phase.__init__(
            self, name="discard phase", required_previous_phases=["main phase"]
        )


phase_library.register(Discard_Phase)


class Draw_Phase(Phase):
    def __init__(self):
        Phase.__init__(
            self, name="draw phase", required_previous_phases=["discard phase"]
        )


phase_library.register(Draw_Phase)


class End_Turn_Phase(Phase):
    def __init__(self):
        Phase.__init__(
            self, name="end turn phase", required_previous_phases=["draw phase"]
        )


phase_library.register(End_Turn_Phase)
