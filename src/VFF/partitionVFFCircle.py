from src.typeclass.many import Many

from src.VFF.split import Split
from src.VFF.translate import Translate
from src.drawables.polyline import PolyLine

from src.sample_method.linspace import Linspace

from math import sqrt
from itertools import cycle

class partitionVFFCircle(Many):
    def __init__(self, cx, cy, r, vff):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.vff = vff

    def many(self):
        recentered = Translate(-self.cx, -self.cy, self.vff)
        sample = PolyLine(recentered.sampl(Linspace(1000))).many()
        samples = list(zip(Linspace(1000).values(),sample))

        get_domains = []
        get_inout = []
        currentinout = None
        result = {"inside":[], "outside":[]}

        for (t, val) in samples:
            (check, inout) = self.check(val.x1,val.y1,val.x2,val.y2)
            if inout != currentinout:
                get_inout.append(inout)
                currentinout = inout
            if check:
                get_domains.append(t)

        # Version 1
        # partitions = Split(self.vff, self.vff.callparam).split_many(get_domains)
        partitions = Split(self.vff).split_many(get_domains)
        for key, part in zip(get_inout, partitions):
            result[key].append(part)

        return result


    def check(self, x1, y1, x2, y2):
        cP1 = self.measure(x1, y1)
        cP2 = self.measure(x2, y2)
        return ( True if ((cP1 * cP2) <= 0) else False
               , "inside" if (cP2 < 0) and (cP2 < 0) else "outside"
               )

    def measure(self, x, y):
        return (x)**2 + (y)**2 - self.r**2

