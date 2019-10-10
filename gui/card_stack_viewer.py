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
        display_face_indicator=True,
        display_text=True,
        display_cost=True,
        display_mill_points=True,
        display_knight_points=True,
        display_win_points=True,
    ):
        buttons = []
        x_card = x
        y_card = y
        for card in card_stack:
            button = Card_Viewer.create_button(
                context=context,
                window=window,
                card=card,
                x=x_card,
                y=y_card,
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
            x_card += int(width / 10)
            y_card += int(width / 10)
        return buttons
