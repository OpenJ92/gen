from src.typeclass.drawable import Drawable
from src.typeclass.many import Many

class Map(Many, Drawable):
    def __init__(self, drawable, vff, sampl):
        self.drawable = drawable
        self.vff = vff
        self.sampl = sampl

    def many(self):
        return [self.drawable(*point) for point in self.vff.sampl(self.sampl)]

    def svg(self):
        return "".join(map(lambda x: x.svg(), self.many()))
