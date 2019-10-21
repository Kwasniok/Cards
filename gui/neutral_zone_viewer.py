import tkinter as tk
import tkinter.font as tkfont
from core.destroy import safe_destroy
import game.directions as directions
from .dice_viewer import Dice_Viewer
from .card_stack_viewer import Card_Stack_Viewer
from .piece_tray_viewer import Piece_Tray_Viewer


class Neutral_Zone_Viewer:
    def __init__(self, window, neutral_zone):
        self._window = window
        self._neutral_zone = neutral_zone
        # dices
        self._dice_viewer_number = Dice_Viewer(
            window=self._window,
            dice=self._window.get_application()
            .get_game_state()
            .get_neutral_zone()
            .get_number_dice(),
            direction=directions.UP,
        )
        self._dice_viewer_event = Dice_Viewer(
            window=self._window,
            dice=self._window.get_application()
            .get_game_state()
            .get_neutral_zone()
            .get_event_dice(),
            direction=directions.DOWN,
        )
        # expansion card stacks
        self._expansion_card_stack_buttons = []
        # structure card stacks
        self._structure_card_stack_buttons = []
        # structure card stacks
        self._resource_card_stack_buttons = []
        # event card stacks
        self._event_card_intake_stack_buttons = []
        self._event_card_tray_stack_buttons = []
        # pieces
        self._piece_tray_buttons = []

    def destroy(self):
        self._dice_viewer_number = safe_destroy(self._dice_viewer_number)
        self._dice_viewer_event = safe_destroy(self._dice_viewer_event)
        self._destroy_expansion_card_stack_buttons()
        self._destroy_structure_card_stack_buttons()
        self._destroy_structure_card_stack_buttons()
        self._destroy_event_card_stack_buttons()
        self._destroy_piece_tray_buttons()

    def _destroy_expansion_card_stack_buttons(self):
        for button_stack in self._expansion_card_stack_buttons:
            for button in button_stack:
                button.destroy()
        self._expansion_card_stack_buttons = []

    def _destroy_resource_card_stack_buttons(self):
        for button in self._resource_card_stack_buttons:
            button.destroy()
        self._resource_card_stack_buttons = []

    def _destroy_structure_card_stack_buttons(self):
        for button_stack in self._structure_card_stack_buttons:
            for button in button_stack:
                button.destroy()
        self._structure_card_stack_buttons = []

    def _destroy_event_card_stack_buttons(self):
        for button in self._event_card_intake_stack_buttons:
            button.destroy()
        self._event_card_intake_stack = []
        for button in self._event_card_tray_stack_buttons:
            button.destroy()
        self._event_card_tray_stack = []

    def _destroy_piece_tray_buttons(self):
        for button in self._piece_tray_buttons:
            button.destroy()
        self._piece_tray_buttons = []

    def on_update_all_dice_viewers(self, context):
        self._dice_viewer_number.on_update(context)
        self._dice_viewer_event.on_update(context)

    def on_update_expansion_card_stack_viewers(self, context):
        toplevel = self._window.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()

        # clear buttons
        self._destroy_expansion_card_stack_buttons()

        # create buttons
        button_width = 150
        button_height = 80
        x_card_stack = button_width / 2
        y_card_stack = height / 2
        for card_stack in self._neutral_zone.get_expansion_card_stacks():
            card_stack_buttons = Card_Stack_Viewer.create_buttons(
                context=context,
                window=self._window,
                card_stack=card_stack,
                x=x_card_stack,
                y=y_card_stack,
                width=button_width,
                height=button_height,
                shift_x=0,
                shift_y=int(button_width * 0.02),
            )
            x_card_stack += button_width

    def on_update_resource_card_stack_viewer(self, context):
        toplevel = self._window.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()

        # clear buttons
        self._destroy_resource_card_stack_buttons()

        # create buttons
        button_width = 150
        button_height = 80
        x_card_stack = button_width / 2 + button_width * 5
        y_card_stack = height / 2
        card_stack_buttons = Card_Stack_Viewer.create_buttons(
            context=context,
            window=self._window,
            card_stack=self._neutral_zone.get_resource_card_stack(),
            x=x_card_stack,
            y=y_card_stack,
            width=button_width,
            height=button_height,
            shift_x=0,
            shift_y=int(button_width * 0.02),
        )

    def on_update_structure_card_stack_viewers(self, context):
        toplevel = self._window.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()

        # clear buttons
        self._destroy_structure_card_stack_buttons()

        # create buttons
        button_width = 150
        button_height = 80
        x_card_stack = width / 2 + button_width
        y_card_stack = height / 2
        card_stack_buttons = Card_Stack_Viewer.create_buttons(
            context=context,
            window=self._window,
            card_stack=self._neutral_zone.get_road_card_stack(),
            x=x_card_stack,
            y=y_card_stack,
            width=button_width,
            height=button_height,
            shift_x=0,
            shift_y=int(button_width * 0.02),
        )
        self._structure_card_stack_buttons.append(card_stack_buttons)
        x_card_stack += button_width
        card_stack_buttons = Card_Stack_Viewer.create_buttons(
            context=context,
            window=self._window,
            card_stack=self._neutral_zone.get_settlement_card_stack(),
            x=x_card_stack,
            y=y_card_stack,
            width=button_width,
            height=button_height,
            shift_x=0,
            shift_y=int(button_width * 0.02),
        )
        self._structure_card_stack_buttons.append(card_stack_buttons)
        x_card_stack += button_width
        card_stack_buttons = Card_Stack_Viewer.create_buttons(
            context=context,
            window=self._window,
            card_stack=self._neutral_zone.get_town_card_stack(),
            x=x_card_stack,
            y=y_card_stack,
            width=button_width,
            height=button_height,
            shift_x=0,
            shift_y=int(button_width * 0.02),
        )
        self._structure_card_stack_buttons.append(card_stack_buttons)
        x_card_stack += button_width

    def on_update_event_card_stack_viewers(self, context):
        toplevel = self._window.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()

        # clear buttons
        self._destroy_event_card_stack_buttons()

        # create buttons
        button_width = 150
        button_height = 80
        x_card_stack = width / 2 + 4 * button_width
        y_card_stack = height / 2
        card_stack_buttons = Card_Stack_Viewer.create_buttons(
            context=context,
            window=self._window,
            card_stack=self._neutral_zone.get_event_card_intake_stack(),
            x=x_card_stack,
            y=y_card_stack,
            width=button_width,
            height=button_height,
            shift_x=0,
            shift_y=int(button_width * 0.02),
        )
        self._structure_card_stack_buttons.append(card_stack_buttons)
        x_card_stack += button_width
        card_stack_buttons = Card_Stack_Viewer.create_buttons(
            context=context,
            window=self._window,
            card_stack=self._neutral_zone.get_event_card_tray_stack(),
            x=x_card_stack,
            y=y_card_stack,
            width=button_width,
            height=button_height,
            shift_x=0,
            shift_y=int(button_width * 0.02),
        )

    def on_update_piece_tray_viewer(self, context):
        toplevel = self._window.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()

        # clear buttons
        self._destroy_piece_tray_buttons()

        # create buttons
        button_width = 80
        button_height = 40
        x = width / 2
        y = (height - button_height) / 2
        self._piece_tray_buttons = Piece_Tray_Viewer.create_buttons(
            context=context,
            window=self._window,
            piece_tray=self._neutral_zone.get_piece_tray(),
            x=x,
            y=y,
            width=button_width,
            height=button_height,
        )
