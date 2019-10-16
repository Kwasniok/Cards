class Context:
    def __init__(
        self,
        game_state,
        active_player,
        opposing_player,
        active_phases,
        inactive_phases,
    ):
        self.game_state = game_state
        self.active_player = active_player
        self.opposing_player = opposing_player
        self.active_phases = active_phases
        self.inactive_phases = inactive_phases
