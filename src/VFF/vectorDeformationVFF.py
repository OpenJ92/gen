from src.typeclass.VFF import VFF

class vectorDeformationVFF(VFF):
    def __init__(self, vff, deformationFunction, callparam=lambda t:t):
        self.vff = vff
        self.deformationFunction = deformationFunction
        self.callparam = callparam

    def __call__(self, x):
        x = self.callparam(x)
        return self.deformationFunction(*self.vff(x))
