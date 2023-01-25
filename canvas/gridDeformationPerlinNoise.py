from src.typeclass.canvas import Canvas
from src.drawables.fromVFF import fromVFF
from src.VFF.vectorDeformationMany import vectorDeformationMany
from src.VFF.radialVectorField import radialVectorField
from src.sample_method.linspace import Linspace
from canvas.grid import grid

from perlin_noise import PerlinNoise
from math import atan2, pow, e, pi

class gridDeformationPerlinNoise(Canvas):
    def __init__(self, many, deformSeedAngle, deformSeedMagnitude, octavesAngle=5, octavesMagnitude=20):
        self.deformSeedAngle = deformSeedAngle
        self.deformSeedMagnitude = deformSeedMagnitude
        self.octavesAngle = octavesAngle
        self.octavesMagnitude = octavesMagnitude
        self.ynam = many

    def drawable(self):
        return list(map(lambda x : fromVFF(x, Linspace(300)), self.many()))

    def many(self):
        pure_grid = self.ynam

        noiseAngle     = lambda x, y : 2*pi*PerlinNoise(octaves=self.octavesAngle, seed=self.deformSeedAngle)((x/Canvas.WIDTH,y/Canvas.HEIGHT))
        noiseMagnitude = lambda x, y : 5*PerlinNoise(octaves=self.octavesMagnitude, seed=self.deformSeedMagnitude)((x/Canvas.WIDTH,y/Canvas.HEIGHT))
        transform = radialVectorField(noiseMagnitude, noiseAngle)
        print(self)

        return vectorDeformationMany(pure_grid, transform).many()
