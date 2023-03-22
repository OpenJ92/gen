from src.typeclass.canvas import Canvas

from src.VFF.__Bezier__ import Bezier as B2

from src.drawables.deformto import deformTo
from src.drawables.fromVFF import fromVFF
from src.drawables.line import Line

from src.sample_method.linspace import Linspace

from src.VFF.rotate import Rotate

import numpy as np
from random import seed, randrange

class B2Play(Canvas):
    def __init__(self, data):
        self.data = data

    @classmethod
    def construct_random(cls, randseed):
        seed(randseed)
        data = [randrange(10, 50) for _ in range(2)]
        return cls(data)

    def drawable(self):
        i, j = self.data

        a1, a2 = (np.array([0,0]),np.array([1,0]))
        b1, b2 = (np.array([0,1]),np.array([1,1]))
        l1 = Line(*a1, *a2, stroke="blue", stroke_width="1.5")
        l2 = Line(*a2, *b2, stroke="blue", stroke_width="1.5")
        l3 = Line(*b2, *b1, stroke="blue", stroke_width="1.5")
        l4 = Line(*b1, *a1, stroke="blue", stroke_width="1.5")
        A = np.hstack((a1.reshape(2,1), -1*np.random.rand(2, i), a2.reshape(2,1)))
        B = np.hstack((b1.reshape(2,1), 2*np.random.rand(2, j), b2.reshape(2,1)))

        ## C = B2(np.stack((B, G, Q)),(0,2))
        ## breakpoint()

        return [  fromVFF(Rotate(-45, l1, callparam=lambda x: (x,)), Linspace(2))
                , fromVFF(Rotate(-45, l2, callparam=lambda x: (x,)), Linspace(2))
                , fromVFF(Rotate(-45, l3, callparam=lambda x: (x,)), Linspace(2))
                , fromVFF(Rotate(-45, l4, callparam=lambda x: (x,)), Linspace(2))
                , *deformTo(Rotate(-45, B2(A,(1,)))
                         ,Rotate(-45, B2(B,(1,)))
                         ,Linspace(300, transform=lambda x:(x,))
                         ,Linspace(500, transform=lambda x:(x,))).many()
               ]

    def __str__(self):
        return f"{self.__class__.__name__}(data={str(self.data)})"
