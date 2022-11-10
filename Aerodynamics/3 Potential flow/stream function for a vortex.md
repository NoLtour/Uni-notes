---
aliases: [""]
tags: []
---

## Stream function for a vortex
### Derivation
Consider a flow which is irrotational for all points except for the origin which has a [[circulation]] of $\Gamma$:

![[Pasted image 20221110001216.png]]

The radial and angular velocities can be described as:
$$\begin{align*}
V_{\theta} &= \frac{c}{r} & V_{r} &=0
\end{align*}$$
Then we can use the identity of [[circulation]], but first we need to know the area of interest; here we know that the total [[circulation]] within any sized circle around the origin is $\Gamma$, a infentesimaly small line segment of the perimeter of a circle of radius $r$ can be defined as $d\vec{s}=rd\theta$ which is what we need for the equation of circulation:
$$\begin{align*}
\Gamma &= \int_{C} \vec{V} \cdot d\vec{s} && \to &  \Gamma &= \int_{0}^{2\pi} \vec{V} \cdot rd\theta && \to &  \Gamma &= \int_{0}^{2\pi} c d\theta \\&&&&&&&&&= -2\pi c
\end{align*}$$
Using the definition of $c$:
$$ V_{\theta} = - \frac{\Gamma}{2\pi r} $$
Then using the same method from [[stream function for uniform flow]] we can get it's stream function using the defs of $V_{\theta}$ and $V_{r}$ which with a bit of [[sometimes I cba to do extra detail on the proofs leave me alone|omitted maths]] gives us:
$$\begin{align*}
\psi (r,\theta) &= - \frac{\Gamma}{2\pi} \ln r
\end{align*}$$

### Equation

> ## $$ \psi(x,z) = \frac{\Gamma}{2\pi} \ln\sqrt{(x-x_{0})^{2} + (z-z_{0})^{2}} $$ 
> ## $$ \psi (r,\theta)  = - \frac{\Gamma}{2\pi} \ln r $$ 
>> where:
>> $z,x=$ position
>> $x_{0},z_{0}=$ position of doublet
>> $\Gamma=$ [[circulation]] of vortex
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