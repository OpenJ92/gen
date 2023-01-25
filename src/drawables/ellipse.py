from src.typeclass.drawable import Drawable
from src.typeclass.VFF import VFF

from math import cos, sin, pi

class Ellipse(Drawable, VFF):
    def __init__(self, cx, cy, rx, ry):
        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry

    def svg(self):
        return f"<ellipse cx={self.cx} cy={self.cy} rx={self.rx} ry={self.ry} />"

    def __call__(self, t):
        x = self.rx * cos(t / (2 * pi))
        y = self.ry * sin(t / (2 * pi))
        return (self.cx + x, self.cy + y)
