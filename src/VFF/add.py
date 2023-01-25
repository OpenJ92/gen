from src.typeclass.VFF import VFF

class Add(VFF):
    def __init__(self, vff1, vff2):
        self.vff1 = vff1
        self.vff2 = vff2

    def __call__(self, t):
        return tuple(map(lambda x,y:x+y, self.vff1(t), self.vff2(t)))
