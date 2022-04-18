import matplotlib.pyplot as plt
import airfoilsim

import math

import numpy

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

        SAMPLES = 80
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

    def render(this, showPoints = False):
        this.plot()
        graph = Graphboi()

        if ( showPoints ):
            for point in this.points:
                graph.addPoint( point[0], point[1] )

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
    def __init__(this, defPoints = [ 0.1, 0.13, 0.2, 0.3, 0.15, 0.12, 0.6, 0.1, 0.6, 0.1 ]):
        #this.LHRatio = 2
        #this.TBRatio = 1.5
        #this.TPLRatio = 0.3
        #this.BPLRatio = 0.4
        #this.FMRatio = 0.5
        this.defPoints = defPoints# [ 0.1, 0.13, 0.2, 0.3, 0.15, 0.12, 0.6, 0.1, 0.6, 0.1 ]

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
        
        fTy = this.defPoints[0]
        fBy = this.defPoints[1]

        t1x = this.defPoints[2]
        t1y = this.defPoints[3]

        t2x = this.defPoints[8]
        t2y = this.defPoints[9]
        
        b1x = this.defPoints[4]
        b1y = this.defPoints[5]

        b2x = this.defPoints[6]
        b2y = this.defPoints[7]

        this.pointsTop = [
            [0, 0],
            [0, fTy],
            [t1x, t1y],
            [t2x, t2y],
            [length, 0]
        ]
        
        this.pointsBot = [
            [0, 0],
            [0, -fBy],
            [b1x, -b1y],
            [b2x, -b2y],
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
        
        this.topBez = BezCurve(5)
        this.botBez = BezCurve(5)

        for i in range( 0, 5 ):
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

class Optimiser:

    def __init__( this, initValues = [ 0.1, 0.13, 0.2, 0.3, 0.15, 0.12, 0.6, 0.1, 0.6, 0.1 ] ):
        this.bValues = initValues;
        this.nValues = this.bValues.copy(); #[ 6.9, 10, 0.8, 0.3, 0.7 ];
        this.bScore  = this.testFoil( this.createAirfoil( this.bValues ), True );
        this.nScore  = 0;

        this.tShiftIndex = 0
        this.shifts = []
        for i in range(0, len(this.bValues)):
            this.shifts.append([
                0, # scoreChange
                0, # shift value
            ])

    def renderBest( this ):
        tmp = this.createAirfoil( this.bValues )
        tmp.showPoints = True;
        tmp.render()

    def createAirfoil( this, values ):
        nFoil = AirFoil();
        nFoil.defPoints = values.copy();
        
        return nFoil;

    def testFoil( this, foil, printValues = False ):
        pointz = foil.generateAsPoints();

        V  = 15
        c  = 0.5 
        nu = 1.516e-5

        Re = V * c / nu

        outs = airfoilsim.airfoilsim( numpy.array( pointz ), 0, Re )

        try:
            outs = airfoilsim.airfoilsim( numpy.array( pointz ), 0, Re )
            if ( printValues ):
                print( "cL:",outs[0],"cD:",outs[1] )
        except:
            print("failed")
            return 0

        return this.generateScore( outs )
    
    def updateBest( this ):
        this.shifts[ this.tShiftIndex ][0] = this.nScore - this.bScore;

        if ( this.nScore > this.bScore ):
            this.bScore = this.nScore
            this.bValues = this.nValues
    
    def genNValues( this ):
        this.tShiftIndex = (1 + this.tShiftIndex)%len(this.bValues)
        this.nValues = this.bValues.copy()

        sChange = this.shifts[ this.tShiftIndex ][0]
        shiftVal = this.shifts[this.tShiftIndex][1]

        if ( sChange > 0 ):
            shiftVal *= 1.6
        elif ( abs( shiftVal )  < 0.000001 ):
            shiftVal = 0.1
        else:
            shiftVal *= -0.3
        
        this.shifts[this.tShiftIndex][1] = shiftVal
        this.nValues[ this.tShiftIndex ] += shiftVal
        
    def iterate( this, count ):
        for i in range(0, count):
            this.genNValues()
            
            this.nScore = this.testFoil( this.createAirfoil( this.nValues ), True )

            print( "bScore:",this.bScore,"\tnScore:",this.nScore, "\tnValues:",this.nValues, "\tshifts:",this.shifts )

            this.updateBest()
            

    def generateScore( this, simOuts ):
        cL = simOuts[0]
        cD = simOuts[1]

        eM = 1;

        if ( cL < 0 ):
            eM = -1

        cLSc = (abs(cL-0.5)**-2)
        if ( cLSc >2000 ):
            cLSc = 2000

        return (1/(cD)) + cLSc  #((cL-(cD*3))**2)/(cD+0.001)

#(AirFoil()).render()

opt = Optimiser( [ 0.05, 0.05, 0.2, 0.1, 0.2, 0.05, 0.66, 0.04, 0.66, 0.04 ] );

print( "score:", opt.bScore )

for i in range(0, 8):
    opt.renderBest()

    opt.iterate( 15 )


opt.renderBest()

opt.iterate( 50 )

opt.renderBest()

opt.iterate( 100 )

opt.renderBest()

print("");
"""

tmp = AirFoil()
tmp.showPoints = True

tmp.LHRatio = 6.9
tmp.TBRatio = 10
tmp.FMRatio = 0.8
tmp.TPLRatio = 0.3
tmp.BPLRatio = 0.7

#tmp.render();
lmao = Graphboi()

allPs = [ [], [] ]

pointz = tmp.generateAsPoints();

tmp.render()

for point in pointz:
    allPs[0].append( point[0] )
    allPs[1].append( point[1] )
    lmao.addPoint( point[0], point[1] )

#lmao.render()

import airfoilsim

V  = 15
c  = 0.5 
nu = 1.516e-5

Re = V * c / nu

outs = airfoilsim.airfoilsim( numpy.array( pointz ), 0, Re )

print(outs)

# Cl 0.20971


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

print("")
"""
