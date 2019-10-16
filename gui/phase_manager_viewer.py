import tkinter as tk
import tkinter.font as tkfont
from core.destroy import safe_destroy
from .phase_viewer import Phase_Viewer


class Phase_Manager_Viewer:
    def __init__(self, window, phase_manager):
        self._window = window
        self._phase_manager = phase_manager
        self._buttons = []

    def destroy(self):
        self._destroy_buttons()

    def _destroy_buttons(self):
        for button in self._buttons:
            button.destroy()
        self._buttons = []

    def on_update(self, context):
        toplevel = self._window.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()

        # clear buttons
        self._destroy_buttons()

        # create buttons
        columns = len(self._phase_manager)
        phase_button_width = 80
        phase_button_height = 40
        # phases
        x_0 = phase_button_width / 2
        y_0 = phase_button_height / 2
        for i in range(columns):
            # phase
            phase = self._phase_manager[i]
            phase_x = x_0 + i * phase_button_width
            phase_y = y_0
            button = Phase_Viewer.create_button(
                context=context,
                window=self._window,
                phase=phase,
                x=phase_x,
                y=phase_y,
                width=phase_button_width,
                height=phase_button_height,
            )
            self._buttons.append(button)
