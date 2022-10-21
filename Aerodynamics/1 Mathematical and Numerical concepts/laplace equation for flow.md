---
aliases: ["laplacian"]
tags: []
---

## Laplace equation for flow

If we find [[curl of a vector]] then define it in terms of [[stream function (2D)|stream functions]] we can get an equation that is solveable, assuming [[curl of a vector|vorticity]] is zero:

$$\begin{align*}
\vec {\omega} &= \left(\frac{\delta V_{y}}{\delta x} - \frac{\delta V_{x}}{\delta y} \right) \hat{e}_{z}  & V_{x} &= \frac{\delta \psi}{\delta y} & V_{y} &= -\frac{\delta \psi}{\delta x} \\ 
0 &= \frac{\delta }{\delta x} \left(-\frac{\delta \psi}{\delta x} \right)- \frac{\delta  }{\delta y}  \frac{\delta \psi}{\delta y}\\
0 &= \frac{\delta^{2} \psi}{\delta x^{2}} + \frac{\delta^{2} \psi}{\delta  y^{2}}
\end{align*}$$

> ### $$ 0 = \frac{\delta^{2} \psi}{\delta x^{2}} + \frac{\delta^{2} \psi}{\delta  y^{2}} $$ 
>> where:
>> $\psi=$ [[stream function (2D)|stream function]]
>> [[curl of a vector|vorticity]] is zero

This equation is a laplace equation hence it can be solved using numerical methods. In numpy if you have $\psi$ then this can be calculated by taking gradient twice.
