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
	dZpsi,dXpsi = np.gradient( streamFunction );
	
	u = dZpsi/dz
	w = -dXpsi/dx
	
	return [u,w]
```

With velocity defined, it is then possible to get [[pressure coefficient]]s using [[Bernouillis equation]] since [[solving the euler equations|we know that for irrotational flow bernoulli can be applied between any two points]]:

$$\begin{align*}
&&  \frac{V^{2}}{2} + hg + \frac{p}{\rho} &= K \\
& & \frac{V_{\infty}^{2}}{2}  + \frac{p_{\infty}}{\rho} &= \frac{V^{2}}{2}  + \frac{p}{\rho} \\
C_{p} &= \frac{p-p_{\infty}}{\frac{1}{2}\rho_{\infty}V^{2}_{\infty} } &  \rho \left(\frac{V_{\infty}^{2}}{2} - \frac{V^{2}}{2}\right) &=     p  -  p_{\infty} \\
 &= \frac{  V_{\infty}^{2} -  V^{2}  }{ V^{2}_{\infty} } &&& V^{2} &= u^{2} + w^{2}\\
  &= 1-\frac{  u^{2} + w^{2}  }{ V^{2}_{\infty} }
\end{align*}$$
Implemented into code this becomes:

```jupyter
def getPressureCFs( u,w,Uref ):
	return 1-((u**2 + w**2) / (Uref**2))
```

Th