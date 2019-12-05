import tkinter as tk
import tkinter.font as tkfont


class Phase_Viewer:
    @staticmethod
    def create_button(context, window, phase, x, y, width, height):
        phase_symbol = phase.get_name(context)
        if phase.is_active():
            phase_symbol += "\n (active)"
        button = tk.Button(
            window.get_tk_toplevel(),
            text=phase_symbol,
            command=lambda phase=phase: window.get_interaction_window().add_object(
                phase
            ),
        )
        button.place(anchor=tk.CENTER, x=x, y=y, width=width, height=height)
        return button
