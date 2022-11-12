---
aliases: [""]
tags: []
---

## Pressure coefficients for a stream function in a potential flow

### Theory

It's quite easy just take the equation for [[pressure coefficient when there is no freestream|pressure coefficient]] and then use the same sort of method we did for finding [[defining the geometry of an object in a flow#Finding thickness|thickness of a object in freestream]] from it's streamfunction, but for the pressure coefficient:

![[pressure coefficient when there is no freestream#^6ace8a]]

### Example

> [[Flow past a circular cylinder]], find the pressure coefficients at the maximum and minimum points of velocity on the surface of cylinder with radius $R=\sqrt{\frac{k}{2\pi U_{\infty}}}$

$$ \psi(r,\theta) = U_{\infty}r\sin(\theta)\left(1- \frac{R^{2}}{r^{2}}\right) $$
$$\begin{align*}
V_{r}&=  \frac{1}{r} \frac{\delta\psi}{\delta\theta} & V_{\theta} &= -\frac{\delta\psi}{\delta r} \\
&= \frac{1}{r} V_{\infty}\cos\theta \left(1- \frac{R^{2}}{r^{2}}\right) & &=0\:\: (\text{online cal})
\end{align*}$$
