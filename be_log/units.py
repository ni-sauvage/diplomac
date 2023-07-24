import networkx as nx
import orders

class Unit:
    def __init__(self):
        pass

class Fleet(Unit):
    def __init__(self, country : str):
        self.country = country
        self.order : orders.Order = None

class Army(Unit):
    def __init__(self, country : str):
        self.country = country
        self.order : orders.Order = None
