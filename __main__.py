from src.drawables.circle import Circle
from src.drawables.line import Line
from src.drawables.polyline import PolyLine
from src.drawables.ellipse import Ellipse
from src.drawables.fromVFF import fromVFF
from src.drawables.map import Map
from src.drawables.deformto import deformTo

from src.VFF.bezier import Bezier
from src.VFF.sphere import Sphere
from src.VFF.plane import Plane
from src.VFF.blade import Blade
from src.VFF.__Bezier__ import Bezier as B2
from src.VFF.linend import LineND
from src.VFF.concat import Concat
from src.VFF.add import Add
from src.VFF.multiply import Multiply
from src.VFF.projection import Projection
from src.VFF.constant import Constant
from src.VFF.scale import Scale
from src.VFF.vectorDeformationVFF import vectorDeformationVFF
from src.VFF.vectorDeformationMany import vectorDeformationMany
from src.VFF.split import Split
from src.VFF.partitionVFFCircle import partitionVFFCircle

from src.typeclass.canvas import Canvas, A0, A1, A2, A3, A4, profilePhoto, squareImage, images, story

from src.sample_method.linspace import Linspace
from src.sample_method.beta import Beta

from src.canvas.canvas import Canvas

from canvas.boundedThreeBezier import boundedThreeBezier
from canvas.ManyPolygonBezierSpine import ManyPolygonBezierSpine
from canvas.grid import grid
from canvas.gridDeformationPerlinNoise import gridDeformationPerlinNoise
from canvas.partitionManyCirclesRotate import partitionManyCirclesRotate
from canvas.deformCirclesR3 import deformCirclesR3
from canvas.partitionManyLine import partitionManyLine
from canvas.circleInversion import circleInversion

from functools import partial
import numpy as np
from math import cos, sin, pi
## import cv2
## from svglib.svglib import svg2rlg
## from reportlab.graphics import renderPM
import os
from random import seed, randrange, choice
from os.path import isfile, join

def composition():
    store = {}
    a, b = randrange(10000000), randrange(10000000)
    c, d, e = randrange(3,5), randrange(3,5), randrange(3,5)
    f = partitionManyLine.construct_random(a,c)
    nf = partitionManyLine.construct_random(a,d)
    g = partitionManyCirclesRotate.construct_random(b,e)
    h = lambda m: gridDeformationPerlinNoise(m, 10, 10, 5, 20)
    ql = grid(0,0,280,280).horizontal()
    q = grid(0,0,140,140)

    l = nf(f(ql))

    construct = circleInversion(circleInversion(circleInversion(l, [100,500,500]), [600,600,1000]), [0,400,300])

    construct.write_to_file("")

    return construct

def deform(m = grid(1, 1, 750, 500, Linspace(500), Linspace(500)).vertical()):
    steps, seednum = randrange(9,13), randrange(10000000)
    l = deformCirclesR3.construct_random(m, seednum, steps)
    l.write_to_file("")
    return l

## Consider making a function that runs random Canvas with arguments. Run daily. Look to write
## fit to canvas wrapper canvas. Perhaps we should look into databasing each canvas.
