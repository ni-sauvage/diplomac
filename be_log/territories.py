from units import Unit
class Territory:
    def __init__(self, name : str, occ : Unit ):
        self.name = name
        self.occ = occ
    
    def __str__(self) -> str:
        return self.name

class Sea(Territory):
    def __init__(self, name : str, occ : Unit):
        super().__init__(name, occ)

class Coastal(Territory):
    def __init__(self, name : str, occ : Unit, centre: bool, hs : bool):
        self.name = name
        self.occ = occ
        self.centre = centre
        self.hs = hs

class Inland(Territory):
    def __init__(self, name : str, occ : Unit, centre: bool, hs : bool):
        self.name = name
        self.occ = occ
        self.centre = centre
        self.hs = hs

