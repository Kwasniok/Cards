import tkinter as tk
import tkinter.font as tkfont
from .card_viewer import Card_Viewer


class Slot_Viewer:
    @staticmethod
    def create_buttons(
        context,
        window,
        slot,
        x,
        y,
        width,
        height,
        shift_x,
        shift_y,
        display_face_indicator=True,
        display_text=True,
        display_cost=True,
        display_mill_points=True,
        display_knight_points=True,
        display_win_points=True,
    ):
        buttons = []
        # slot
        slot_symbol = slot.get_name()
        slot_symbol += " (" + str(len(slot)) + "/" + str(slot.get_limit()) + ")"
        slot_symbol += "\n"
        slot_symbol += "|".join(
            pct.__name__ for pct in slot.get_accepted_base_types()
        )
        # slot button
        button = tk.Button(
            window.get_tk_toplevel(),
            text=slot_symbol,
            command=lambda slot=slot: window.get_interaction_window().add_object(
                slot
            ),
        )
        button.place(anchor=tk.CENTER, x=x, y=y, width=width, height=height)
        buttons.append(button)
        # cards in slot
        card_x = x
        card_y = y
        for card in slot:
            card_width = int(width * 0.9)
            card_height = int(height * 0.5)
            buttons.append(
                Card_Viewer.create_button(
                    context,
                    window=window,
                    card=card,
                    x=card_x,
                    y=card_y,
                    width=card_width,
                    height=card_height,
                    display_face_indicator=display_face_indicator,
                    display_text=display_text,
                    display_cost=display_cost,
                    display_mill_points=display_mill_points,
                    display_knight_points=display_knight_points,
                    display_win_points=display_win_points,
                )
            )
            card_x += shift_x
            card_y += shift_y
        return buttons
