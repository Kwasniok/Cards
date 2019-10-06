from collections import defaultdict

# IDEA:
# Whenever
#     listenable_object.action(arg1, ..., argN)
# is called
#     listener_object.on_action()
# should be called (afterwards) as well.

# IMPLEMENTATION:
# i) `listenable_object` must be a Listenable
# ii) `action` must be decorated with `@listenable`
# iii) `listener_object` must be registered via:
#     listenable_object.register_listener("action",
#                                         listener_object,
#                                         Listener.on_Action
#                                        )
#
# Note: At most one on_action per listener_object per action per
#       listenable_object.


class Listenable:
    def __init__(self):
        # dict of listenings:
        # key: method_name (string, name of a method of self, method must be
        #      decorated with listenable)
        # value: dict where
        #            key: listener (object)
        #            value: listener_method (function taking the listener
        #                   as its argument)
        self._listenings = defaultdict(lambda: {})

    def register_listener(self, method_name, listener, listener_method):
        # self.<method_name> must exist
        if not (hasattr(self, method_name)):
            raise (
                ValueError(
                    "Cannot register listener: "
                    + str(self)
                    + " has no method "
                    + method_name
                )
            )
        # self.<method_name> must be a method
        attr = getattr(self, method_name)
        if not callable(attr):
            raise (
                ValueError(
                    "Cannot register listener: "
                    + str(self)
                    + " has an attribute "
                    + method_name
                    + " but it is not callable."
                )
            )
        if not (hasattr(attr, "_listenable")):
            raise (
                ValueError(
                    "Cannot register listener: "
                    + str(self)
                    + " has a method "
                    + method_name
                    + " but it is not listenable."
                )
            )

        self._listenings[method_name][listener] = listener_method

        del self._listenings[method_name][listener]
    def unregister_listener(self, method_name, listener):


def listenable(old_method):
    # decorator, to define method as listenable
    # call old_method first
    # call all listeners afterwards
    def new_method(self, *args, **kwargs):
        old_method(self, *args, **kwargs)
        for listener, listener_method in self._listenings[
            old_method.__name__
        ].items():
            listener_method(listener)

    # mark decorated method as listenable
    new_method._listenable = None
    return new_method
