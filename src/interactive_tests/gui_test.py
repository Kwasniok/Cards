import tkinter as tk
from core.gui.application import Application
from core.gui.window import Window


class Test_Window(Window):
    def __init__(self, application, x, y):
        width = 512
        height = 512
        Window.__init__(
            self,
            application=application,
            title="A Test Window",
            width=width,
            height=height,
            x=x,
            y=y,
        )
        self.make_non_resizable()
        self.center()
        self.set_icon("../res/test.gif")
        self._counter = 0
        self._canvas = tk.Canvas(self.get_tk_toplevel())
        self._canvas.pack(expand=True, fill=tk.BOTH)  # fill parent
        self._arc_id = self._canvas.create_arc(
            2,
            2,
            width - 2,
            height - 2,
            start=0,
            extent=120,
            fill="#0000FF",
            outline="#FFFFFF",
        )
        self._image = tk.PhotoImage(file="../res/test.gif")
        self._image_id = self._canvas.create_image(
            128, 128, anchor=tk.NW, image=self._image
        )
        self._text_id = self._canvas.create_text(
            146, 146, anchor=tk.CENTER, text=""
        )

    def destroy(self):
        self._image = None
        if not (self._canvas is None):
            self._canvas.destroy()
        self._canvas = None
        Window.destroy(self)

    def on_next_frame(self):
        self._counter += 1
        self._canvas.itemconfig(self._arc_id, start=self._counter)
        self._canvas.itemconfig(self._text_id, text=str(self._counter))


def main():
    application = Application()
    window = Test_Window(application, x=100, y=100)
    application.run()
    application.destroy()


if __name__ == "__main__":
    main()
