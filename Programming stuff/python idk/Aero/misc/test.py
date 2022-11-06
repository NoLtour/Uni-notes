import numpy as np
import matplotlib.pyplot as plot

domainWidth = 2;

xMin = -domainWidth
xMax = domainWidth
zMin = -domainWidth
zMax = domainWidth

dx = dz = 0.2

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

# Here is the linear stream function we defined above
def sourceSF( x0,z0, x,z, flowRate ):
    return x+z
    #return (flowRate/(2*np.pi)) * np.arctan2( (z-z0), (x-x0) )

# By changning alpha and speed you can change the resulting velocitys
streamFunction = sourceSF( 0.6,0.6, x,z, 5 );

# We can then get the velocitys from the scalar values of the stream function
u,w = getVelocitys( streamFunction )

plot.figure(69)
plot.title("flow field")
plot.quiver( z, x, u, w )

plot.show()
