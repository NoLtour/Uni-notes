---
aliases: ["parabolic PDEs"]
tags: []
---

## Parabolic partial differential equations

### Intro

Parabolic PDEs are usually associated with diffusion problems. Parabolic PDEs can be described as situations where information is propagated instantly (an infinite speed), this is often done for situations where such an approximation does not have significant effect on the output.
An example would be the heat equation:
$$\begin{align*}
\frac{\delta u}{\delta y }  &= k \frac{\delta^{2}u}{\delta x^{2}}
\end{align*}$$
When plotted it can be seen that at the instant $t\neq 0$ all values on the domain are effected instantly, hence no time delay:
![[Pasted image 20221103215447.png]]

In situations that occur on a microscopic scale the rate of information transfer can often be accurately approximated as instantaneous, hence it is common to use [[parabolic partial differential equations|parabolic PDEs]] in such situations.

### Boundary conditions

![[Pasted image 20221104094309.png]]

$$\begin{align*}
\frac{\delta u}{\delta y }  &= k \frac{\delta^{2}u}{\delta x^{2}}
\end{align*}$$

If you look at the heat equation above you can see that is is defined using 1 double derivative and a normal derivative, hence to fix these equations we require 3 boundary conditions:
- 2 Boundary conditions at the ends of the domain $x=0 ,\:x=L$. These boundary values might be of the form $u(0,t)=0$ or the derivative $\frac{d}{dx}u(0,t)=0$.
- 1 initial condition ($t=0$) here you'll probably have some value or the derivative eg: $u(x,0)=0$, $\frac{d}{dt}u(x,0)=0$.

Notice how these boundary conditions defined for a specific value of the independent variable works for all values of the other independents, hence why on the graph they can be visualised as strait lines.