---
aliases: [""]
tags: []
---

## Stream function for line source or sink

### Derivation

![[Pasted image 20221106164053.png]]

If we take the origin at the point of the source/sink the maths becomes much cleaner. This is the same method as [[stream function for uniform flow#Derivation]] except now we will use the polar form of [[stream function (2D)|stream function]]. It is clear from observation that the angular velocity is zero, however the radial velocity is a bit more complex.
If we define the volume flow rate from the source as $\dot{q}$ then the 2D version is the area flow rate which is constant and can be defined as $Q$. It can then be observed that if you draw a circle of any radius around the origin the total area flow rate through it will be constant regardless of radius. Hence since we know the perimeter of the circle is $P=2\pi r$ and the area flow rate to be $Q=PV$ we can get:
$$\begin{align*}
Q &=  2\pi r V\\
\frac{Q}{2\pi r} &= V
\end{align*}$$
Since we know that $V$ is only acting in the radial direction, this can be written as $\frac{Q}{2\pi r}  = V_{r}$ now we just sub the identities of radial and angular velocity into the [[stream function (2D)|stream function]] definition in polar coordiantes and integrate:
$$\begin{align*}
 V_{r} &= \frac{1}{r} \frac{\delta \psi}{ \delta \theta } & V_{\theta} &= - \frac{\delta \psi}{ \delta r } \\
\frac{Q}{2\pi r} &= \frac{1}{r} \frac{\delta \psi}{ \delta \theta } & 0 &= - \frac{\delta \psi}{ \delta r }\\
\int \frac{Q}{2\pi  } \delta \theta &=  \int \delta \psi  &\int 0 \delta r &= \int \delta \psi  \\
 \frac{Q}{2\pi} \theta + f(r) &= \psi( r, \theta ) & 0 + f(\theta) &= \psi( r, \theta )\\\\
\therefore \: \frac{Q}{2\pi} \theta  &= \psi( r, \theta )
\end{align*}$$

Once again it is also possible to do a similar method to find the [[velocity potential]] (which would be $\phi = \frac{Q}{2\pi}\ln r$). To convert this into cartesian coordinates is trivial, just sub in $\theta=\arctan \frac{z}{x}$:
$$ \frac{Q}{2\pi} \arctan \frac{z}{x}  = \psi( x, z ) $$
This form still requires the source/sink to be at the origin, but if we let the source be at $(x_{0},z_{0})$ it's clear that the stream function can be written as:
$$ \frac{Q}{2\pi} \arctan \frac{z-z_{0}}{x-x_{0}}  = \psi( x, z ) $$


### Equation

> ## $$ \psi(x,z) = \frac{Q}{2\pi} \arctan \left(\frac{z-z_{0}}{x-x_{0}}\right)  $$ 
>> where:
>> $z,x=$ position
>> $x_{0},z_{0}=$ position of source/sink
>> $Q=$ area flow rate from source (negative indicates sink)
>> $\psi=$ [[stream function (2D)|stream function]] of source/sink

### Application


```jupyter
import numpy as np
import matplotlib.pyplot as plot

domainWidth = 2;

xMin = -domainWidth
xMax = domainWidth
zMin = -domainWidth
zMax = domainWidth

dx = dz = 0.25

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
    return (flowRate/(2*np.pi)) * np.arctan( (z0-z)/(x0-x) )

# By changning alpha and speed you can change the resulting velocitys
streamFunction = sourceSF( 0.6,0.6, x,z, 5 );

# We can then get the velocitys from the scalar values of the stream function
u,w = getVelocitys( streamFunction )

plot.figure(69)
plot.title("flow field")
plot.quiver( z, x, u, w )

plot.show()
```
