from abc import abstractmethod
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
    @abstractmethod
    def __init__(self):
        # dict of listenings:
        # key: method_name (string, name of a method of self, method must be
        #      decorated with listenable)
        # value: dict where
        #            key: listener (object; can be `None` for global listening)
        #            value: listener_method (function taking the listener
        #                   as its argument or method name (non-global
        #                   listening only))
        self._listenings = defaultdict(lambda: {})

    # method_name : str; self.<method_name> must be a defined method
    # listener: None or object; None means global listening
    # listener_method: function or str; if str then listener != None and
    #                  listener.<listener_method> must be a defined method
    #                  taking nor arguments; if function then listener_method
    #                  == listener.<listener_method> or some function taking #                  one argument
    def register_listener(self, method_name, listener, listener_method):
        if not (callable(listener_method) or type(listener_method) is str):
            raise (
                ValueError(
                    "Cannot register listener: "
                    + str(self)
                    + " because its method "
                    + str(listener_method)
                    + " is neither callable nor a string."
                )
            )
        if (listener is None) and (not callable(listener_method)):
            raise (
                ValueError(
                    "Cannot register listener (NONE) "
                    + " because "
                    + str(listener_method)
                    + " must be callable."
                )
            )
        if (type(listener_method) is str) and (
            not hasattr(listener, listener_method)
        ):
            raise (
                ValueError(
                    "Cannot register listener: "
                    + str(self)
                    + " because its method "
                    + listener_method
                    + " is not defined."
                )
            )
        if type(listener_method) is str:
            attr = getattr(listener, listener_method)
            if not callable(attr):
                raise (
                    ValueError(
                        "Cannot register listener: "
                        + str(self)
                        + " because "
                        + listener_method
                        + " is not a callable method."
                    )
                )
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

    def unregister_listener(self, method_name, listener):
        if method_name in self._listenings:
            listening = self._listenings[method_name]
            if listener in listening:
                del listening[listener]


def listenable(old_method):
    # decorator, to define method as listenable
    # call old_method first
    # call all listeners afterwards
    def new_method(self, *args, **kwargs):
        old_method(self, *args, **kwargs)
        for listener, listener_method in self._listenings[
            old_method.__name__
        ].items():
            if not callable(listener_method):
                # listener_method is a string --> execute listener.<listener_method>()
                listener_method = getattr(listener, listener_method)
                listener_method()
            else:
                # listener_method is a function
                listener_method(listener)

    # mark decorated method as listenable
    new_method._listenable = None
    return new_method
