import tkinter as tk
import tkinter.font as tkfont
from core.destroy import safe_destroy
import game.directions as directions
from .dice_viewer import Dice_Viewer
from .card_stack_viewer import Card_Stack_Viewer


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
            direction=directions.LEFT,
        )
        self._dice_viewer_event = Dice_Viewer(
            window=self._window,
            dice=self._window.get_application()
            .get_game_state()
            .get_neutral_zone()
            .get_event_dice(),
            direction=directions.RIGHT,
        )
        # expansion card stacks
        self._expansion_card_stack_buttons = []
        # structure card stacks
        self._structure_card_stack_buttons = []

    def destroy(self):
        safe_destroy(self._dice_viewer_number)
        safe_destroy(self._dice_viewer_event)
        self._destroy_expansion_card_stack_buttons()
        self._destroy_structure_card_stack_buttons()

    def _destroy_expansion_card_stack_buttons(self):
        for button_stack in self._expansion_card_stack_buttons:
            for button in button_stack:
                button.destroy()
        self._expansion_card_stack_buttons = []

    def _destroy_structure_card_stack_buttons(self):
        for button_stack in self._structure_card_stack_buttons:
            for button in button_stack:
                button.destroy()
        self._structure_card_stack_buttons = []

    def on_update_dices(self, context):
        self._dice_viewer_number.on_update(context)
        self._dice_viewer_event.on_update(context)

    def on_update_expansion_card_stacks(self, context):
        toplevel = self._window.get_tk_toplevel()
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()

        # clear buttons
        self._destroy_expansion_card_stack_buttons()

        # create buttons
        button_width = 180
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
            )
            x_card_stack += button_width

    def on_update_structure_card_stacks(self, context):
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
        )
        self._structure_card_stack_buttons.append(card_stack_buttons)
        x_card_stack += button_width
