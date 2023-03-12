from src.typeclass.drawable import Drawable
from src.typeclass.many import Many
from src.typeclass.canvas import Canvas

from src.sample_method.linspace import Linspace

from src.drawables.line import Line
from src.drawables.map import Map
from src.drawables.polyline import PolyLine

from src.VFF.linend import LineND
from src.VFF.projection import Projection

from numpy import array

## Should deformTo operate with a LineND form and then be projected to the plane?

class deformTo(Many, Canvas):
    def __init__(self, vff1, vff2, samplPoly, samplVFF, projective_plane = array([[1,0],[0,1]]),stroke_width = .15):
        self.vff1 = vff1
        self.vff2 = vff2
        self.samplPoly = samplPoly
        self.samplVFF = samplVFF
        self.projective_plane = projective_plane
        self.stroke_width = stroke_width

    def spines(self):
        svff1 = self.vff1.sampl(self.samplVFF)
        svff2 = self.vff2.sampl(self.samplVFF)
        return [Line(*i, *j) for i, j in zip(svff1, svff2)]

    def many(self):
        spines = map(lambda x: x.sampl(self.samplPoly), self.spines())
        points    = zip(*spines)
        polylines = map(PolyLine, points)
        return list(polylines)

    def drawable(self):
        return self.many()


## DeformTo should be parameterized on spine VFF/Poly We'll call them down here as partial
## functions. 
