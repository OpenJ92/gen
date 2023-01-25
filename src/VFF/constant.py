from src.typeclass.VFF import VFF

class Constant(VFF):
    def __init__(self, point):
        self.point = point

    def __call__(self, t):
        return self.point
