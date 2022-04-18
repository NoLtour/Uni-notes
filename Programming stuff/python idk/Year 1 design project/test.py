import airfoilsim

import splineLibs as sl
import numpy as np

def withoutLast( inpList ):
    if ( len( inpList ) < 1 ):
        return []
    return inpList[ :len( inpList ) - 2 ]

"""

   X     X
X                   X
---------------------
X                   X  
   X         X

"""

CHORD_LENGTH  = 0.4
MIN_THICKNESS = 0.006/CHORD_LENGTH

class RestrictedFoil:

    def __init__( this, inpValues = [0.04,0.2,0.04,0.3,10,65,10,85,0.15,0.07,0.04,0.1,0.07,0.03,0] ):
        this.sT_TF = inpValues[0] # 0.1
        this.sT_TB = 0#inpValues[1] #0.2
        this.sT_BF = inpValues[2] #0.1
        this.sT_BB = 0#inpValues[3] #0.3

        this.sTA_TF = inpValues[4] #10
        this.sTA_TB = 0# inpValues[5] #65
        this.sTA_BF = inpValues[6] #10
        this.sTA_BB = 0# inpValues[7] #85

        this.sH_T1 = inpValues[8] #0.2
        this.sH_T2 = inpValues[9] #0.3
        this.sH_T3 = inpValues[10] #0.1

        this.sH_B1 = inpValues[11] #0.2
        this.sH_B2 = inpValues[12] #0.3
        this.sH_B3 = inpValues[13] #0.1

        this.sAngle = inpValues[14] #0

        this.generatePoints();

        this.calculateCoefficients()
    
    def generatePoints( this ):
        topCurve = sl.BezCurve( 7 )
        botCurve = sl.BezCurve( 7 )

        # Top first airfoil point
        tmp = this.getCircPoint( MIN_THICKNESS, 0, 180 - this.sTA_TF )
        topCurve.setPoint( 0, 0, 0 )

        # Bot first airfoil point
        tmp = this.getCircPoint( MIN_THICKNESS, 0, this.sTA_BF - 180 )
        botCurve.setPoint( 0, 0, 0 )

        # Top last airfoil point
        tmp = this.getCircPoint( 1 - MIN_THICKNESS, 0, this.sTA_TB )
        topCurve.setPoint( 6, tmp[0], tmp[1] )

        # Bot last airfoil point
        tmp = this.getCircPoint( 1 - MIN_THICKNESS, 0, -this.sTA_BB )
        botCurve.setPoint( 6, tmp[0], tmp[1] )

        # Top Second airfoil point
        tmp = this.getTangPoint( MIN_THICKNESS, 0, 180 - this.sTA_TF, -this.sT_TF )
        topCurve.setPoint( 1, 0, this.sT_TF )
        
        # Bot Second airfoil point
        tmp = this.getTangPoint( MIN_THICKNESS, 0, this.sTA_BF - 180, this.sT_BF )
        botCurve.setPoint( 1, 0, -this.sT_BF )

        # Top Second last airfoil point
        tmp = this.getTangPoint( 1 - MIN_THICKNESS, 0, this.sTA_TB, this.sT_TB )
        topCurve.setPoint( 5, tmp[0], tmp[1] )

        # Bot Second last airfoil point
        tmp = this.getTangPoint( 1 - MIN_THICKNESS, 0, -this.sTA_BB, -this.sT_BB )
        botCurve.setPoint( 5, tmp[0], tmp[1] )

        MID_SEP = 0.37

        # Top mid 3 points
        topCurve.setPoint( 2, 0.5 - MID_SEP, this.sH_T1 )
        topCurve.setPoint( 3, 0.5          , this.sH_T2 )
        topCurve.setPoint( 4, 0.5 + MID_SEP, this.sH_T3 )

        # Bot mid 3 points
        botCurve.setPoint( 2, 0.5 - MID_SEP, -this.sH_B1 )
        botCurve.setPoint( 3, 0.5          , -this.sH_B2 )
        botCurve.setPoint( 4, 0.5 + MID_SEP, -this.sH_B3 )

        #topCurve.render( True )

        #botCurve.render( True )

        topCurve.genGraphPoints()
        botCurve.genGraphPoints()

        frontCurve = [[],[]] # this.genCirclePoints( MIN_THICKNESS, 0, 180 - this.sTA_TF,  this.sTA_BF - 180 )
        backCurve  = this.genCirclePoints( 1-MIN_THICKNESS, 0, -this.sTA_BB, this.sTA_TB )

        topCurve.graphXs.reverse()
        topCurve.graphYs.reverse()

        this.finalXs = withoutLast( backCurve[0] ) + withoutLast( topCurve.graphXs ) + withoutLast( frontCurve[0] ) + ( botCurve.graphXs )
        this.finalYs = withoutLast( backCurve[1] ) + withoutLast( topCurve.graphYs ) + withoutLast( frontCurve[1] ) + ( botCurve.graphYs ) 

        tmp = sl.Graphboi()
        tmp.addPoints( this.finalXs, this.finalYs )
        tmp.render()

    def calculateCoefficients( this ):
        allPoints = []

        lX = -1;
        lY = -1

        MIN_DIF = 0.001

        for i in range( len(this.finalXs) ):
            cX = this.finalXs[i]
            cY = this.finalYs[i]
            if ( abs( cX - lX ) > MIN_DIF or abs(cY - lY) > MIN_DIF  ):
                allPoints.append( 
                    [ this.finalXs[i], this.finalYs[i] ]
                )
                lX = cX
                lY = cY

        
        Re = 15 * CHORD_LENGTH * 1.516e-5

        airfoilsim.airfoilsim( np.array( allPoints ), this.sAngle, Re )

        try:
            oup = airfoilsim.airfoilsim( np.array( allPoints ), this.sAngle, Re );
        except:
            oup = [ 0, 100000 ]

        this.cL = oup[0]
        this.cD = oup[1]

        

    def genCirclePoints( this, xCentre, yCentre, startAngle, endAngle, radius = MIN_THICKNESS ):
        xPoints = []
        yPoints = []

        while ( startAngle > endAngle ):
            endAngle += 360

        for cAngle in range( startAngle, endAngle ):
            if ( cAngle%4 == 0 or cAngle == startAngle or cAngle == endAngle ):
                radAngle = cAngle*3.142/180
                xPoints.append( xCentre + ( radius * np.cos( radAngle ) ) )
                yPoints.append( yCentre + ( radius * np.sin( radAngle ) ) )

        return [ xPoints, yPoints ]

    def getCircPoint( this, xCentre, yCentre, angle, radius = MIN_THICKNESS ):
        angle = angle*3.142/180
        x = xCentre + ( radius * np.cos( angle ) )
        y = yCentre + ( radius * np.sin( angle ) )
        return [x, y]

    def getTangPoint( this, xCentre, yCentre, angle, tangentLength, radius = MIN_THICKNESS  ):
        angle = angle*3.142/180
        x = xCentre + (radius * np.cos(angle)) - ( tangentLength * np.sin( angle ) )
        y = yCentre + (radius * np.sin(angle)) + ( tangentLength * np.cos( angle ) )
        return [x, y]

    

tmp = RestrictedFoil(  )

print("")
    