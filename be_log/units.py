import networkx as nx
class Unit:
    def __init__(self, country : str, pos : str):
        self.country = country

class Fleet(Unit):
    def __init__(self, country : str, pos: str):
        super(Unit, self).__init__(self, country, pos)

class Army(Unit):
    def __init__(self, country : str, pos: str):
        super(Unit, self).__init__(self, country, pos)
