from src.typeclass.canvas import Canvas
from src.typeclass.many import Many

from src.drawables.line import Line
from src.drawables.deformto import deformTo

from src.sample_method.linspace import Linspace

class grid(Canvas, Many):
    @classmethod
    def constructGivenDensity(cls, dpsm, sm, *data):
        # constuct grid with desired density (dpsm) per particular square mm size (sm)
        # Ultimatly, we're looking to put together the vertical and horizontal sample
        # together so as to achieve the given 
        pass

    def __init__( self

                , xmin, ymin
                , xmax, ymax

                , verticalSample = Linspace(600)
                , horizontalSample = Linspace(600)

                ):

        self.xmin = xmin ; self.ymin = ymin
        self.xmax = xmax ; self.ymax = ymax

        self.verticalSample = verticalSample
        self.horizontalSample = horizontalSample

    def vertical(self):
        horizontalTop = Line(self.xmin, self.ymin, self.xmax, self.ymin, stroke_width=".2")
        horizontalBot = Line(self.xmin, self.ymax, self.xmax, self.ymax, stroke_width=".2")
        return deformTo(horizontalTop, horizontalBot, self.horizontalSample, self.horizontalSample)

    def horizontal(self):
        verticalTop   = Line(self.xmin, self.ymin, self.xmin, self.ymax, stroke_width=".2")
        verticalBot   = Line(self.xmax, self.ymin, self.xmax, self.ymax, stroke_width=".2")
        return deformTo(verticalTop, verticalBot, self.verticalSample, self.verticalSample)

    def drawable(self):
        horizontalGrid = self.horizontal()
        verticalGrid   = self.vertical()
        return [*horizontalGrid.many(), *verticalGrid.many()]

    def many(self):
        return self.drawable()

    def __str__(self):
        return f"{self.__class__.__name__}(xmin={self.xmin},ymin={self.ymin},xmax={self.xmax},ymax={self.ymax},verticalSample={str(self.verticalSample)},horizontalSample={str(self.horizontalSample)})"
