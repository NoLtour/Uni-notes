---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How do we deal with
## Capacitors in AC


### Theory
It's the usual, take the equation for [[capacitors#^e6fedd|capacitors]] then the equation for [[complex numbers for representing AC|representing AC with complex numbers]]:
$$\begin{align*}
V(t) &= \frac{1}{C} \int^{t}_{t_{0}} I(t) \cdot dt + V(t_{0}) & I &= I_{p}\cos(\omega t + \phi ) \\
 &=  \frac{1}{C} \int^{t}_{t_{0}} I_{p}\cos(\omega t + \phi ) \cdot dt + V(t_{0}) \\
 && &at\:t=-\phi,V=0\\
&=  \frac{I_{p}}{C \omega} \sin(\omega t + \phi ) \\
&
\end{align*}$$