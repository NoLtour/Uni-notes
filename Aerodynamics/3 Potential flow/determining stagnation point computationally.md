---
aliases: [""]
tags: []
---

## Determining stagnation point computationally

Although it has been shown in [[defining the geometry of an object in a flow]] that [[stagnation point]] and the related surface can be found analytically, for things such as [[Flow past a circular cylinder]] it is possible but hard, so instead we can find it computationally. Done right this also provides a program which can solve general potential flow problems.

To start we can define the environment from [[computational environment setup for potential flow]]:


```jupyter
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
 
def niceContorPlot( x,z, scalarField, lineCount ):
	niceVals = []

	xRange = xMax-xMin
	xStep  = xRange/lineCount

	zRange = zMax-zMin
	zStep  = zRange/lineCount

	cX = xMin
	cZ = zMin
	while ( cX <= xMax ):
		niceVals.append( scalarField[ int((cX-xMin)/dx) ][ int((cZ-zMin)/dz) ] )

		cX = cX + xStep
		cZ = cZ + zStep

	niceVals = np.unique( sorted(niceVals) )

	plot.contour( x, z, scalarField, niceVals )

Uinf = 10;

streamFunction = linearSF( x,z, 0, 10 ) + doubletSF( 0, 0, x,z, 5 ) ;

# We can then get the velocitys from the scalar values of the stream function
u,w = getVelocitys( streamFunction )

print("done running")
```

To get the stagnation point, we simply need to find where in our domain the velocity is zero, of course since the $dx,dz$ is not at zero some errors will occur so instead of looking for where it equals exactly zero we need to look at where it's near zero:

```jupyter
def getStagnationPoints( x,z, u,w ): 
	stagnationValue = np.min( np.abs( u ) + np.abs( w ) )*1.5
	if ( stagnationValue > 0.15 ):
		print("unable to find stagnation point, lowest vel was: ",stagnationValue/1.5)
		return [[],[]]

	print("using sv:", stagnationValue)

	pointIndecies = np.where(  ( np.abs( u ) + np.abs( w ) )< stagnationValue) 

	return [ x[pointIndecies], z[pointIndecies] ];

print("done running")
```

Instead of using $|V|=\sqrt{ u^{2} + w^{2} }$ we are using $|V|\approx |u| + |w|$ since it is less computationally demanding and reasonably suitable for this application. This can get us the stagnation points:
```jupyter
plot.figure(69)

niceContorPlot( x,z, streamFunction, 40 )

stX,stZ = getStagnationPoints( x,z,u,w )

plot.plot( stX, stZ, "rx" )
```

Then we can find the streamfunction that correlates to the stagnation point using:
```jupyter
def getStagnationSFVal( x,z, u,w, streamFunction ):
	xIndx,zIndx = np.unravel_index( np.argmin( np.abs( u ) + np.abs( w ) ), u.shape ) 

	return streamFunction[ xIndx, zIndx ]

print("done running")
```

Plotted we get:
```jupyter
plot.figure(21)
plot.title("flow field")
#plot.quiver( x, z, u, w )

stX,stZ = getStagnationPoints( x,z,u,w )

plot.plot( stX, stZ, "rx" )

niceContorPlot( x,z, streamFunction, 40 )

stagnationStreamValue = getStagnationSFVal( x,z,u,w,streamFunction );

print("the stream function at stagnation point: ",stagnationStreamValue)

plot.contour( x, z, streamFunction,[ stagnationStreamValue ], linewidths=2, colors="black" )

plot.show()
```

It is clear from this that for [[Flow past a circular cylinder]] the stagnation points occur on the leading and trailing edge, and the stream function that intercepts this occurs along the radius.
