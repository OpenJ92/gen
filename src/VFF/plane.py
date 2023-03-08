from src.typeclass.VFF import VFF

class Plane(VFF):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __call__(self, ts):
        t1, t2, *ts = ts

        return t1*self.p1 + t2*self.p2
