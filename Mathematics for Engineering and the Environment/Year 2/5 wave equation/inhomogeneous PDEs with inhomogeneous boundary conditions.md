---
aliases: [""]
tags: []
---

## Inhomogeneous PDEs with inhomogeneous boundary conditions
### Intro
So far we've been working with cases where the boundary conditions are homogeneous, aka $y(...)=0$ such as:
$$\begin{align*}
\frac{\delta y}{\delta t} &= \frac{\delta^{2} y}{\delta x^{2}} &&&&\text{where}:& y(0,t)&= 0, &y(1,t)&= 0
\end{align*}$$
But now we have the [[a funny|fun]] situation where the boundary conditions are non homogeneous ([[I am dead inside|yay]]):
$$\begin{align*}
\frac{\delta y}{\delta t} &= \frac{\delta^{2} y}{\delta x^{2}} &&&&\text{where}:& y(0,t)&= f_{1}(t), &y(1,t)&= f_{2}(t)
\end{align*}$$
Then the methods discussed up to now don't work, so we need to figure out a way of solving them anyway.

### Case with constants

If we could somehow 
