import tkinter as tk
from tkinter import messagebox
from core.destroy import safe_destroy
from core.owning import Owned
from core.gui.window import Window as Base_Window
from game.action import get_all_bound_action_methods

update_button_width = 200
update_button_height = 20


class Update_Window(Base_Window):
    def __init__(self, application, window, interaction_window, x, y):
        width = update_button_width
        height = update_button_height
        Base_Window.__init__(
            self,
            application=application,
            title="Update Window (for debugging)",
            width=width,
            height=height,
            x=x,
            y=y,
        )
        self.set_icon("../res/game_icon.gif")
        self.make_non_resizable()
        self._window = window
        self._interaction_window = interaction_window

        ## update buttons
        # interaction window
        i = 0
        self._update_interaction_window_button = tk.Button(
            self.get_tk_toplevel(),
            text="update interaction tray",
            command=lambda: self._interaction_window.update(),
        )
        self._update_interaction_window_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * i,
            width=update_button_width,
            height=update_button_height,
        )
        i += 1
        # all
        self._update_all_button = tk.Button(
            self.get_tk_toplevel(),
            text="update main window",
            command=lambda: self._window.update_all_viewers(),
        )
        self._update_all_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * i,
            width=update_button_width,
            height=update_button_height,
        )
        i += 1
        # realms
        self._update_realms_button = tk.Button(
            self.get_tk_toplevel(),
            text="update realms",
            command=lambda: self._window.update_all_realm_viewers(),
        )
        self._update_realms_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * i,
            width=update_button_width,
            height=update_button_height,
        )
        i += 1
        # hands
        self._update_hands_button = tk.Button(
            self.get_tk_toplevel(),
            text="update hands",
            command=lambda: self._window.update_all_hand_viewers(),
        )
        self._update_hands_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * i,
            width=update_button_width,
            height=update_button_height,
        )
        i += 1
        # player
        self._update_player_status_button = tk.Button(
            self.get_tk_toplevel(),
            text="update players",
            command=lambda: self._window.update_all_player_status_viewers(),
        )
        self._update_player_status_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * i,
            width=update_button_width,
            height=update_button_height,
        )
        i += 1
        # dices
        self._update_dice_button = tk.Button(
            self.get_tk_toplevel(),
            text="update dices",
            command=lambda: self._window.update_all_dice_viewers(),
        )
        self._update_dice_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * i,
            width=update_button_width,
            height=update_button_height,
        )
        i += 1
        # card stacks
        self._update_card_stacks_button = tk.Button(
            self.get_tk_toplevel(),
            text="update card stacks",
            command=lambda: self._window.update_all_card_stack_viewers(),
        )
        self._update_card_stacks_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * i,
            width=update_button_width,
            height=update_button_height,
        )
        i += 1
        # pieces
        self._update_pieces_button = tk.Button(
            self.get_tk_toplevel(),
            text="update piece trays",
            command=lambda: self._window.update_all_piece_tray_viewers(),
        )
        self._update_pieces_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * i,
            width=update_button_width,
            height=update_button_height,
        )
        i += 1
        # phase manager
        self._update_phase_manager_button = tk.Button(
            self.get_tk_toplevel(),
            text="update phase manager",
            command=lambda: self._window.update_phase_manager_viewer(),
        )
        self._update_phase_manager_button.place(
            anchor=tk.NW,
            x=0,
            y=update_button_height * i,
            width=update_button_width,
            height=update_button_height,
        )
        i += 1
        # resize window
        toplevel = self.get_tk_toplevel()
        toplevel.update_idletasks()
        toplevel.geometry(
            "%dx%d+%d+%d"
            % (
                update_button_width,
                update_button_height * i,
                toplevel.winfo_x(),
                toplevel.winfo_y(),
            )
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
        self._update_phase_manager_button = safe_destroy(
            self._update_phase_manager_button
        )
        Base_Window.destroy(self)

    def on_close_requested(self):
        messagebox.showinfo(
            "Close Window", "Cannot close this window individually."
        )
