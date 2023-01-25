from src.typeclass.sample_method import Sample_Method

from numpy.random import beta, seed
from numpy import sort

class Beta(Sample_Method):
    def __init__(self, alpha, beta, num, _seed = 10):
        self.alpha = alpha
        self.beta = beta
        self.num = num
        self.seed = _seed

    def values(self):
        ## without the seed, you get a lot of erratic behavior
        seed(self.seed)
        return sort(beta(self.alpha, self.beta ,size=self.num))
