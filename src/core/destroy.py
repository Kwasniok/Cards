def safe_destroy(object):
    if not (object is None):
        object.destroy()
        object = None
    return object
