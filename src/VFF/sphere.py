from src.typeclass.VFF import VFF
from src.VFF.blade import Blade

from math import sin, cos
from numpy import hstack, array

class Sphere(VFF):
    def __call__(self, ts):
        return self.recursive_call(array([1]), ts)

    def recursive_call(self, arr, ts):
        t, *ts = ts
        arr = hstack((cos(t)*arr, sin(t)))
        if ts: return self.recursive_call(arr, ts)
        else : return arr



