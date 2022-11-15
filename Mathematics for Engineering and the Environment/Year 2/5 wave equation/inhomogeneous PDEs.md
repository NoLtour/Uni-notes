---
aliases: [""]
tags: []
---

## Inhomogeneous PDEs
You thought normal [[separation of variables]] was a pain? Well it gets worse, introducing inhomogeneous PDEs. For example this abomination:

$$ \frac{\delta y}{\delta t} = k^{2} \frac{\delta^{2} y}{\delta x^{2}} + F(x,t) $$
$$\begin{align*}
\text{where:} & & y(0,t) &= 0 & y(1,t)&= 0
\end{align*}$$
If we try the rearranging process from [[separation of variables#Separation]] we can't get the equation above into something useful, we just end up with:
$$ \frac{\dot{T}}{T} = k^{2} \frac{X''}{X} + \frac{F}{XT} $$
(useless)
What we can do is guess that all the elements that make up the structure of the PDE are similar, if that's the case then the solution to the equation without the $F$ term should hold useful information... so for the sake of argument lets solve the equation:
$$ \frac{\delta y}{\delta t} = k^{2} \frac{\delta^{2} y}{\delta x^{2}}   $$
This is of course solvable using the content from [[separation of variables]], (not going to prove this because pointless) if this is solved using the boundary conditions from the original equation you get:
$$\begin{align*}
y & = \sum\limits^{\infty}_{n=1} T_{n}(t) \sin(n\pi x) 
\end{align*}$$

