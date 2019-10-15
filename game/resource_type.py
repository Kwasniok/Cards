from core.internally_named import Internally_Named


class Resource_Type(Internally_Named):
    def __init__(self, name, source_name):
        Internally_Named.__init__(self, name)
        self.source = source_name

    def __repr__(self):
        return str(self)

    def get_name(self):
        return str(self)

    def get_source_name(self):
        return self.source
