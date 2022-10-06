---
aliases: [""]
tags: []
---

## Ansatz
This is just a fancy way of saying "guess" when working with ordinary differential equations.

For example if we take the following:

$$ a \frac{d^{2}y}{dx^{2}} + b \frac{dy}{dx} + c y = 0$$
$$\begin{align*}
\frac{d^{2}y}{dx^{2}} + \frac{b}{a} \frac{dy}{dx} + \frac{c}{a} y &= 0\\
\frac{d^{2}y}{dx^{2}} + f \frac{dy}{dx} + g y &= 0
\end{align*}$$

^9d621e

Then we call this guess $y=e^{\alpha x}$ the [[ansatz]] :
$$\begin{align*}
 \frac{d^{2}y}{dx^{2}} + f \frac{dy}{dx} + g y &= 0 & y&=e^{\alpha x}\\
 & & \frac{dy}{dx} &= \alpha e^{\alpha x}\\
 & & \frac{dy^{2}}{dx^{2}} &= \alpha^{2} e^{\alpha x}\\
\alpha^{2} e^{\alpha x} + f \alpha e^{\alpha x} + g e^{\alpha x} &= 0\\
\alpha^{2} + f \alpha + g &= 0
\end{align*}$$

This term is also used in the case where $r(x)\not\equiv 0$ (aka non [[homogeneous and nonhomogeneous differential equations|homogeneous]] cases) when we try and guess a function suitable for the [[Inhomogeneous linear second order ODEs||Inhomogeneous ODE]] the thing that becomes the [[particular integral]] can also be called an [[ansatz]] (a guess). 