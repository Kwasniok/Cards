import tkinter as tk
import tkinter.font as tkfont


class Card_Viewer:
    @staticmethod
    def create_button(
        context,
        window,
        card,
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
        card_symbol = card.get_title(context)
        if display_face_indicator:
            if card.is_face_up():
                card_symbol += " (FU)"
            else:
                card_symbol += " (FD)"
        if display_cost:
            cost = card.get_cost(context)
            if cost:
                card_symbol += (
                    "\n[" + (",".join([c.get_name() for c in cost])) + "]"
                )
        if display_mill_points:
            mp = card.get_mill_points(context)
            if mp:
                card_symbol += " " + str(mp) + "xM"
        if display_knight_points:
            kp = card.get_knight_points(context)
            if kp:
                card_symbol += " " + str(kp) + "xK"
        if display_win_points:
            wp = card.get_win_points(context)
            if wp:
                card_symbol += " " + str(wp) + "xW"
        if display_text:
            card_symbol += "\n" + card.get_text(context)
        button = tk.Button(
            window.get_tk_toplevel(),
            text=card_symbol,
            command=lambda card=card: window.get_interaction_window().add_object(
                card
            ),
        )
        button.place(anchor=tk.CENTER, x=x, y=y, width=width, height=height)
        return button
