---
aliases: [""]
tags: []
---

## Laplace equation for flow

If we find [[curl of a vector]] then define it in terms of [[stream function (2D)|stream functions]] we can get an equation that is solveable, assuming [[curl of a vector|vorticity]] is zero:

$$\begin{align*}
  \nabla \times \vec{V} = \left(\frac{\delta V_{y}}{\delta x} - \frac{\delta V_{x}}{\delta y} \right) \hat{e}_{z}   &= \frac{\delta \psi}{\delta y} & V_{y} &= -\frac{\delta \psi}{\delta x} \\ 
\frac{\delta^{2} \psi}{\delta y^{2}}  - \frac{\delta^{2} \psi}{\delta x^{2}} &= 0
\end{align*}$$

This equation only applies when there is zero [[curl of a vector|vorticity]]
