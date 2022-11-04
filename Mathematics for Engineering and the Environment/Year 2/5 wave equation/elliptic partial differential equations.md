---
aliases: ["elliptic PDEs"]
tags: []
---

## Elliptic partial differential equations

### Intro

Elliptic PDEs are usually associated with static or stationary problems (no time propagation). 
An example would be [[laplace equation for flow|Laplace's equation]]:
$$ \frac{\delta^{2}u}{\delta x^{2}} + \frac{\delta^{2} u}{\delta y^{2}} = 0 $$
Which may look like:
![[Pasted image 20221103215820.png]]


### Boundary conditions

![[Pasted image 20221104094309.png]]

$$\begin{align*}
\frac{\delta u}{\delta y }  &= k \frac{\delta^{2}u}{\delta x^{2}}
\end{align*}$$

If you look at the heat equation above you can see that is is defined using 1 double derivative and a normal derivative, hence to fix these equations we require 3 boundary conditions:
- 2 Boundary conditions at the ends of the domain $x=0 ,\:x=L$. These boundary values might be of the form $u(0,t)=0$ or the derivative $\frac{d}{dx}u(0,t)=0$.
- 1 initial condition ($t=0$) here you'll probably have some value or the derivative eg: $u(x,0)=0$, $\frac{d}{dt}u(x,0)=0$.

Notice how these boundary conditions defined for a specific value of the independent variable works for all values of the other independents, hence why on the graph they can be visualised as strait lines.