import tkinter as tk
import tkinter.font as tkfont
from .piece_viewer import Piece_Viewer


class Piece_Tray_Viewer:
    @staticmethod
    def create_buttons(context, window, piece_tray, x, y, width, height):
        buttons = []
        x_piece = x
        y_piece = y
        for piece in piece_tray:
            button = Piece_Viewer.create_button(
                context=context,
                window=window,
                piece=piece,
                x=x_piece,
                y=y_piece,
                width=width,
                height=height,
            )
            buttons.append(button)
            y_piece += height
        return buttons
