from src.typeclass.VFF import VFF

from math import sin, cos, pi

class Rotate(VFF):
    def __init__(self, angle, vff, callparam=lambda t:t):
        self.angle = (2*pi/360)*angle
        self.vff = vff
        self.callparam = callparam

    def __call__(self, t):
        (x, y) = self.vff(self.callparam(t))
        return ( cos(self.angle)*x - sin(self.angle)*y
               , sin(self.angle)*x + cos(self.angle)*y
               )

