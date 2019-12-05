from .listening import Listenable, listenable

# IDEA:
# A `Trigger` has a `pull` method which can be listened to (see .listening).


class Trigger(Listenable):
    def __init__(self):
        Listenable.__init__(self)

    @listenable
    def pull(self):
        pass

    def register(self, listener, listener_method):
        return self.register_listener("pull", listener, listener_method)

    def unregister(self, listener):
        return self.unregister_listener("pull", listener)
