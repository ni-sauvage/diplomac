from units import Unit
class Territory:
    def __init__(self, name : str, occ : Unit ):
        self.name: str = name
        self.occ : Unit = occ
    
    def __str__(self) -> str:
        return self.name

class Sea(Territory):
    def __init__(self, name : str, occ : Unit):
        super().__init__(name, occ)

class Coastal(Territory):
    def __init__(self, name : str, centre: bool, hc : str, occ : Unit):
        self.name   : str = name
        self.occ    : Unit = occ
        self.centre : bool = centre
        self.hc     : bool = hc

class Inland(Territory):
    def __init__(self, name : str, centre: bool, hc : str, occ : Unit):
        self.name   : str = name
        self.occ    : Unit = occ
        self.centre : bool = centre
        self.hc     : bool = hc

