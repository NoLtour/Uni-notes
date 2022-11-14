---
aliases: [""]
tags: []
---

## Separation of variables the heat equation
#### Problem setup
Here we are going to be applying what was done from [[separation of variables]] but to the heat equation ([[parabolic partial differential equations|the prototype example for parabolic PDEs]]).

Solve:
$$ \frac{\delta y}{\delta t} = k^{2} \frac{\delta^{2} y}{\delta x^{2}} $$
With the boundary conditions:
$$\begin{align*}
\frac{\delta y}{\delta x}(0, t) &= 0, & \frac{\delta y}{\delta x}(1,t)=0  
\end{align*}$$
And initial data:
$$ y(x,0) = x(1-x) $$


#### Definition of boundary conditions
Just like last time we assume $y=T(t)\times X(x)$ hence:
$$\begin{align*}
\frac{\delta y}{\delta t} &=  k^{2} \frac{\delta^{2} y}{\delta x^{2}}\\
\frac{\delta TX}{\delta t} &=  k^{2} \frac{\delta^{2} TX}{\delta x^{2}}\\
X \dot{T} &=  k^{2} T X''\\
 \frac{X''}{X} &=k^{2} \frac{\dot{T}}{T}=\lambda 
\end{align*}$$
$$\begin{align*}
 \dot{T} - \frac{\lambda}{k^{2}} T&= 0 & X''-\lambda X &=  0
\end{align*}$$
Then we can 