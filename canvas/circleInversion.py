from src.typeclass.canvas import Canvas
from src.typeclass.VFF import VFF
from src.typeclass.many import Many
from src.drawables.fromVFF import fromVFF
from src.sample_method.linspace import Linspace

from math import sqrt

class circleInversion(Many, Canvas):
    def __init__(self, many, data):
        self.ynam = many
        self.data = data

    def construct_random(cls, randseed, canvas):
        seed(randseed)
        raise NotImplementedError

        ## given the context of the figure (perhaps its center), make a selection
        ## on the center and radius of the inversion. Perhaps it'll be sufficent
        ## to supply just the Canvas component with it's dimensions.

        return lambda many: cls(many, constructed_data)

    def many(self):
        cx, cy, r = self.data
        return list(map(lambda x: Invert(cx, cy, r, x), self.ynam.many()))

    def drawable(self):
        return list(map(lambda x: fromVFF(x, Linspace(500)), self.many()))

    def __str__(self):
        return f"{self.__class__.__name__}(many={str(self.ynam)}, data={self.data})"

class Invert(VFF):
    def __init__(self, cx, cy, r, vff, callparam=lambda t:t):
        self.cx = cx
        self.cy = cy
        self.r  = r
        self.vff = vff
        self.callparam = callparam

    def __call__(self, t):
        (x, y) = self.vff(self.callparam(t))

        dx = x - self.cx;
        dy = y - self.cy;
        dist0 = sqrt(dx * dx + dy * dy);
        dist1 = self.r * self.r / dist0;
        ratio = dist1 / dist0;
        return (self.cx + dx * ratio, self.cy + dy * ratio)
