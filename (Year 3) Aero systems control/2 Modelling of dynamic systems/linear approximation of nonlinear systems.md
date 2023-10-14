---
aliases: [""]
tags: []
---

## Linear approximation of nonlinear systems

We've done this a tone for over the past couple of years, but here it'll be formalised a bit. (Now if this isn't ringing any bells... please just leave the course)

![[Pasted image 20231014184100.png]]

It is normally possible to represent a nonlinear system using a linear (or small-signal) approximation. In this example if the variation of $x$ about $𝑥_{0}$ is small enough, the nonlinear curve can be approximated by its tangent at point $0$.

Defining:
- $\Delta x = x-x_{0}$
- $\Delta y = y-y_{0}$

We can write the linearized model of $f(x)$ as:
$$\begin{align*}
\Delta y &= \left. \left(\frac{df}{dx}\right) \right|_{x=x_{0}} \Delta x
\end{align*}$$

Every time you've used a small angle approximation this is exactly what you where doing. 

[[Taylor series]] is actually just this ^ taken to it's extreme! 
