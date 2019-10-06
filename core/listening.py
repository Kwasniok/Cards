from collections import defaultdict


class Listenable:
    def __init__(self):
        self._listenings = defaultdict(
            lambda: {}
        )  # method: list of lambdas to call

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

    def unregister_listener(method_name, listener):
        del self._listenings[method_name][listener]


def listenable(old_method):
    # decorator
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
