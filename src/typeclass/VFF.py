from src.typeclass.samplable import Samplable
from src.sample_method.linspace import Linspace
## from src.sample_method.strategy import LinspaceStrat

from math import sqrt
from abc import ABC, abstractmethod
from functools import reduce, cached_property, cache
from itertools import combinations, product
from statistics import mean

class VFF(Samplable, ABC): ## Splitable(?)
    # [0,1] -> (,)
    @abstractmethod
    def __call__(self):
        pass

    def sampl(self, sample_method):
        return list(map(self, sample_method.values()))

    def center_of_mass(self):
        return tuple(map(mean, zip(*self.sampl(Linspace(10)))))

    @cached_property
    def approx_length(self):
        sample = self.sampl(Linspace(10))
        length = lambda x: (x[0][1] - x[1][1])**2 + (x[0][0] - x[1][0])**2
        add    = lambda x, y: x + y
        return sqrt(reduce(add, map(length, zip(sample, sample[1:]))))

    def bounds(self):
        samp = self.sampl(Linspace(10))
        size = len(self(0))
        mins = tuple(min(samp, key=lambda x: x[i])[i] for i in range(size))
        maxs = tuple(max(samp, key=lambda x: x[i])[i] for i in range(size))
        return [mins, maxs]

    def bounding_box(self):
        return list(product(*zip(*self.bounds())))

    ## def make_sample(self, strat):
    ##     length = self.approx_length()
    ##     sample_method = strat(length)
    ##     ## Consider what the form of strat should be. Clearly it's a VFF
    ##     ## in what sense is unclear to me at the moment.
    ##     return sample_method



    ## look to implement a length based linspace constructor.
    ## What's more, look to make a curvature dependant transform
    ## where we can make use of components of one dimensional dynamics
    ## to have higher density of sampling in regions of high curvature
