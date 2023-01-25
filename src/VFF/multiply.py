from src.typeclass.VFF import VFF

class Multiply(VFF):
    def __init__(self, vff1, vff2):
        self.vff1 = vff1
        self.vff2 = vff2

    ## vffs don't necesarily need to be two dimensional
    ## Maybe use your version of multiply which mimics Polynomials.
    def __call__(self, t):
        resolution = {}
        element = tuple(map(lambda x: tuple(map(lambda y: x*y,self.vff2(t))), self.vff1(t)))

        for i in range(len(element)):
            for j in range(len(element[0])):
                if i+j not in resolution.keys():
                    resolution[i+j] = element[i][j]
                else:
                    resolution[i+j] += element[i][j]

        return tuple(resolution.values())
