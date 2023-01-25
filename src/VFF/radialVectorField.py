from src.typeclass.VFF import VFF
from math import sin, cos, pi, sqrt

class radialVectorField(VFF):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    def __call__(self, x, y):
        evalmag = self.magnitude(x, y)
        evalang = self.angle(x, y)
        unitx = x / sqrt(x**2 + y**2)
        unity = y / sqrt(x**2 + y**2)
        return ( evalmag * (unitx*cos(evalang) - unity*sin(evalang)) + x
               , evalmag * (unitx*sin(evalang) + unity*cos(evalang)) + y
               )
