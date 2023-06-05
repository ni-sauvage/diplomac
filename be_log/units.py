class Unit:
    def __init__(self, country : str):
        self.country = country

class Fleet(Unit):
    def __init__(self, country : str):
        super(Unit, self).__init__(self, country)

class Army(Unit):
    def __init__(self, country : str):
        super(Unit, self).__init__(self, country)