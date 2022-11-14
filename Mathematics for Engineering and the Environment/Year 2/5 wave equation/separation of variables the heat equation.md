---
aliases: [""]
tags: []
---

## Separation of variables the heat equation
Here we are going to be applying what was done from [[separation of variables]] but to the heat equation ([[parabolic partial differential equations|the prototype example for parabolic PDEs]]).

Solve:
$$ \frac{\delta y}{\delta t} = k^{2} \frac{\delta^{2} y}{\delta x^{2}} $$
With the boundary conditions:
$$\begin{align*}
\frac{\delta y}{\delta x}(0, t) &= 0, & \frac{\delta y}{\delta x}(1,t)=0  
\end{align*}$$
And initial data:
$$ y(x,0) = x(1-x) $$
