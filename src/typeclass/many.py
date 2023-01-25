from abc import ABC, abstractmethod

from functools import cache
from itertools import combinations, product
from statistics import mean

class Many(ABC):
    ## () -> [VFF]
    @abstractmethod
    @cache
    def many(self):
        pass

    def center_of_mass(self):
        return tuple(map(mean, zip(*list(map(lambda x: x.center_of_mass(), self.many())))))

    def bounds(self):
        vffs = self.many()
        size = len(vffs[0](0))
        mins, maxs = list(zip(*map(lambda x: x.bounds(), vffs)))
        fn = lambda cmpfn, lst: tuple(cmpfn(lst, key=lambda x: x[i])[i] for i in range(size))
        return [fn(min,mins), fn(max, maxs)]

    def bounding_box(self):
        return list(product(*zip(*self.bounds())))



