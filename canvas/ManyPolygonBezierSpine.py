from src.typeclass.canvas import Canvas
from src.typeclass.drawable import Drawable

from src.drawables.line import Line

from src.VFF.bezier import Bezier

from numpy import array

class ManyPolygonBezierSpine(Canvas):
    ## __init__ :: [Int] -> (Int, Int) -> [Int] -> [Int]
    def __init__(self, starts, end, control, cont_dist):
        self.starts = self.pairstarts(starts)
        self.end = end
        self.control = self.pairstarts(control)
        self.cont_dist = cont_dist

    def drawable(self):
        ## construct Bezier curves from input data
        ## Sample equitably these curves for line construction
        ## Map Polygons over sample point row space
        ## Supply polygons to caller.
        starting_points = self.pairedstarts(self.starts)

    def pairstarts(self, starts):
        pairedstarts = []
        while len(starts) > 0:
            x, y, *starts = starts
            pairedstarts.append((x,y))
        return pairedstarts

    ## split :: [(Int, Int)] -> ([(Int, Int)], [(Int, Int)])
    def split(self, control, dist):
        return control[0:dist], control[dist:-1]
