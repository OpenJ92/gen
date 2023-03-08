from src.typeclass.VFF import VFF

from functools import reduce
from numpy import array_split, identity

class Blade(VFF):
    @classmethod
    def unit(cls, n):
        return cls(array_split(identity(n), n))
    def __init__(self, vs):
        self.vs = vs

    def __call__(self, ts):
        return reduce(lambda x, y: x + y, map(lambda l: l[0]*l[1], zip(self.vs, ts)))
