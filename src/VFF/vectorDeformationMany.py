from src.typeclass.many import Many
from src.VFF.vectorDeformationVFF import vectorDeformationVFF

class vectorDeformationMany(Many):
    def __init__(self, ynam, deformationFunction):
        self.ynam = ynam
        self.deformationFunction = deformationFunction

    def many(self):
        return [vectorDeformationVFF(vff, self.deformationFunction) for vff in self.ynam.many()]
