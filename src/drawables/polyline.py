from src.typeclass.drawable import Drawable
from src.typeclass.VFF import VFF
from src.typeclass.many import Many

from src.drawables.line import Line

from math import modf
import functools

class PolyLine(Drawable, Many, VFF):
    def __init__(self, points, callparam=lambda t:t):
        self.points = points
        self.length = len(self.points)
        self.callparam = callparam

    def svg(self):
        out = ""
        for point in self.points:
           x, y = point
           out += f"{x},{y} "
        return f"<polyline points=\"{out}\" fill=\"none\" stroke=\"black\" stroke-width=\".2\"/>"

    @functools.lru_cache(maxsize=None)
    def many(self):
        return [Line(*i, *j) for i, j in zip(self.points, self.points[1:])]

    def __call__(self, t):
        t = self.callparam(t)
        spines = self.many(); lenspines = len(spines)
        prime = t * lenspines

        if (prime >= lenspines):
            frac, whole = 1, lenspines - 1
        elif (prime < 0):
            frac, whole = 0, 0
        else:
            frac, whole = modf(prime)

        return spines[int(whole)](frac)
