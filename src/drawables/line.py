from src.typeclass.drawable import Drawable
from src.typeclass.VFF import VFF

class Line(Drawable, VFF):
    def __init__(self, x1, y1, x2, y2, stroke = "black", stroke_width = .1, callparam=lambda t:t):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.callparam = callparam

    def svg(self):
        return f"<line x1=\"{self.x1}\" x2=\"{self.x2}\" y1=\"{self.y1}\" y2=\"{self.y2}\" fill=\"none\" stroke=\"{self.stroke}\" stroke-width=\"{self.stroke_width}\" />"

    def __call__(self, t):
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        return ( self.x1 + self.callparam(t) * dx
               , self.y1 + self.callparam(t) * dy
               )

