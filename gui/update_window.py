import tkinter as tk
from tkinter import messagebox
from core.destroy import safe_destroy
from core.owning import Owned
from core.gui.window import Window as Base_Window
from game.action import get_all_bound_action_methods

update_button_width = 100
update_button_height = 20


class Update_Window(Base_Window):
    def __init__(self, application, window, interaction_window, x, y):
        width = update_button_width
        height = update_button_height * 7
        Base_Window.__init__(
            self,
            application=application,
            title="Update Window (for debugging)",
            width=width,
            height=height,
            x=x,
            y=y,
        )
        self.set_icon("res/game_icon.gif")
        self.make_non_resizable()
        self._window = window
        self._interaction_window = interaction_window

        ## update buttons
        # interaction window
        self._update_interaction_window_button = tk.Button(
            self.get_tk_toplevel(),
            text="update interaction tray",
            command=lambda: self._interaction_window.on_update(),
        )
        self._update_interaction_window_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * 0,
            width=update_button_width,
            height=update_button_height,
        )
        # realms
        self._update_realms_button = tk.Button(
            self.get_tk_toplevel(),
            text="update realms",
            command=lambda: self._window.on_update_realms(None),
        )
        self._update_realms_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * 1,
            width=update_button_width,
            height=update_button_height,
        )
        # hands
        self._update_hands_button = tk.Button(
            self.get_tk_toplevel(),
            text="update hands",
            command=lambda: self._window.on_update_hands(None),
        )
        self._update_hands_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * 2,
            width=update_button_width,
            height=update_button_height,
        )
        # player
        self._update_player_status_button = tk.Button(
            self.get_tk_toplevel(),
            text="update players",
            command=lambda: self._window.on_update_player_status(None),
        )
        self._update_player_status_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * 3,
            width=update_button_width,
            height=update_button_height,
        )
        # dices
        self._update_dice_button = tk.Button(
            self.get_tk_toplevel(),
            text="update dices",
            command=lambda: self._window.on_update_dices(None),
        )
        self._update_dice_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * 4,
            width=update_button_width,
            height=update_button_height,
        )
        # card stacks
        self._update_card_stacks_button = tk.Button(
            self.get_tk_toplevel(),
            text="update card stacks",
            command=lambda: self._window.on_update_card_stacks(None),
        )
        self._update_card_stacks_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * 5,
            width=update_button_width,
            height=update_button_height,
        )
        # pieces
        self._update_pieces_button = tk.Button(
            self.get_tk_toplevel(),
            text="update piece trays",
            command=lambda: self._window.on_update_piece_trays(None),
        )
        self._update_pieces_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * 6,
            width=update_button_width,
            height=update_button_height,
        )

    def destroy(self):
        self._update_realms_button = safe_destroy(self._update_realms_button)
        self._update_hands_button = safe_destroy(self._update_hands_button)
        self._update_player_status_button = safe_destroy(
            self._update_player_status_button
        )
        self._update_dice_button = safe_destroy(self._update_dice_button)
        self._update_card_stacks_button = safe_destroy(
            self._update_card_stacks_button
        )
        self._update_pieces_button = safe_destroy(self._update_pieces_button)
        Base_Window.destroy(self)

    def on_close_requested(self):
        messagebox.showinfo(
            "Close Window", "Cannot close this window individually."
        )
