import networkx as nx
class Unit:
    def __init__(self):
        pass

class Fleet(Unit):
    def __init__(self, country : str):
        self.country = country

class Army(Unit):
    def __init__(self, country : str):
        self.country = country
