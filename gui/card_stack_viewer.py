import tkinter as tk
import tkinter.font as tkfont
from .card_viewer import Card_Viewer


class Card_Stack_Viewer:
    @staticmethod
    def create_buttons(
        context,
        window,
        card_stack,
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
        # card stack
        handle_width = width
        handle_height = int(height * 0.2)
        # symbol
        card_stack_symbol = card_stack.get_name()
        card_stack_symbol += " (" + str(len(card_stack)) + ")"
        # button
        button = tk.Button(
            window.get_tk_toplevel(),
            text=card_stack_symbol,
            command=lambda card_stack=card_stack: window.get_interaction_window().add_object(
                card_stack
            ),
        )
        button.place(
            anchor=tk.CENTER,
            x=x,
            y=y - (height + handle_height) / 2,
            width=handle_width,
            height=handle_height,
        )
        buttons.append(button)

        # crards in card stack
        card_x = x
        card_y = y
        for card in card_stack:
            button = Card_Viewer.create_button(
                context=context,
                window=window,
                card=card,
                x=card_x,
                y=card_y,
                width=width,
                height=height,
                display_face_indicator=True,
                display_text=True,
                display_cost=True,
                display_mill_points=True,
                display_knight_points=True,
                display_win_points=True,
            )
            buttons.append(button)
            card_x += shift_x
            card_y += shift_y
        return buttons
