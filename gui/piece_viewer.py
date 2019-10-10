import tkinter as tk
import tkinter.font as tkfont


class Piece_Viewer:
    @staticmethod
    def create_button(context, window, piece, x, y, width, height):
        piece_symbol = piece.get_name(context)
        mp = piece.get_mill_points(context)
        if mp:
            piece_symbol += " " + str(mp) + "xM"
        kp = piece.get_knight_points(context)
        if kp:
            piece_symbol += " " + str(kp) + "xK"
        wp = piece.get_win_points(context)
        if wp:
            piece_symbol += " " + str(wp) + "xW"
        button = tk.Button(
            window.get_tk_toplevel(),
            text=piece_symbol,
            command=lambda piece=piece: print("clicked on " + repr(piece)),
        )
        button.place(anchor=tk.CENTER, x=x, y=y, width=width, height=height)
        return button
