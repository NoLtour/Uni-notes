from ast import arg
from cmath import isnan, nan
import matplotlib.pyplot as plt

import math

import numpy

import airfoilsim

class Graphboi:
    def addPoint(this, nX, nY):
        this.x.append( nX );
        this.y.append( nY )

    def addPoints(this, nX, nY):
        if ( len( nX ) != len( nY ) ):
            print("bad")
            return;
        
        for cNX in nX:
            this.x.append( cNX );
        
        for cNY in nY:
            this.y.append( cNY );

    def plot(this, showLine = True, showPoints = False):
        if ( showLine ):
            if ( showPoints ):
                plt.plot( this.x, this.y, marker='x' );
            else:
                plt.plot( this.x, this.y );
        else:
            if ( showPoints ):
                plt.plot( this.x, this.y, marker='x', linestyle="" );
        
        


    def render(this, showLine = True, showPoints = False):
        this.plot(showLine, showPoints)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()
    
    def genPointsFromFunc( this, function, minX = 0, maxX = 10, increment = 0.025 ):
        i = minX
        while (i<maxX):
            this.addPoint( i, function( i ) )

            i += increment

    def __init__(this):
        this.x = []
        this.y = []


def basicPoly( x ):

    return x**2 + 2*x + 1

class BezCurve:

    def C( this, n, i ):
        return math.factorial( n )/( math.factorial(i) * math.factorial(n-i) )

    def __init__(this, pointCount = 3):
        this.points = []
        this.weights = []
        this.pointCount = 0
            
        this.graphXs = []
        this.graphYs = []

        this.maxX = 0
        this.maxY = 0
        this.minX = 0
        this.minY = 0

        this.showPoints = False

        this.pointCount = pointCount

        for i in range(0, pointCount):
            this.points.append( [ i, i%2 ] )
            this.weights.append( 1 )


    def setPoint( this, n, x, y, weight = -1 ):
        this.points[n][0] = x
        this.points[n][1] = y
        if ( weight > 0 ):
            this.weights[n] = weight
        
    def addPoint( this, x, y, weight = -1 ):
        this.insertPoint( this.pointCount, x, y, weight )
    
    # inserts point before element at given n value
    def insertPoint( this, n, x, y, weight = -1 ):
        
        if (n == this.pointCount):
            this.points.append([0,0])
        else:
            this.points.insert(n, [0,0])
        
        this.pointCount+=1;

        this.points[n][0] = x
        this.points[n][1] = y

        this

        if ( weight > 0 ):
            this.weights[n] = weight


    def setWeight( this, n, weight ):
        this.weights[n] = weight

    def updateRange( this ):
        this.maxX = this.points[0][0]
        this.minX = this.points[0][0]
        this.maxY = this.points[0][1]
        this.minY = this.points[0][1]

        for point in this.points:
            if ( point[0] > this.maxX ):
                this.maxX = point[0]
            elif ( point[0] < this.minX ):
                this.minX = point[0]

            if ( point[1] > this.maxY ):
                this.maxY = point[1]
            elif ( point[1] < this.minY ):
                this.minY = point[1]
        return


    def genGraphPoints( this ):
        this.graphXs = []
        this.graphYs = []

        this.updateRange()

        SAMPLES = 150
        increment = (this.maxX-this.minX)/SAMPLES
        
        t = 0

        pWM = []
        #for weight in this.weights:
        #    pWM.append( weight *  )

        while ( t <= 1 ):
            x = 0
            y = 0

            for i in range(0, this.pointCount ):
                cWFuncOup = ( this.C( this.pointCount-1, i ) * ( t**(i) ) * ( ( 1-t )**(this.pointCount-(i+1)) ) ) 

                x += this.points[i][0] * cWFuncOup
                y += this.points[i][1] * cWFuncOup

            this.graphXs.append( x )
            this.graphYs.append( y )

            t += 1/SAMPLES

        return 

    def plot(this):
        this.genGraphPoints()
        graph = Graphboi()

        this.genGraphPoints()
        graph.addPoints( this.graphXs, this.graphYs )
        graph.plot()

    def render(this):
        this.plot()
        graph = Graphboi()
        graph.render()

class SplineGroup:

    def __init__(this, startX=0, startY=0, endX=1, endY=1):
        this.bezCurves = []

        fCurve = BezCurve( 3 );

        fCurve.setPoint( 0, startX, startY )
        fCurve.setPoint( 1, startX, endY)
        fCurve.setPoint(2, endX, endY)

        this.bezCurves.append( fCurve );

    def addSpline(this, inpCurve=-1 ):
        if ( inpCurve == -1 ):
            this.bezCurves.append(BezCurve(3))
        
        else:
            this.bezCurves.append( inpCurve )

        this.connectAllSplines()

    def connectSplines( this, spline1, spline2 ):
        spline2.points[0] = spline1.points[spline1.pointCount-1]

    def connectSplinesCont( this, spline1, spline2 ):
        this.connectSplines( spline1, spline2 )
        
        commonPoint = spline2.points[0]
        spline1RPoint = spline1.points[spline1.pointCount-2]
        gradPoint = spline2.points[1]
        spline2RPoint = spline2.points[2]

        if ( (commonPoint[0]-spline1RPoint[0]) != 0 ):

            m = (commonPoint[1]-spline1RPoint[1])/(commonPoint[0]-spline1RPoint[0])
            c = commonPoint[1] - (m*commonPoint[0])

            gradPoint[0] = (spline2RPoint[0]+(m*(spline2RPoint[1]-c)))/(1+(m**2))
            gradPoint[1] = (gradPoint[0]*m) + c

            #tmp = Graphboi()
            #tmp.addPoints( [ spline1RPoint[0], commonPoint[0], gradPoint[0], spline2RPoint[0],1,0,0 ], [ spline1RPoint[1], commonPoint[1], gradPoint[1], spline2RPoint[1],0,0,1 ] )
            #tmp.render()

        else:
            gradPoint[0] = commonPoint[0]
            gradPoint[1] = spline2RPoint[1]

        return;

    def connectAllSplinesCont(this):
        for i in range(0, len( this.bezCurves ) - 1 ):
            this.connectSplinesCont( this.bezCurves[i], this.bezCurves[i+1] )

    def connectAllSplines(this):
        for i in range(0, len( this.bezCurves ) - 1 ):
            this.connectSplines( this.bezCurves[i], this.bezCurves[i+1] )

    def render(this):
        graph = Graphboi()

        for curve in this.bezCurves:
            curve.genGraphPoints()
            graph.addPoints( curve.graphXs, curve.graphYs )

        graph.render()

class Shape:
    def __init__(this):
        this.points = []

    def addPoint(this, x, y):
        this.points.append( [x, y] )

    def render(this):
        pointCount = len(this.points)

        if ( pointCount <= 2 ):
            return

        sG = SplineGroup( this.points[0][0], this.points[0][1], this.points[1][0], this.points[1][1] )

        for i in range(1, pointCount):
            cSpline = BezCurve(3)

            cPoint = this.points[i]
            nPoint = this.points[(i+1)%pointCount]

            cSpline.setPoint( 0, cPoint[0], cPoint[1] )
            cSpline.setPoint( 2, nPoint[0], nPoint[1] )

            sG.addSpline( cSpline )

        sG.connectAllSplinesCont()

        sG.render()

class AirFoil:
    def __init__(this):
        this.LHRatio = 2
        this.TBRatio = 1.5
        this.PLRatio = 0.3
        this.FMRatio = 0.5


        this.pointsTop = []
        this.pointsBot = []

        this.topBez = 0;
        this.botBez = 0

        this.showPoints = False

    def displayPoints( this, points ):
        graph = Graphboi()
        for point in points:
            graph.addPoint( point[0], point[1] )
        graph.plot( True, True );

    def generatePoints(this):
        length = 1;
        height = length/this.LHRatio

        minHeight = height/(1+this.TBRatio)
        maxHeight = height - minHeight

        frontMinH = height * this.FMRatio / 2
        frontMaxH = height * this.FMRatio / 2


        peakLength = this.PLRatio * length

        this.pointsTop = [
            [0, 0],
            [0, frontMaxH],
            [peakLength, maxHeight],
            [length, 0]
        ]
        
        this.pointsBot = [
            [0, 0],
            [0, -frontMinH],
            [peakLength, -minHeight],
            [length, 0]
        ]

        if ( this.showPoints ):
            this.displayPoints( this.pointsBot )
            this.displayPoints( this.pointsTop )

    def render( this ):
        this.generateCurves()
        this.topBez.plot()
        this.botBez.render()

    def generateCurves( this ):
        this.generatePoints()
        
        this.topBez = BezCurve(4)
        this.botBez = BezCurve(4)

        for i in range( 0, 4 ):
            this.topBez.setPoint( i, this.pointsTop[i][0], this.pointsTop[i][1] )
            this.botBez.setPoint( i, this.pointsBot[i][0], this.pointsBot[i][1] )

        this.topBez.genGraphPoints()
        this.botBez.genGraphPoints()
    
    def generateAsPoints( this ):
        this.generateCurves()

        points = [ [1, 0] ]
        
        allPointXs = list(reversed( this.botBez.graphXs )) + this.topBez.graphXs
        allPointYs = list(reversed( this.botBez.graphYs )) + this.topBez.graphYs

        for i in range(1, len(allPointXs)):
            if ( allPointXs[i] != allPointXs[i-1] or allPointYs[i] != allPointYs[i-1] ):
                points.append( [allPointXs[i], allPointYs[i]] )
        
        return points + [ [1, 0] ]

    def getCoefficients( this, angle ):
        pointz = this.generateAsPoints();

        V  = 15
        c  = 0.5 
        nu = 1.516e-5

        Re = V * c / nu

        try:
            outs = airfoilsim.airfoilsim( numpy.array( pointz ), angle, Re )
        except:
            return -1;

        return [ outs[0], outs[1] ];


tmp = AirFoil()
tmp.showPoints = False

tmp.LHRatio = 6.9
tmp.TBRatio = 2.5
tmp.FMRatio = 0.45
tmp.PLRatio = 0.3

TARGET_CL = 2

BOUNDS      = [ [-3, 12], [2, 16], [0.1, 6], [0.05, 0.95], [0.05, 0.95] ]
INIT_VALUES = [6, 6.9, 2.5, 0.45, 0.31]

def foilFronArgs(args):
    foil = AirFoil();
    foil.LHRatio = args[1]
    foil.TBRatio = args[2]
    foil.FMRatio = args[3]
    foil.PLRatio = args[4]

    return foil;

def calcScore( args ):
    foil = foilFronArgs( args )

    for i in range( 0, len(BOUNDS) ):
        if ( args[i] < BOUNDS[i][0] or args[i] > BOUNDS[i][1] ):
            print("bad bounds")
            return 10000

    oups = foil.getCoefficients( args[0] )
    print(args)

    if ( oups == -1 or isnan( oups[0] ) or isnan( oups[1] ) ):
        print(oups)
        return 10000
    
    print( oups )
    score = (20*((TARGET_CL-oups[0])**2))  + oups[1]
    print( score )

    return score

import scipy.optimize as sp


oups = sp.minimize( calcScore, INIT_VALUES, method="COBYLA", bounds=BOUNDS, options={'maxiter':130} )#, 

print( oups )

foilFronArgs( oups["x"] ).render()

print( oups )

"""
#tmp.render();
lmao = Graphboi()

allPs = [ [], [] ]

pointz = tmp.generateAsPoints();

for point in pointz:
    allPs[0].append( point[0] )
    allPs[1].append( point[1] )
    lmao.addPoint( point[0], point[1] )

#lmao.render()

V  = 15
c  = 0.5 
nu = 1.516e-5

Re = V * c / nu

outs = airfoilsim.airfoilsim( numpy.array( pointz ), 0, Re )
"""
print(tmp.getCoefficients())

# Cl 0.20971

"""
y = Shape()

y.addPoint(1,1)
y.addPoint(2.2,3)
y.addPoint(3,1)
y.addPoint(5,1)
y.addPoint(2,0)

y.render()


x = SplineGroup( 0, 0, 1, 1 )
x.bezCurves[0].points[1] = [0.3, 0.8]

nCurve = BezCurve();

nCurve.setPoint(2, 2, 1)

x.addSpline( nCurve )

x.connectAllSplinesCont()

x.render()

tmp = BezCurve( 4 )


tmp.setPoint( 0, 6, -4 )

tmp.setPoint( 1, 6, 2 )
tmp.setPoint( 2, 4, 2 )
tmp.setPoint( 3, 3, 6 )



tmp.render()
"""
print("")

