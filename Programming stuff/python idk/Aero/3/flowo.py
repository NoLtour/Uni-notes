import numpy as np
import matplotlib.pyplot as plot
import matplotlib.ticker as tickers
from scipy import interpolate

domainWidth = 2;

xMin = -domainWidth
xMax = domainWidth
zMin = -domainWidth
zMax = domainWidth

dx = dz = 0.002

# Create axis' using domain at the defined resolution
xAxis = np.arange( xMin, xMax, dx )
zAxis = np.arange( zMin, zMax, dz )

# We take our 2 axis and then create a grid
x,z = np.meshgrid( xAxis, zAxis )
 

def getVelocitys( streamFunction ):
	dXpsi,dZpsi = np.gradient( streamFunction );
	
	u = dXpsi/dz
	w = -dZpsi/dx
	
	return [u,w]

def getPressureCFs( u,w,Uref ):
	return 1-((u**2 + w**2) / (Uref**2))

# Stream function for linear flow
def linearSF( x,z, alpha, speed ):
    return speed*( (z*np.cos(alpha) ) - (x*np.sin(alpha) )  )

# Stream function source/sink
def sourceSF( x0,z0, x,z, flowRate ): 
    return (flowRate/(2*np.pi)) * np.arctan( (z-z0)/(x-x0) )

# Stream function doublet
def doubletSF( x0,z0, x,z, strength ): 
    return (-strength/(2*np.pi)) * ( ( z-z0 )/( (x-x0)**2 + (z-z0)**2 ) )

# Stream function vortex
def vortexSF( x0,z0, x,z, Gamma ): 
    return (Gamma/(2*np.pi)) * np.log( np.sqrt( (x-x0)**2 + (z-z0)**2 ) )

# returns [X,Z]
def getLowestVelPoint( x,z, u,w ):
	xIndx,zIndx = np.unravel_index( np.argmin( np.abs( u ) + np.abs( w ) ), u.shape )

	xPos = x[ xIndx, zIndx ];
	zPos = z[ xIndx, zIndx ]; 

	return xPos, zPos



def getStagnationPoints( x,z, u,w ): 
	stagnationValue = np.min( np.abs( u ) + np.abs( w ) )*1.5
	if ( stagnationValue > 0.15 ):
		print("unable to find stagnation point, lowest vel was: ",stagnationValue/1.5)
		return [[],[]]

	print("using sv:", stagnationValue)

	pointIndecies = np.where(  ( np.abs( u ) + np.abs( w ) )< stagnationValue) 

	return [ x[pointIndecies], z[pointIndecies] ];

def getStagnationSFVal( x,z, u,w, streamFunction ):
	xIndx,zIndx = np.unravel_index( np.argmin( np.abs( u ) + np.abs( w ) ), u.shape ) 

	return streamFunction[ xIndx, zIndx ]


def niceContorPlot( x,z, scalarField, lineCount ):
	niceVals = []

	xRange = xMax-xMin
	xStep  = xRange/lineCount

	zRange = zMax-zMin
	zStep  = zRange/lineCount

	cX = xMin
	cZ = zMin
	
	alt = 0
	while ( cX <= xMax ):
		#niceVals.append( scalarField[ int((xMin + xRange*np.random.random())/dx ) ][ int((zMin + zRange*np.random.random())/dz) ] )

		if ( alt == 0 ):
			niceVals.append( scalarField[ int((cX-xMin)/dx) ][ int((cZ-zMin)/dz) ] )
		elif ( alt == 1 ):
			niceVals.append( scalarField[ int((xMax-cX)/dx) ][ int((zMax-cZ)/dz) ] )
		elif ( alt == 2 ):
			niceVals.append( scalarField[ int((xMax-cX)/dx) ][ int((cZ-zMin)/dz) ] )
		elif ( alt == 3 ):
			niceVals.append( scalarField[ int((cX-xMin)/dx) ][ int((zMax-cZ)/dz) ] )


		cX = cX + xStep
		cZ = cZ + zStep
		alt = int(4*np.random.random()) #(alt+1)%4

	niceVals = np.unique( sorted(niceVals) )

	plot.contour( x, z, scalarField, niceVals )

Uinf = 10;

streamFunction = linearSF( x,z, 0, 10 ) + doubletSF( 0, 0, x,z, 5 ) ;
#streamFunction = linearSF( x,z, np.pi/2, 10 ) + sourceSF( 0.1, -0.5, x,z, 2.5 ) + sourceSF( -0.1, -0.5, x,z, 2.5 ) + sourceSF( 0, 0.5, x,z, -5 ) + doubletSF( 0.1, 0.2, x,z, -0.6 ) + sourceSF( -0.1, 0.16, x,z, 0.5 );

# We can then get the velocitys from the scalar values of the stream function
u,w = getVelocitys( streamFunction )

plot.figure(69)
plot.title("flow field")
#plot.quiver( x, z, u, w )

stX,stZ = getStagnationPoints( x,z,u,w )

plot.plot( stX, stZ, "rx" )

niceContorPlot( x,z, streamFunction, 40 )

plot.contour( x, z, streamFunction,[getStagnationSFVal( x,z,u,w,streamFunction )], linewidths=2, colors="black" )

plot.show()
