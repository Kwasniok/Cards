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


LOGS = Resource_Type("Logs", "Wood")
BRICKS = Resource_Type("Bricks", "Clay Pit")
GRAIN = Resource_Type("Grain", "Field")
IRON = Resource_Type("Iron", "Mountain")
WOOL = Resource_Type("Wool", "Meadow")
GOLD = Resource_Type("Gold", "River")
