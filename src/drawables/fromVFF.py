from src.drawables.polyline import PolyLine
from src.typeclass.drawable import Drawable

class fromVFF(Drawable):
    def __init__(self, vec, sampl):
        self.vec = vec
        self.sampl = sampl

    def svg(self):
        return PolyLine(self.vec.sampl(self.sampl)).svg()
