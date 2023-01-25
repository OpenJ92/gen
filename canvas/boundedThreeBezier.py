from src.typeclass.canvas import Canvas
from src.typeclass.drawable import Drawable

from src.drawables.deformto import deformTo
from src.drawables.circle import Circle
from src.drawables.fromVFF import fromVFF
from src.drawables.line import Line

from src.VFF.bezier import Bezier

from src.sample_method.linspace import Linspace
from src.sample_method.beta import Beta

from numpy import array

class boundedThreeBezier(Canvas):
    def __init__( self

                , x1, y1
                , x2 ,y2
                , x3, y3

                , p11 = 50  , p12 = 150
                , p51 = 100 , p52 = 40
                , p21 = 150 , p22 = 30
                , p31 = 150 , p32 = 200
                , p41 = 250 , p42 = 175
                , p61 = 200 , p62 = 20

                , b1sampl     = Linspace(500)
                , b2sampl     = Linspace(500)
                , b3sampl     = Linspace(500)

                , d1samplPoly = Linspace(100)
                , d1samplvff  = Linspace(100)
                , d2samplPoly = Linspace(100)
                , d2samplvff  = Linspace(100)
                , d3samplPoly = Linspace(20)
                , d3samplvff  = Beta(.8,.125,100,42)
                , d4samplPoly = Linspace(20)
                , d4samplvff  = Beta(.8,.125,100,43)
                , d5samplPoly = Linspace(20)
                , d5samplvff  = Beta(.8,.125,100,44)

                ):

        self.x1 = x1 ; self.y1 = y1
        self.x2 = x2 ; self.y2 = y2
        self.x3 = x3 ; self.y3 = y3

        self.p11 = p11 ; self.p12 = p12
        self.p21 = p21 ; self.p22 = p22
        self.p31 = p31 ; self.p32 = p32
        self.p41 = p41 ; self.p42 = p42
        self.p51 = p51 ; self.p52 = p52
        self.p61 = p61 ; self.p62 = p62

        self.b1sampl     = b1sampl
        self.b2sampl     = b2sampl
        self.b3sampl     = b3sampl

        self.d1samplPoly = d1samplPoly
        self.d1samplvff  = d1samplvff
        self.d2samplPoly = d2samplPoly
        self.d2samplvff  = d2samplvff
        self.d3samplPoly = d3samplPoly
        self.d3samplvff  = d3samplvff
        self.d4samplPoly = d4samplPoly
        self.d4samplvff  = d4samplvff
        self.d5samplPoly = d5samplPoly
        self.d5samplvff  = d5samplvff

    def drawable(self):
        c1 = (self.x1,self.y1)
        c2 = (self.x2,self.y2)
        c3 = (self.x3,self.y3)

        cir1 = Circle(*c1, 1)
        cir2 = Circle(*c2, 1)
        cir3 = Circle(*c3, 1)

        cir1b = Circle(*c1, 10)
        cir2b = Circle(*c2, 10)
        cir3b = Circle(*c3, 10)

        p1 = (self.p11 , self.p12)
        p2 = (self.p21 , self.p22)
        p3 = (self.p31 , self.p32)
        p4 = (self.p41 , self.p42)
        p5 = (self.p51 , self.p52)
        p6 = (self.p61 , self.p62)

        b1 = Bezier(array(p1),array(p5),array((c1,c2)).T)
        b2 = Bezier(array(p3),array(p2),array((c2,c3)).T)
        b3 = Bezier(array(p4),array(p6),array((c1,c3)).T)

        d1 = deformTo(b1, b2, self.d1samplPoly, self.d1samplvff)
        d2 = deformTo(b2, b3, self.d2samplPoly, self.d2samplvff)
        d3 = deformTo(cir3, cir3b, self.d3samplPoly, self.d3samplvff)
        d4 = deformTo(cir2, cir2b, self.d4samplPoly, self.d4samplvff)
        d5 = deformTo(cir1, cir1b, self.d5samplPoly, self.d5samplvff)

        return [ cir1, cir2, cir3
               , Line(*p1, *p3, stroke = "red", stroke_width=".4")
               , Line(*p3, *p4, stroke = "red", stroke_width=".4")
               , Line(*p5, *p2, stroke = "black", stroke_width=".4")
               , Line(*p2, *p6, stroke = "black", stroke_width=".4")
               , fromVFF(b1, self.b1sampl)
               , fromVFF(b2, self.b2sampl)
               , fromVFF(b3, self.b3sampl)
               , d1, d2, d3, d4, d5
               ]
