import operator
from functools import reduce


class Strict_Argument_Type_Error(TypeError):
    def __init__(self, msg):
        TypeError.__init__(self, msg)


# decorator for type requirments of function arguments
# example:
#       @strict_argument_types
#       def f(a:int, b): pass
#
#       f(a=1, b="test") # ok
#       f(a=str, b="test") # error: wrong type for a
#       f(1, b="test") # error: must be called with keyword arguments only
# WARNING: This decorator slows the call time of decorated functions
#          significantly and non-keyword arguments a not possible!
def strict_argument_types(func):
    # check if all annotations for arguments are types (or tuples of types)
    for arg_name, arg_annotation in func.__annotations__.items():
        if isinstance(arg_annotation, type) or (
            isinstance(arg_annotation, tuple)
            and reduce(
                operator.__and__,
                [
                    isinstance(tuple_element, type)
                    for tuple_element in arg_annotation
                ],
            )
        ):
            pass
        else:
            raise (
                Strict_Argument_Type_Error(
                    "Cannot ceate function "
                    + str(func.__name__)
                    + " with strict argument typing: Annotation for argument "
                    + arg_name
                    + " must be an type."
                )
            )

    def dec_func(*args, **kwargs):
        # reject non-keyword arguments as thier type cannot be inferred
        if args:
            raise (
                Strict_Argument_Type_Error(
                    "Cannot call function `"
                    + str(func.__name__)
                    + "` with strict argument types: Non-keyword arguments are not supported."
                )
            )

        # check if all keyword arguments have the correct types
        for name, value in kwargs.items():
            if name in func.__annotations__:
                if not isinstance(value, func.__annotations__[name]):
                    msg = (
                        "Cannot call function `"
                        + str(func.__name__)
                        + "` with strict argument types: Argument `"
                        + name
                        + "` must be an instance of "
                    )
                    annotation = func.__annotations__[name]
                    if isinstance(annotation, type):
                        msg += "`" + annotation.__name__ + "`"
                    if isinstance(annotation, tuple):
                        msg += " or ".join(
                            ["`" + elem.__name__ + "`" for elem in annotation]
                        )
                    msg += "."
                    raise (Strict_Argument_Type_Error(msg))
        return func(**kwargs)

    dec_func.__annotations__ = func.__annotations__
    return dec_func
