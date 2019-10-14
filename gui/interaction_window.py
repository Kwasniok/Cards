import tkinter as tk
from tkinter import messagebox
from core.destroy import safe_destroy
from core.gui.window import Window as Base_Window
from game.action import get_all_bound_action_methods

update_button_with = 150
update_button_height = 20
object_button_width = update_button_with
object_button_height = 50
action_button_width = update_button_with
action_button_height = 20


class Interaction_Window(Base_Window):
    def __init__(self, application):
        Base_Window.__init__(
            self,
            application=application,
            title="Interaction Window",
            width=10,
            height=10,
            x=0,
            y=0,
        )
        self.center()
        self.set_icon("res/game_icon.gif")
        self._stack = []
        self._stack_buttons = []
        # update button
        self._update_button = tk.Button(
            self.get_tk_toplevel(),
            text="update interaction tray",
            command=lambda: self.on_update(),
        )
        self._update_button.place(
            anchor=tk.NW,
            x=0,
            y=0,
            width=update_button_with,
            height=update_button_height,
        )
        self.on_update()

    def destroy(self):
        self._update_button = safe_destroy(self._update_button)
        self._destroy_stack_buttons()
        self._stack = []
        Base_Window.destroy(self)

    def on_close_requested(self):
        messagebox.showinfo(
            "Close Window", "Cannot close this window individually."
        )

    def _destroy_stack_buttons(self):
        for button in self._stack_buttons:
            button.destroy()
        self._stack_buttons = []

    def add_object(self, object):
        self._stack.append(object)
        self.on_update()

    def on_clear(self):
        self._stack = []

    def on_update(self):
        toplevel = self.get_tk_toplevel()
        toplevel.update_idletasks()
        width = object_button_width * max(1, len(self._stack))
        height = update_button_height + object_button_height
        actions = []
        if len(self._stack) > 0:
            actions = get_all_bound_action_methods(self._stack[0])
        height += len(actions) * action_button_height

        # resize
        self._toplevel.geometry(
            "%dx%d+%d+%d"
            % (width, height, toplevel.winfo_x(), toplevel.winfo_y())
        )

        # clear buttons
        self._destroy_stack_buttons()

        # create buttons
        x = 0
        y = update_button_height
        for i in range(len(self._stack)):
            object = self._stack[i]
            symbol = str(object)
            symbol += "\n" + str(object.get_owner())
            button = tk.Button(
                toplevel,
                text=symbol,
                command=lambda object=object: print(
                    "clicked on "
                    + repr(object)
                    + " in interaction tray (@ position "
                    + str(i)
                    + ")"
                ),
            )
            button.place(
                anchor=tk.NW,
                x=x,
                y=y,
                width=object_button_width,
                height=object_button_height,
            )
            self._stack_buttons.append(button)
            x += object_button_width
        x = 0
        y = update_button_height + object_button_height
        for action in actions:
            symbol = action.__qualname__
            button = tk.Button(
                toplevel,
                text=symbol,
                command=lambda action=action: print(
                    "clicked on action " + str(action) + " in interaction tray"
                ),
            )
            button.place(
                anchor=tk.NW,
                x=x,
                y=y,
                width=action_button_width,
                height=action_button_height,
            )
            self._stack_buttons.append(button)
            y += action_button_height
