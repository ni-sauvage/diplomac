from territories import Territory
class Country:
    def __init__(self, name: str, ncentres : int, centres : list[Territory], nunits: int):
        self.name = name
        self.ncentres = ncentres
        self.centres = centres
        self.nunits = nunits
