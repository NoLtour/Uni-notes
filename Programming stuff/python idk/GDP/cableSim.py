
import numpy as np
import matplotlib.pyplot as plt


class Pulley:
    """
        x_s : seperation between pulley points
        DpL : Drag per length
        WpL : Weight per length
        pW  : point weight
        L1  : Length pulley 1
        L2  : Length pulley 2
        res : Samples per length
    """
    def __init__(this, x_s, DpL, WpL, pW, L1, L2, res):
        this.x_s = x_s
        this.DpL = DpL
        this.WpL = WpL
        this.pW  = pW
        this.L1  = L1
        this.L2  = L2
        
        this.m1 = 1 + int(L1/res)
        this.m2 = 1 + int(L2/res)

        this.l1 = this.L1/this.m1
        this.l2 = this.L2/this.m2

        pointLength = 0.0001

        this.lengs = np.concatenate([ np.ones( this.m1 )*this.l1, [pointLength], np.ones( this.m2 )*this.l2 ])


    def compute(this, varVals:np.ndarray):
        R1 = varVals[0]
        R2 = varVals[1]
        alphas = varVals[2:]

        pTen = R1
        errors = np.zeros( alphas.size )

        for i in range( 0, alphas.size ):
            


    def plotDataset( this, varVals, plotStyle="r-" ):
        R1 = varVals[0]
        R2 = varVals[1]
        alphas = varVals[2:]

        xT = 0
        yT = 0

        xVal = [ 0 ]
        yVal = [ 0 ]

        for i in range(0, alphas.size):
            cAlpha = alphas[i]
            cLen   = this.lengs[i]
            xT += np.cos( cAlpha ) * cLen
            yT += np.sin( cAlpha ) * cLen
            xVal.append( xT )
            yVal.append( yT )

        plt.plot( xVal, -np.array( yVal ), plotStyle )

    def validate( this, inpVals ):
        plt.figure( 21 )
        plt.grid()
        this.plotDataset( this.getInitVals(), "rx--" )

        plt.show( block=False )
        ""

    def getInitVals(this):
        xP = (this.x_s**2 + this.L1**2 - this.L2**2)/(2 * this.x_s)
        yP = ( this.L1**2 - xP**2 )**0.5

        alphaL1 = np.arctan( yP/xP )
        alphaL2 = - np.arctan( yP/(this.x_s - xP) ) 

        Txp = xP*this.pW/yP
        vTL1 = Txp*this.L1/xP
        vTL2 = Txp*this.L2/(this.x_s - xP)

        alphasL1 = np.ones(this.m1) * alphaL1
        alphasL2 = np.ones(this.m2) * alphaL2

        initVals = np.concatenate( [[ vTL1, vTL2 ], alphasL1, [0], alphasL2] )

        return initVals


sRes = 1
sL1  = 5
sL2  = 6
pSim = Pulley( 5, 1, 3, 8, sL1, sL2, sRes )

pSim.validate( "" )
