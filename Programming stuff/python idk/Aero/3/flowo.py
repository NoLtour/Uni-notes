import numpy as np
import matplotlib.pyplot as plot

domainWidth = 2;

xMin = -domainWidth
xMax = domainWidth
zMin = -domainWidth
zMax = domainWidth

dx = dz = 0.04

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
 
Uinf = 10;

streamFunction = linearSF( x,z, 0, 10 ) + doubletSF( dx/2,dz/2, x,z, 5 );

# We can then get the velocitys from the scalar values of the stream function
u,w = getVelocitys( streamFunction )

plot.figure(69)
plot.title("flow field")
plot.quiver( x, z, u, w )
#plot.contour( x, z, streamFunction,40)
plot.contour( x, z, streamFunction,1, value=0 )

plot.show()
