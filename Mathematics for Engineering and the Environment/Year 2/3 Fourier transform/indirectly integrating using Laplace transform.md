---
aliases: [""]
tags: []
---

## Indirectly integrating using [[Laplace transform]]

### Intro

It is possible to use [[Laplace transform standard results]], [[linearity principle for Laplace transforms]], [[first shift theorem for Laplace transform|first shift theorem]] and [[Laplace transform of a derivative]] to solve many ODE's as well as other complex equations.

### Example

> Solve $y''+y=0$ using [[Laplace transform]], given that $y(0)=0$ and $y'(0)=1$

$$\begin{align*}
\frac{d^{2}y}{dy^{2}} + y &= 0\\
\mathcal{L}\left[\frac{d^{2}y}{dy^{2}} + y\right] &= \mathcal{L}[0]\\
\mathcal{L}\left[\frac{d^{2}y}{dy^{2}} \right] + \mathcal{L}\left[ y\right] &= 0 & \mathcal{L} \left[ \frac{d^{2}f}{dx^{2}} \right] &= s^{2} \tilde{f}(s) - s f(0) - f'(0)\\
s^{2} \tilde{y}(s) - s y(0) - y'(0) + \tilde{y}(s) &= 0 \\
&& y(0)&=0 & y'(0)&=1\\
s^{2} \tilde{y}(s)  - 1 + \tilde{y}(s) &= 0\\
 \tilde{y}(s) &= \frac{1}{s^{2} + 1}
\end{align*}$$

We know using [[Laplace transform of sin]]:
$$ \mathcal{L}[\sin(ax)] = \frac{a}{s^{2}+a^{2}} $$ 
Hence:
$$\begin{align*}
\tilde{y}(s) = \mathcal{L}\left[\frac{d^{2}y}{dy^{2}} \right] &= \frac{1}{s^{2} + 1}
\end{align*}$$