from src.typeclass.VFF import VFF
from src.VFF.fromCallable import fromCallable

class Split(VFF):
    def __init__(self, vff, callparam=lambda t:t):
        self.vff = vff
        self.callparam = callparam

    def __call__(self, t):
        return self.vff(self.callparam(t))

    # look to reconstruct this method s.t. we return reconstructed objects with updated
    # callparameters.
    def split(self, t):
        return [ Split(self.vff, callparam=lambda nt: self.callparam(t*nt))
               , Split(self.vff, callparam=lambda nt: self.callparam((1-t)*nt+t))
               ]

    def split_many(self, xs):
        if xs:
            x, *xs = xs
            sx, sxs = self.split(x)
            return [sx, *sxs.split_many(xs)]
        else:
            return [self]

    def split_spherical(self, thetas):
        pass
