from .listeining import Listenable


class Trigger(Listenable):
    def __init__(self):
        Listenable.__init__(self)

    @listenable
    def pull(self):
        pass

    def register(listener, listener_method):
        return self.register_listener("pull", listener, listener_method)

    def unregister(listener):
        return self.unregister_listener("pull", listener)
