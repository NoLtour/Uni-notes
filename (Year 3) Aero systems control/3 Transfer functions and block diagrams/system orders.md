---
aliases:
  - first order system
  - second order system
  - system order
tags:
---

## System orders
### Description

The order of a system is equal to the highest power of derivative in the differential equation model. This corresponds to the highest power of s in the Laplace transform model.
### Examples
#### First order

$$\begin{align*}
a_{1} \frac{dc}{dt} + a_{0} c &= b_{0} r & &\to & G(S)&= \frac{b_{0}}{a_{1}s+a_{0}}
\end{align*}$$
#### Second order

$$\begin{align*}
a_{2} \frac{d^{2}c}{dt^{2}} + a_{1} \frac{dc}{dt} + a_{0} c &= b_{0} r & &\to & G(S)&= \frac{b_{0}}{a_{2}s^{2}+a_{1}s+a_{0}}
\end{align*}$$
$$\begin{align*}
a_{2} \frac{d^{2}c}{dt^{2}}   + a_{0} c &= b_{0} r & &\to & G(S)&= \frac{b_{0}}{a_{2}s^{2} +a_{0}}
\end{align*}$$