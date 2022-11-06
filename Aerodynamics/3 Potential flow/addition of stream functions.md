---
aliases: [""]
tags: []
---

## Addition of stream functions
### Idea
We know that  [[laplace equation for flow|Laplace equation]] contains a definition regarding [[stream function (2D)|stream functions]]:

$$ 0 = \frac{\delta^{2} \psi}{\delta x^{2}} + \frac{\delta^{2} \psi}{\delta  y^{2}} $$

It can be seen that this equation which describes flow is linear, hence solutions to this equation can be superimposed on each other:

$$\psi = \psi_{1}+ \psi_{2}+ \psi_{3}+...+ \psi_{n}$$

This means that by adding multiple stream functions to each other it is possible to get more complex resultant flows:
![[Pasted image 20221106190721.png]]

### Example (doublet)
Simply taking the [[stream function for line source or sink]] and then placing a source at $(0.45,0.05)$ and a sink at $(-0.45,0.05)$ results in:
```jupyter
import numpy as np
import matplotlib.pyplot as plot

domainWidth = 1.4;

xMin = -domainWidth
xMax = domainWidth
zMin = -domainWidth
zMax = domainWidth

dx = dz = 0.1

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
 
def sourceSF( x0,z0, x,z, flowRate ): 
    return (flowRate/(2*np.pi)) * np.arctan( (z-z0)/(x-x0) )

# addition of the two source functions
streamFunction = sourceSF( 0.45,0.05, x,z, 12 ) +  sourceSF( -0.45,0.05, x,z, -12 );

# We can then get the velocitys from the scalar values of the stream function
u,w = getVelocitys( streamFunction )

plot.figure(69)
plot.title("flow field")
plot.quiver( x, z, u, w )
plot.contour( x, z, streamFunction, 50)   # streamlines

plot.show()

```

The resulting 