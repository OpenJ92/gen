from src.typeclass.VFF import VFF

class Translate(VFF):
    def __init__(self, dx, dy, vff, callparam=lambda t: t):
        self.dx = dx
        self.dy = dy
        self.vff = vff
        self.callparam = callparam

    def __call__(self, t):
        (x, y) = self.vff(self.callparam(t))
        return (x + self.dx, y + self.dy)

