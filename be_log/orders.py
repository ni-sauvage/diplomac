class Move():
    def __init__(self, u_t : str, start : str, end : str) -> None:
        self.u_t = u_t
        self.start = start
        self.end = end

class MoveSupport():
    def __init__(self, u_t : str, loc : str, sup_unit_start : str, sup_unit_end : str):
        self.u_t = u_t
        self.loc = loc
        self.sup_unit_start = sup_unit_start
        self.sup_unit_end = sup_unit_end

class Hold():
    def __init__(self, u_t : str, loc : str) -> None:
        self.u_t = u_t
        self.loc = loc

class Convoy():
    def __init__(self, u_t : str, loc : str, con_unit_start : str, con_unit_end : str):
        self.u_t = u_t
        self.loc = loc
        self.con_unit_start = con_unit_start
        self.con_unit_end = con_unit_end

class HoldSupport():
    def __init__(self, u_t : str, loc : str, sup_unit_loc : str):
        self.u_t = u_t
        self.loc = loc
        self.sup_unit_loc = sup_unit_loc
        