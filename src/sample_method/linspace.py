from src.typeclass.sample_method import Sample_Method

from numpy import linspace

class Linspace(Sample_Method):
    def __init__(self, num, start = 0, end = 1, transform = lambda x: x):
        self.num   = num
        self.start = start
        self.end   = end
        self.transform = transform

    def values(self):
        return map(self.transform, linspace(self.start,self.end,self.num))

    def __str__(self):
        return f"{self.__class__.__name__}(num={self.num},start={self.start},end={self.end})"
