from canvas.B2play import B2Play
from canvas.gridDeformationPerlinNoise import gridDeformationPerlinNoise

from src.typeclass.canvas import Canvas

import random

class B2wDeformation(Canvas):
    def __init__(self, data):
        self.data = data

    def drawable(self):
        b2i, *self.data = self.data
        dsa, dsm, oa, om, *self.data = self.data

        ## this is deeply broken
        sculpture = B2Play.construct_random(b2i)
        sculpture_def = gridDeformationPerlinNoise(sculpture, dsa, dsm, oa, om)
        return sculpture_def.drawable()

    def __str__(self):
        return f"{self.__class__.__name__}(data={str(self.data)})"
