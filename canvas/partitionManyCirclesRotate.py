from src.typeclass.canvas import Canvas
from src.typeclass.many import Many

from src.VFF.partitionVFFCircle import partitionVFFCircle
from src.VFF.translate import Translate
from src.VFF.rotate import Rotate

from src.drawables.fromVFF import fromVFF

from src.sample_method.linspace import Linspace

from random import seed, randrange, choice
from functools import cache

class partitionManyCirclesRotate(Many, Canvas):
    def __init__(self, many, data):
        self.ynam = many
        self.data = data

    @classmethod
    def from_file(cls, file):
        # make class that can take the file name and reconstruct use re
        pass

    @classmethod
    def save_location(cls):
        # save location for entities of the outermost canvas
        pass

    # Look to submit multivector to sample for variable boundaries. 
    #   ie. cx ^ cy ^ r ^ theta
    @classmethod
    # Ultimatly, we're looking to put together the vertical and horizontal sample
    # together so as to achieve the given 
    def construct_random(cls, randseed, circlecount):
        seed(randseed)
        constructed_data = []
        while circlecount > 0:
            cx, cy = (randrange(0,140), randrange(0,140))
            r = randrange(20, 60)
            theta = randrange(-180, 180)
            constructed_data = [*constructed_data, cx, cy, r, theta]
            circlecount = circlecount - 1

        return lambda many: cls(many, constructed_data)

    @cache
    def many(self):
        element = {'inside':[], 'outside':[]}
        ynam = self.ynam.many()
        data = self.data

        while data:
            # unpack data
            cx, cy, radius, theta, *data = data

            # Apply partition to many
            ynam = list(map(lambda x: partitionVFFCircle(cx, cy, radius, x).many(), ynam))

            # Place partitioned objects into containers.
            for elem in ynam:
                element['inside'] = [*element['inside'], *elem['inside']]
                element['outside'] = [*element['outside'], *elem['outside']]

            # construct functions to apply to partitions
            rot = lambda x : Translate(cx, cy, Rotate(theta, Translate(-cx, -cy, x)))

            # Apply functions to each partition
            element['inside'] = list(map(rot, element['inside']))

            # Unpack transformed elements back into many for next partition
            ynam = [*element['inside'], *element['outside']]

            # clear storage
            element = {'inside': element['outside'], 'outside': []}
            # element = {'inside': [], 'outside': []}


        return ynam

    def drawable(self):
        return list(map(lambda x: fromVFF(x, Linspace(70)), self.many()))

    def __str__(self):
        return f"{self.__class__.__name__}(many={str(self.ynam)}, data={self.data})"
