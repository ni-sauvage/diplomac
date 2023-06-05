from units import Unit
class Territory:
    def __init__(self, name : str, coastal : bool, l_s: bool, occ : Unit ):
        self.name = name
        self.coastal = coastal
        self.l_s = l_s
        self.occ = occ
    
    def __str__(self) -> str:
        return self.name