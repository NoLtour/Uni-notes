---
aliases: ["hyperbolic PDEs"]
tags: []
---

## Hyperbolic partial differential equations

### Intro

Hyperbolic PDEs are usually associated with wave propagation, and are central to hydro- and electro- dynamics. What is important to note about [[hyperbolic partial differential equations|hyperbolic PDEs]] is that information is propagated at a finite speed. For example:

$$ \frac{\delta^{2} u}{\delta t^{2} } = c^{2} \frac{\delta^{2} u}{ \delta x^{2} } $$

This is an example of a hyperbolic PDE, in which its graph can be seen below; what is notable is that as time progresses the wave moves and there is no movement of "information" faster than what is permitted, the variable that in this case is defining information propagation speed "c".
![[Pasted image 20221103214940.png]]
![[Pasted image 20221103214950.png]]
Other wave propagation problems include acoustics, seismic waves, shallow water theory, general relativity, global atmospheric dynamics, Maxwell’s equations, and so on.

### Boundary conditions

![[Pasted image 20221104093233.png]]

To fix these equations we require 4 boundary conditions:
- 2 Boundary conditions at the ends of the domain $x=0 ,\:x=L$. These boundary values might be of the form $u(0,t)=0$ or the derivative $\frac{d}{dx}u(0,t)=0$.
- 2 initial conditions ($t=0$) here you'll probably have some value and the derivative eg: $u(x,0)=0$, $\frac{d}{dt}u(x,0)=0$.

Notice how these boundary conditions defined for a specific value of the independent variable works for all values of the other independents, hence why on the graph they can be visualised as strait lines.
