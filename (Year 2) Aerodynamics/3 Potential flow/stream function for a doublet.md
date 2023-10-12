---
aliases: [""]
tags: []
---

## Stream function for a doublet

### Derivation
We can get the stream function of a doublet by placing a [[stream function for line source or sink|source and sink]] next to each other with an infinitesimally small separation. Recall the equation for a source/sink is:
$$ \psi(x,z) = \frac{Q}{2\pi} \arctan \left(\frac{z-z_{0}}{x-x_{0}}\right)  $$ So take this and get a source of strength $Q$ at $0,-B$ and then place a sink of strength $Q$ at $0 , B$:

$$\begin{align*}
\psi_{source}(x,z) &=  \frac{Q}{2\pi} \arctan \left(\frac{z }{x+B}\right) & \psi_{sink}(x,z) &=  \frac{-Q}{2\pi} \arctan \left(\frac{z }{x- B}\right)
\end{align*}$$
Then we know that [[addition of stream functions]] is possible hence:
$$\begin{align*}
\psi_{doublet}(x,z) &=  \frac{Q}{2\pi} \arctan \left(\frac{z }{x+B}\right) -\frac{Q}{2\pi} \arctan \left(\frac{z }{x- B}\right) 
\end{align*}$$
If we convert to polar coordinates:
$$\begin{align*}
\psi_{doublet}(\theta,r) &=  \frac{Q}{2\pi} (\theta_{1}-\theta_{2})
\end{align*}$$
If we kept $Q$ constant then as $\Delta \theta$ tends to zero the whole function would tent to zero which is not useful, so instead we are going to scale $Q$ according to the distance $B$ using the relationship: $Q2B=k$ where $k$ is some constant hence $Q=\frac{k}{2B}$:
$$\begin{align*}
\psi_{doublet}(\theta,r) &=  \frac{Q}{2\pi} (\theta_{1}-\theta_{2})\\
  &=  \frac{2BQ}{2\pi} \left( \frac{\theta_{1}-\theta_{2}}{2B} \right)\\
  &=  \frac{k}{2\pi} \left( \frac{\theta_{1}-\theta_{2}}{2B} \right)\\
\end{align*}$$
Then it can be shown (with maths that's [[aka I did not look it up and its not in the notes since we do not need to know it|too complex to be suitable here]]) that:
$$\begin{align*}
\lim_{B\to 0} \frac{\theta_{1}-\theta_{2}}{2B} &= \lim_{B\to 0} \frac{  \arctan \left(\frac{z }{x+B}\right) -  \arctan \left(\frac{z }{x- B}\right)  }{2B} = - \frac{\sin\theta}{r}
\end{align*}$$
Hence subbing back into the previous equation, as $B$ approaches zero:
$$\begin{align*}
\psi_{doublet}(\theta,r)  &=  -\frac{k}{2\pi} \frac{\sin\theta}{r}\\
\end{align*}$$
### Equation

The conversion to the cartesian form is complex and not needed here, so just take my word for it. [[prove it yourself|:trol:]]

> ## $$ \psi(x,z) = - \frac{k}{2\pi} \frac{z-z_{0}}{(x-x_{0})^{2} + (z-z_{0})^{2}}  $$ 
> ## $$ \psi( r, \theta ) =  -\frac{k}{2\pi} \frac{\sin\theta}{r} $$ 
>> where:
>> $z,x=$ position
>> $x_{0},z_{0}=$ position of doublet
>> $k=$ strength of doublet
>> $\psi=$ [[stream function (2D)|stream function]] of  doublet

### Application


```jupyter
import numpy as np
import matplotlib.pyplot as plot

domainWidth = 2;

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

# Here is the stream function we defined above
def sourceDB( x0,z0, x,z, strength ): 
    return (-strength/(2*np.pi)) * ( ( z-z0 )/( (x-x0)**2 + (z-z0)**2 ) )
 
streamFunction = sourceDB( -0.05,0.05, x,z, 5 );

# We can then get the velocitys from the scalar values of the stream function
u,w = getVelocitys( streamFunction )

plot.figure(69)
plot.title("flow field")
plot.quiver( x, z, u, w )
plot.contour( x, z, streamFunction,100)

plot.show()

```