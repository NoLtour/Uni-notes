---
aliases: [""]
tags: []
---

## Separation of variables for the elliptic PDEs
### Intro
Just doing [[separation of variables]] on [[elliptic partial differential equations|elliptic PDEs]], specifically Laplaces equation:
$$ \frac{\delta^{2}u}{\delta x^{2}} + \frac{\delta^{2}u}{\delta y^{2}} = 0 $$
Something that's noteable is that the laplace equation can also be written using the [[del operator]] to define the laplace equation in the nth dimension:
$$ \nabla^{2} u = 0 $$
Also unlike the previous examples where we used $y$ as the solution we are using $u$, since well $y$ is being used for a spacial variable ([[yee|duh]]).

### Boundary conditions
As discussed in [[elliptic partial differential equations|elliptic PDEs]], the problem needs to have 4 defined boundary conditions. Each can take on 1 of 3 types:
- Dirichlet BCs: $u(0,y) = 0$
- Neumann BCs: $\frac{\delta u}{\delta i}(0,y) = 0$
- Mixed BCs: $u(0,y)+\frac{\delta u}{\delta i}(0,y) = 0$

![[Pasted image 20221120122001.png]]

### Example
> Solve $\nabla u=0$ in 2 dimensions with boundary conditions:
> $$\begin{align*} u(0,y) &= 0 & u(1,y) &= 0 & u(x,0) &= 0 & u(x,1) &= 0 \end{align*}$$

We can re write $\nabla u=0$ into a more familiar form $\frac{\delta^{2}u}{\delta x^{2}} = -\frac{\delta^{2}u}{\delta y^{2}}$ then using [[separation of variables]] get:
$$ u(x,y) = XY $$
$$\begin{align*}
X'' - \lambda X &= 0 & Y'' + \lambda Y &= 0
\end{align*}$$
From here it's just the normal [[solving eigenvalue ODEs|eigenvalue ODE]] stuff.
