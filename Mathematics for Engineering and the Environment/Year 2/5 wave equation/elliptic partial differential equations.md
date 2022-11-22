---
aliases: ["elliptic PDEs"]
tags: []
---

## Elliptic partial differential equations

### Intro

Elliptic PDEs are usually associated with static or stationary problems (no time propagation). 
The prototype example would be [[laplace equation for flow|Laplace's equation]]:
$$ \frac{\delta^{2}u}{\delta x^{2}} + \frac{\delta^{2} u}{\delta y^{2}} = 0 $$
Which may look like:
![[Pasted image 20221103215820.png]]


### Boundary conditions

![[Pasted image 20221104094729.png]]

$$ \frac{\delta^{2}u}{\delta x^{2}} + \frac{\delta^{2} u}{\delta y^{2}} = 0 $$

If you look at the laplace equation above you can see that is is defined using 2 double derivatives, hence to fix these equations we require 4 boundary conditions:
- 2 Boundary conditions defining $x$
- 2 Boundary conditions defining $y$

There is no time dependence for elliptic problems, hence unlike most other cases we don't use initial conditions.
