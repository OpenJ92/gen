from src.drawables.circle import Circle
from src.drawables.line import Line
from src.drawables.polyline import PolyLine
from src.drawables.ellipse import Ellipse
from src.drawables.fromVFF import fromVFF
from src.drawables.map import Map
from src.drawables.deformto import deformTo

from src.VFF.bezier import Bezier
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

from src.typeclass.canvas import Canvas, A0, A1, A2, A3, A4

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

from functools import partial
import numpy as np
from math import cos, sin, pi
import cv2
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
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
    q = grid(0,0,140,140)
    ql = grid(0,0,140,140)

    store[f"{a}_{b}"] = [nf(g(f(ql))), nf(f(g(q)))]
    nf(g(f(ql))).write_to_file("")
    nf(f(g(q))).write_to_file("")
    return store

def deform():
    a, b, c = [randrange(1, 1000000) for _ in range(3)]
    d, e, f = [randrange(1, 4) for _ in range(3)]
    steps = randrange(2,13)
    print(a, b, c, d, e, f, steps)
    deformCirclesR3(a, b, c, d, e, f, steps).write_to_file("")

## Consider making a function that runs random Canvas with arguments. Run daily. Look to write
## fit to canvas wrapper canvas. Perhaps we should look into databasing each canvas.
