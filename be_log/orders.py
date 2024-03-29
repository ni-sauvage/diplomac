class Order():
    def __init__(self) -> None:
        pass

class Move(Order):
    def __init__(self, u_t : str, start : str, end : str) -> None:
        self.u_t = u_t
        self.start = start
        self.end = end
        self.strength : int = 1

class MoveSupport(Order):
    def __init__(self, u_t : str, loc : str, sup_unit_start : str, sup_unit_end : str):
        self.u_t = u_t
        self.loc = loc
        self.sup_unit_start = sup_unit_start
        self.sup_unit_end = sup_unit_end
        self.strength : int = 1

class Hold(Order):
    def __init__(self, u_t : str, loc : str) -> None:
        self.u_t = u_t
        self.loc = loc
        self.strength : int = 1

class Convoy(Order):
    def __init__(self, u_t : str, loc : str, con_unit_start : str, con_unit_end : str):
        self.u_t = u_t
        self.loc = loc
        self.con_unit_start = con_unit_start
        self.con_unit_end = con_unit_end
        self.strength : int = 1

class HoldSupport(Order):
    def __init__(self, u_t : str, loc : str, sup_unit_loc : str):
        self.u_t = u_t
        self.loc = loc
        self.sup_unit_loc = sup_unit_loc
        self.strength : int = 1
        