from src.typeclass.canvas import Canvas

from src.sample_method.linspace import Linspace

from src.VFF.constant import Constant

from src.drawables.deformto import deformTo
from src.drawables.circle import Circle

import numpy as np
from random import seed, randrange

class glitchCircle(Canvas):
    def __init__(self, data):
        self.data = data

    def drawable(self):
        circle1 = Circle(Constant(0), Constant(0), Constant(1))

        ## Here we want to implement a sort of smooth step function with identical 
        ## values on the endpoints. A great variety of values and big changes will be great.
        ## We should finally introduce the logistic VFF. What's more, the radius function should
        ## have some noise introduced to distinguish these from B2Play Canvas.
        make_radius = Constant(10)
        circle2 = Circle(Constant(0), Constant(0), make_radius)
        pass

    def __str__(self):
        return f"{self.__class__.__name__}(data={str(self.data)})"
