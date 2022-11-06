---
aliases: [""]
tags: []
---

## Stream function for uniform flow
### Derivation
Honestly the whole idea of [[stream function (2D)|stream function]] is kinda abstract, but it is essentially a function that describes the shape of flow. It'll be clearer once this example is done.

Lets say we want to find the stream function for a uniform flow:
![[Pasted image 20221106142734.png]]
It's clear that for this sort of uniform flow that:
$$\begin{align*}
V_{z} = w &= U_{\infty} \sin \alpha & V_{x} = u &= U_{\infty} \cos \alpha 
\end{align*}$$
Then we can take the definition of [[stream function (2D)|stream function]] and the method for [[derivative symbols#Example (and how to integrate these)|integrating partial derivatives]] to find the streamfunction:
$$\begin{align*}
V_{x} &= \frac{\delta \psi}{ \delta z } & V_{z} &= - \frac{\delta \psi}{ \delta x }   &  V_{z}  &= U_{\infty} \sin \alpha & V_{x}  &= U_{\infty} \cos \alpha \\
 U_{\infty} \cos \alpha &= \frac{\delta \psi}{ \delta z } & U_{\infty} \sin \alpha &= - \frac{\delta \psi}{ \delta x } \\
\int U_{\infty} \cos \alpha \delta z &= \int \delta \psi & \int U_{\infty} \sin \alpha \delta x &= - \int \delta \psi\\
zU_{\infty} \cos \alpha + f(x) &= \psi(x,z) & -xU_{\infty} \sin \alpha + f(z) &= \psi(x,z)\\\\
\therefore \:\psi(x,z) &= U_{\infty}( z \cos \alpha - x \sin \alpha )
\end{align*}$$

It is possible to do the same sort of method for finding [[velocity potential]], for defining a potential flow you can use one or the other. (Here if you do this method for [[velocity potential]] you'd get $\phi(x,z)= U_{\infty}( x \cos \alpha + z \sin \alpha )$ which is clearly at 90 degrees to the [[stream function (2D)|stream function]] as expected by defenition).

### Equation

> ## $$ \psi(x,z) = U_{\infty}( z \cos \alpha - x \sin \alpha ) $$ 
>> where:
>> $z,x=$ position
>> $U_{\infty}=$ flow speed
>> $\alpha=$ flow angle
>> $\psi=$ [[stream function (2D)|stream function]] of uniform flow at angle $\alpha$
>> ![[Pasted image 20221106142734.png]]

### Application
If we take the [[computational environment setup for potential flow]] and then define our stream function we can easily get a representation of the flow:

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
	dXpsi,dZpsi = np.gradient( streamFunction );
	
	u = dXpsi/dz
	w = -dZpsi/dx
	
	return [u,w]

def getPressureCFs( u,w,Uref ):
	return 1-((u**2 + w**2) / (Uref**2))

# Here is the linear stream function we defined above
def linearSF( x,z, alpha, speed ):
    return speed*( (z*np.cos(alpha) ) - (x*np.sin(alpha) )  )

# By changning alpha and speed you can change the resulting velocitys
streamFunction = linearSF( x,z, np.pi/8, 5 );

# We can then get the velocitys from the scalar values of the stream function
u,w = getVelocitys( streamFunction )

plot.figure(69)
plot.title("flow field")
plot.quiver( z, x, u, w )

plot.show()
```
