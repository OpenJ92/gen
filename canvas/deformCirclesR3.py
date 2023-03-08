from src.drawables.circle import Circle
from src.typeclass.canvas import Canvas, A4, c30x30
from src.drawables.line import Line
from src.typeclass.many import Many
from src.drawables.fromVFF import fromVFF
from src.VFF.vectorDeformationMany import vectorDeformationMany
from src.VFF.radialVectorField import radialVectorField
from src.sample_method.linspace import Linspace
from canvas.grid import grid

from math import atan2, pow, e, pi
from functools import cache
from perlin_noise import PerlinNoise
from random import seed, randrange, choice

class deformCirclesR3(c30x30, Many):
    @classmethod
    def construct_random(self, m, randseed, maxcircle):
        seed(randseed)
        a, b, c = [randrange(1, 1000000) for _ in range(3)]
        d, e, f = [randrange(1, 7) for _ in range(3)]
        steps = randrange(2,maxcircle)
        return deformCirclesR3(m, [a, b, c, d, e, f, steps])

    def __init__(self, many, data):
        self.ynam = many
        self.data = data

    @cache
    def many(self):
        dSA, dSM, dSR, *self.data = self.data
        oA, oM, oR,    *self.data = self.data
        steps,         *self.data = self.data

        noiseAngle     = lambda x, y : 2*pi*PerlinNoise(oA,dSA)((x/c30x30.WIDTH,y/c30x30.HEIGHT))
        noiseAngle1    = lambda x, y : 2*pi*PerlinNoise(oR,dSM)((x/c30x30.WIDTH,y/c30x30.HEIGHT))
        noiseMagnitude = lambda x, y : 50*PerlinNoise(oM,dSM)((x/c30x30.WIDTH,y/c30x30.HEIGHT))
        noiseRadius    = lambda x, y : 30*PerlinNoise(oR ,dSR)((x/c30x30.WIDTH,y/c30x30.HEIGHT))

        transform = radialVectorField(noiseMagnitude, noiseAngle)
        deformed  = vectorDeformationMany(self.ynam, transform)

        for _ in range(steps - 2):
            deformed = vectorDeformationMany(deformed, transform)

        deformed  = vectorDeformationMany(deformed, transform).many()
        deformMap = []
        for deform in deformed:
            deformMap = [*deformMap, *deform.sampl(Linspace(100))]

        f = lambda x: Line(*x
                          , *Circle(*x, lambda _: noiseRadius(*x))(noiseAngle(*x))
                          , stroke_width = ".15")

        g = lambda x: Line(*x
                           , *Circle(*x, lambda _: noiseRadius(*x))(noiseAngle1(*x))
                           , stroke_width=".15")

        h = lambda x: Line(*x[0](1), *x[1](1)
                           , stroke_width=".15")

        circles  = list(map(f, deformMap))
        circles1 = list(map(g, deformMap))
        connect  = list(map(h, zip(circles, circles1)))
        return [*connect] #, *connect, *circles1]

    def drawable(self):
        return self.many()
        # return list(map(lambda x: fromVFF(x, Linspace(x.samples)), self.many()))

    def __str__(self):
        return f"{self.__class__.__name__}(many={str(self.ynam)}, data={str(self.data)})"

