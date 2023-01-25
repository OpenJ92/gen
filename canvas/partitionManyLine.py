from src.typeclass.canvas import Canvas
from src.typeclass.many import Many

from src.VFF.partitionVFFLine import partitionVFFLine
from src.VFF.translate import Translate

from src.drawables.fromVFF import fromVFF
from src.drawables.circle import Circle

from src.sample_method.linspace import Linspace

from random import seed, randrange, choice
from functools import cache

class partitionManyLine(Many, Canvas):
    # Look to submit multivector to sample for variable boundaries. 
    #   ie. cx ^ cy ^ dx ^ dy ^ mag
    @classmethod
    def construct_random(cls, randseed, linecount):
        seed(randseed)
        constructed_data = []
        while linecount > 0:
            # Partition our object
            cx = randrange(0, 140)
            cy = randrange(0, 140)
            dx = choice([0,1])
            dy = int(not dx)
            mag = choice([-1,1])*randrange(10,50)
            constructed_data = [*constructed_data, cx, cy, dx, dy, mag]
            linecount = linecount - 1

        return lambda many: cls(many, constructed_data)

    def __init__(self, many, data):
        self.ynam = many
        self.data = data

    @cache
    def many(self):
        element = {'inside':[], 'outside':[]}
        ynam = self.ynam.many()
        data = self.data

        while data:
            # unpack data
            cx, cy, dx, dy, mag, *data = data

            # Apply partition to many
            ynam = list(map(lambda x: partitionVFFLine(cx, cy, dx, dy, x).many(), ynam))

            # Place partitioned objects into containers.
            for elem in ynam:
                element['inside'] = [*element['inside'], *elem['inside']]
                element['outside'] = [*element['outside'], *elem['outside']]

            # construct functions to apply to partitions
            intra = lambda x : Translate(mag*dy/2, mag*dx/2, x)
            outra = lambda x : Translate(-1*mag*dy/2, -1*mag*dx/2, x)
            sepintra = lambda x : Translate(-1*5*dx/2, -1*5*dy/2, x)
            sepoutra = lambda x : Translate(5*dx/2,5*dy/2, x)
            # sepintra = lambda x : x
            # sepoutra = lambda x : x

            # Apply functions to each partition
            element['inside'] = list(map(lambda x: intra(sepintra(x)), element['inside']))
            element['outside'] = list(map(lambda x: outra(sepoutra(x)), element['outside']))

            # Unpack transformed elements back into many for next partition
            ynam = [*element['inside'], *element['outside']]

            # clear storage
            # element = {'inside': element['outside'], 'outside':[]}
            element = {'inside': [], 'outside':[]}

        return ynam

    def drawable(self):
        return list(map(lambda x: fromVFF(x, Linspace(500)), self.many()))

    def __str__(self):
        return f"{self.__class__.__name__}(many={str(self.ynam)}, data={self.data})"
