import numpy as np
import matplotlib.pyplot as plot

import sys; 
print(sys.executable)

domainWidth = 4;

xMin = -domainWidth
xMax = domainWidth
zMin = -domainWidth
zMax = domainWidth

dx = dz = 0.5

# Create axis' using domain at the defined resolution
xAxis = np.arange( xMin, xMax, dx )
zAxis = np.arange( zMin, zMax, dz )

# We take our 2 axis and then create a grid
x,z = np.meshgrid( xAxis, zAxis )
 

def getVelocitys( streamFunction ):
	dZpsi,dXpsi = np.gradient( streamFunction );
	
	u = dZpsi/dz
	w = -dXpsi/dx
	
	return [u,w]

def getPressureCFs( u,w,Uref ):
	return 1-((u**2 + w**2) / (Uref**2))

def linearSF( x,z, alpha, speed ):
    return speed*( (z*np.cos(alpha) ) - (x*np.sin(alpha) )  )

streamFunction = linearSF( x,z, np.pi/8, 5 );

u,w = getVelocitys( streamFunction )

plot.figure(69)
plot.title("flow field")
plot.quiver( z, x, u, w )

plot.show()