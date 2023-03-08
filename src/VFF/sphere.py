from src.typeclass.VFF import VFF
from src.VFF.blade import Blade

from math import sin, cos
from numpy import hstack, array

class Sphere(VFF):
    def __init__(self, n):
        self.n = n

    def __call__(self, ts):
        cach = { t : { sin: sin(t), cos: cos(t) } for t in ts }
        return self.recursive_call(cach, array([1]), ts)

    def recursive_call(self, cach, arr, ts):
        t, *ts = ts
        arr = hstack((cach[t][cos]*arr, cach[t][sin]))
        if not ts: return arr
        else: return self.recursive_call(cach, arr, ts)



