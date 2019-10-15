class Context:
    def __init__(
        self, game_state, current_phase, active_player, opposing_player
    ):
        self.game_state = game_state
        self.current_phase = current_phase
        self.active_player = active_player
        self.opposing_player = opposing_player
