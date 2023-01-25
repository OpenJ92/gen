from src.typeclass.drawable import Drawable
from src.typeclass.VFF import VFF

# should this just be matrix transform?
class Projection(VFF, Drawable):
    def __init__(self, vff, projection_normal):
        self.vff = vff
        self.projection_normal = projection_normal

    def __call__(self, t):
        (reduce(lambda x, y: x+y, zipWith(lambda x, y: x*y, self.vff(t), self.projection_normal[i]))
        for i
        in range(len(self.projection_normal)))
