from src.typeclass.VFF import VFF

from numpy import array

class Projection(VFF):
    def __init__(self, vff, projective_plane):
        self.vff = vff
        self.projective_plane = projective_plane

    def __call__(self, t):
        return tuple(self.projective_plane @ array(self.vff(t)))
