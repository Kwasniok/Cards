import inspect

_supported_action_additional_argument_types = []


def get_all_supported_action_additional_argument_types():
    return tuple(_supported_action_additional_argument_types)


def register_supported_action_additional_argument_type(typ):
    if not (isinstance(typ, type)):
        raise (TypeError("Cannot register non-type object."))
    if not typ in _supported_action_additional_argument_types:
        _supported_action_additional_argument_types.append(typ)


def unregister_all_supported_action_additional_argument_types():
    _supported_action_additional_argument_types.clear()


# interface:
# def on_<action_name>(self, context, <kwarg_1>:<kwarg_1_type>, ..., <kwarg_N>:<kwarg_N_type>)
def action(action_function):
    # check function name
    if not action_function.__name__.startswith("on"):
        raise (
            TypeError(
                "Function "
                + action_function.__qualname__
                + " decorated with @action must have a name beginning with `on` (not fullfilled by `"
                + action_function.__name__
                + "`)."
            )
        )
    # check required arguments
    argument_names = inspect.getfullargspec(action_function).args
    if not len(argument_names) >= 2:
        raise (
            TypeError(
                "Function "
                + action_function.__qualname__
                + " decorated with @action must have at laest two arguments."
            )
        )
    if not argument_names[0] == "self":
        raise (
            TypeError(
                "Function "
                + action_function.__qualname__
                + " decorated with @action must have first argument called `self` (not `"
                + argument_names[0]
                + "`)."
            )
        )
    if not argument_names[1] == "context":
        raise (
            TypeError(
                "Function "
                + action_function.__qualname__
                + " decorated with @action must have first argument called `context` (not `"
                + argument_names[1]
                + "`)."
            )
        )
    # check optional arguments
    for i in range(2, len(argument_names)):
        additional_argument_name = argument_names[i]
        if not additional_argument_name in action_function.__annotations__:
            raise (
                TypeError(
                    "Function "
                    + action_function.__qualname__
                    + " decorated with @action must have annotated additional arguments only: Argument `"
                    + additional_argument_name
                    + "` has no annotation. (In function definition: Replace `"
                    + additional_argument_name
                    + "` with `"
                    + additional_argument_name
                    + ":<type>` where `<type>` is "
                    + " or ".join(
                        [
                            "`" + t.__qualname__ + "`"
                            for t in _supported_action_additional_argument_types
                        ]
                    )
                    + ")"
                )
            )
        annotation = action_function.__annotations__[additional_argument_name]
        if not isinstance(annotation, type):
            raise (
                TypeError(
                    "Function "
                    + action_function.__qualname__
                    + " decorated with @action must have additional arguments annotated with a type only: Argument `"
                    + additional_argument_name
                    + "` has non-type annotation `"
                    + str(annotation)
                    + "`."
                )
            )
        if not issubclass(
            annotation, tuple(_supported_action_additional_argument_types)
        ):
            raise (
                TypeError(
                    "Function "
                    + action_function.__qualname__
                    + " decorated with @action must have additional arguments annotated with a supported types only: Argument `"
                    + additional_argument_name
                    + "` has non supported annotation `"
                    + annotation.__qualname__
                    + "` (must be "
                    + " or ".join(
                        [
                            "`" + t.__qualname__ + "`"
                            for t in _supported_action_additional_argument_types
                        ]
                    )
                    + ")."
                )
            )
    # mark as action
    action_function._is_game_action = None
    # forwarding
    return action_function


def is_game_action(function):
    return hasattr(function, "_is_game_action")


def get_additional_action_argument_types(action_function):
    if not is_game_action(action_function):
        raise (
            TypeError(
                "Function "
                + action_function.__qualname__
                + " is not a @action."
            )
        )
    additional_argument_names = inspect.getfullargspec(action_function).args[2:]
    return tuple(
        [
            action_function.__annotations__[additional_argument_name]
            for additional_argument_name in additional_argument_names
        ]
    )


def get_all_bound_action_methods(object):
    bound_action_methods = []
    # search for bound `@action` methods
    for attribute_name in dir(object):
        # skip private attributes
        if attribute_name.startswith("_"):
            continue
        # check if `_is_game_action` attribute is present
        attribute = getattr(object, attribute_name)
        if callable(attribute) and hasattr(attribute, "_is_game_action"):
            # found a `@action`
            bound_action_methods.append(attribute)
    return bound_action_methods
