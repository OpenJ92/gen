from src.typeclass.VFF import VFF

class Scale(VFF):
    def __init__(self, vff, constant):
        self.vff = vff
        self.constant = constant

    def __call__(self, t):
        return tuple(map(lambda x: x * self.constant, self.vff(t)))
