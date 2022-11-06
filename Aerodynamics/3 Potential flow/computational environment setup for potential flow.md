---
aliases: [""]
tags: []
---

## Computational environment setup for potential flow

First we need to setup the grid that will form the space in which the flow occurs, hence we define the domain size as well as the step interval (resolution of our grid):

```jupyter
import numpy as np
import matplotlib.pyplot as plot

domainWidth = 4;

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
```

Since we will be given a stream function and we need velocity, we know we can get [[coordinate system being used in potential flow (stupid)#Velocity potential and stream function|velocity from the stream function]]:

```jupyter

def getVelocitys( streamFunction ):
	u,w = np.gradient( streamFunction );
	
	# Since 
	u = u/dz
	w = -w/dx
	
	return [u,w]


```
