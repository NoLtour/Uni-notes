---
aliases: [""]
tags: []
---

## Solving the [[euler equations for inviscid and incompressible flow|euler equations]]

These equations are still too complex to be solved analytically so we simplify them. (yes even further)

Basically we know the following to be true from [[stream function (2D)|stream function]]s and [[mass continuity using divergence]]:
$$\begin{align*}
V_{y} &= - \frac{\delta \psi}{ \delta x } & V_{x} &= \frac{\delta \psi}{ \delta y } & \frac{\delta V_{x}}{\delta x}  + \frac{\delta V_{y}}{\delta y} &= 0 \\
\frac{\delta V_{y}}{\delta y} &= - \frac{\delta^{2} \psi}{ \delta x\delta y } & \frac{\delta V_{x}}{\delta x} &= \frac{\delta^{2} \psi}{ \delta y\delta x  }\\
& & & & \frac{\delta^{2} \psi}{ \delta x\delta y  }- \frac{\delta^{2} \psi}{ \delta y\delta x } &= 0
\end{align*}$$
