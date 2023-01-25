from src.typeclass.drawable import Drawable
from src.typeclass.VFF import VFF

from src.drawables.polyline import PolyLine
from src.sample_method.linspace import Linspace

from math import cos, sin, pi

class Circle(Drawable, VFF):
    def __init__(self, cx, cy, r, init = lambda t : 0, freq = lambda t: 1, fill="none", callparam=lambda t: t, points = Linspace(100)):
        self.cx = cx
        self.cy = cy
        self.r  = r
        self.init = init
        self.freq = freq
        self.fill = fill
        self.callparam = callparam
        self.points = points

    def svg(self):
        return PolyLine(list(map(self, self.points.values()))).svg()
        # return f"<circle cx=\"{self.cx}\" cy=\"{self.cy}\" r=\"{self.r}\" fill=\"{self.fill}\" stroke=\"black\" stroke-width=\".1\"/>"

    def __call__(self, t):
        ## breakpoint()
        x = self.r(t) * cos(self.freq(t) * self.callparam(t) * (2 * pi) + self.init(t))
        y = self.r(t) * sin(self.freq(t) * self.callparam(t) * (2 * pi) + self.init(t))
        return (self.cx + x, self.cy + y)
