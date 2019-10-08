import tkinter as tk


class Root:
    _root = None
    _application = None

    @staticmethod
    def register_application(application):
        if not (Root._application is None):
            raise (RuntimeError("Only one Application is allowed."))
        Root._application = application

    @staticmethod
    def unregister_application():
        Root._application = None

    def get_root():
        if Root._root is None:
            Root._root = tk.Tk()
            # disable default window
            Root._root.withdraw()
        return Root._root

    @staticmethod
    def get_application():
        return Root._application
