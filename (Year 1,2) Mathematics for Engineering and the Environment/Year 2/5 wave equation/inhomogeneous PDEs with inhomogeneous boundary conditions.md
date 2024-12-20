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
Since it's simpler for explaining the method we'll start with the case where the boundary conditions are non zero constants:
$$\begin{align*}
\frac{\delta y}{\delta t} &= \frac{\delta^{2} y}{\delta x^{2}} &&&&\text{where}:& y(0,t)&= C_{0}, &y(1,t)&= C_{1}
\end{align*}$$
What we really want to do is find a way to simplify this situation such that it can be solved using known methods, so what if we solve for some function that has a defined relationship to $y$ but is designed such that it's boundary conditions are zero?

$$\begin{align*}
y(x,t) - y_{p}(x) &= v(x,t) &&&&\text{where}:& v(0,t)&= 0, &v(1,t)&= 0\\
&&&&&& y(0,t) - y_{p}(0) &= 0 & y(1,t) - y_{p}(1) &= 0\\
y(x,t) &= v(x,t) + y_{p}(x)&&&&&  y_{p}(0) &=C_{0} &  y_{p}(1) &= C_{1}\\
\end{align*}$$
If we substitute this $v$ function into our original [[partial differential equation|PDE]] equation:
$$\begin{align*}
\frac{\delta y}{\delta t} &= \frac{\delta^{2} y}{\delta x^{2}} &\to&& \frac{\delta}{\delta t}(v(x,t) + y_{p}(x)) &= \frac{\delta^{2}}{\delta x^{2}}(v(x,t) + y_{p}(x))\\
&& && \frac{\delta v}{\delta t} &= \frac{\delta^{2} v}{\delta x^{2}} + \frac{\delta^{2} y_{p}}{\delta x^{2}}
\end{align*}$$
This equation is clearly solvable using [[separation of variables]] if we can find a function $y_{p}$ where $\frac{\delta^{2}}{\delta x^{2}} y_{p}=0$ since then the equation above simplifies to a familiar problem:
$$\begin{align*}
\frac{\delta v}{\delta t} &= \frac{\delta^{2} v}{\delta x^{2}}  &&&&\text{where}:& v(0,t)&= 0, &v(1,t)&= 0, & \frac{\delta^{2}}{\delta x^{2}} y_{p}&= 0\\
\end{align*}$$
Finding such a function of $y_{p}$ is actually pretty easy:
$$\begin{align*}
\frac{\delta^{2}}{\delta x^{2}} y_{p}&= 0 &  y_{p}(0) &=C_{0} &  y_{p}(1) &= C_{1}
\end{align*}$$
$$\begin{align*}
y_{p} &= C_{0} + (C_{1}-C_{0})x
\end{align*}$$
This clearly satisfies the conditions required, now we can just solve the simple problem of $v$ and then add $y_{p}$ onto the solution to get the solution of the original problem of $y$ since we've clearly stated that:
$$y(x,t) = v(x,t) + y_{p}(x)$$
### General case
Basically you know how we made a linear equation for the $y_p$, which worked for constant's? Well turns out that works in the general case as well, just replace the $C_1,C_2$ with functions:
$$ y_{p} = f_{0} + ( f_{1} - f_{0} ) x$$
$$\begin{align*}
\text{for:} && y(0,t)&= f_{0}(t), & y(1,t)&= f_{1}(t) 
\end{align*}$$

> 
> ## $$\begin{align*} \frac{\delta y}{\delta t} &= \frac{\delta^{2} y}{\delta x^{2}} & &\to &\frac{\delta v}{\delta t} &= \frac{\delta^{2} v}{\delta x^{2}} \end{align*}$$
> ## $$\begin{align*} y(0,t)&= f_{0}(t), & y(1,t)&= f_{1}(t) & &\to &v(0,t)&= 0, & v(1,t)&= 0 \end{align*}$$
> ## $$y(x,t) = v(x,t) + y_{p}(x)$$
> ##  $$\begin{align*}  y_{p} &=  f_{0} + ( f_{1} - f_{0} ) x &  y_{p} &=  f_{0} \left(1 + x\frac{f_{1}}{f_{0}} - x \right)\end{align*}$$


