import numpy as np
import matplotlib.pyplot as plot 

domainWidth = 13;

xMin = -2
xMax = 2
zMin = -2
zMax = 2

dx = dz = 0.01

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
	return 1-(((u**2) + (w**2)) / (Uref**2))

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
	if ( stagnationValue > 0.2 ):
		print("unable to find stagnation point (try increasing dx), lowest vel was: ",stagnationValue/1.5)
		return [[],[]]

	print("using sv:", stagnationValue)

	pointIndecies = np.where(  ( np.abs( u ) + np.abs( w ) )< stagnationValue) 

	return [ x[pointIndecies], z[pointIndecies] ];

def getStagnationSFVal( x,z, u,w, streamFunction ):
	xIndx,zIndx = np.unravel_index( np.argmin( np.abs( u ) + np.abs( w ) ), u.shape ) 

	return streamFunction[ xIndx, zIndx ]
 
def readValue( X, Z, dataGrid, showOnGraph=False ):
	if ( showOnGraph ):
		plot.plot( X, Z, "gx" )

	return dataGrid[ int((Z-zMin)/dz), int((X-xMin)/dx) ]
 
 
def filterExtreme( inp, maxMag ):
	return np.where( abs(inp)<maxMag, inp, maxMag*inp/abs(inp) )

Uinf = 1;



#streamFunction = linearSF( x,z, 0, Uinf ) + vortexSF(0,0, x,z, 56.25674); 
a = 0.5
k = 2 * np.pi

streamFunction = doubletSF( a,0, x,z, k ) + doubletSF( -a,0, x,z, -k )

u,w = getVelocitys( streamFunction )

 
cp = getPressureCFs( u,w, Uinf )



plot.figure(69)
plot.title("flow field") 

stX,stZ = getStagnationPoints( x,z,u,w )

plot.plot( stX, stZ, "rx" )

# Pressure plot
plot.colorbar( plot.contourf( x, z, filterExtreme( cp, 2 ), 60 ) )

# Applies bernoullis to find the difference in pressure between two points = P1-P2
def getPressureDif( x1, z1, x2, z2, u, w, rho ):
	return rho*((readValue( x1, z1, u )**2 + readValue( x1, z1, w )**2) - (readValue( x2, z2, u )**2 + readValue( x2, z2, w )**2) )/2

print("u,w at (0,0):", readValue( 0,0, u, True ), readValue( 0,0, w, True ) )
print("u,w at (0,1):", readValue( 0,1, u, True ), readValue( 0,1, w, True ) )
print("u,w at (0,2):", readValue( 0,1.98, u, True ), readValue( 0,1.98, w, True ) )
print("delta P      :", getPressureDif( -2, 0, -4, 0, u, w, 1000 ) )
print("mStag: ", getLowestVelPoint( x,z,u,w ) )
print("stags: ",stX,stZ )


# Streamline plot
plot.contour( x, z, filterExtreme( streamFunction, 100 ), 30 ) 

stagnationPointStreamFunctionValue = getStagnationSFVal( x,z,u,w,streamFunction )
print( "stagnationPoint SF value: ", stagnationPointStreamFunctionValue )

# Streamline going through stagnation point
plot.contour( x, z, streamFunction,[stagnationPointStreamFunctionValue], linewidths=2, colors="black" ) 

plot.show()

input("")