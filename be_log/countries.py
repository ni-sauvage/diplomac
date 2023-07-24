from territories import Territory
class Country:
    def __init__(self, centres : list[Territory], nunits: int, ncentres: int):
        self.centres = centres
        self.ncentres = ncentres
        self.nunits = nunits
