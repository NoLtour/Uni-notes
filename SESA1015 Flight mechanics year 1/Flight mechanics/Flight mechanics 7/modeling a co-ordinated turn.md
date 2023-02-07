---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Modeling a [[co-ordinated turn]]
### Useful bit

![[calculating lift in a co-ordinated turn]]

### Proof

We will use $\phi$ for [[bank angle]].
We also know the [[centrifugal force equation]] is $F=\frac{mv^{2}}{r}$

We know that the aircraft is in equilibrium:

> Vertacle equilibrium
> $$\begin{align*}
L\cos(\phi)&=W 
\end{align*}$$

> Horizontal equilibrium
> $$\begin{align*}
L\sin(\phi) &= \frac{mV^{2}}{R}\\
&= \frac{W}{g}\frac{V^{2}}{R}
\end{align*}$$

^259f1c

> Longitudinal equilibrium
> $$\begin{align*}
T    &= D
\end{align*}$$

Knowing this we can combine them to:
$$\begin{align*}
&&L\cos(\phi)&=W & L\sin(\phi) &=\frac{W}{g}\frac{V^{2}}{R}\\
1&= \cos^{2}\theta + \sin^{2}\theta & \cos(\phi)&=\frac{W}{L} & \sin(\phi) &=\frac{W}{L}\frac{V^{2}}{gR}\\\\
&= \left(\frac{W}{L}\right)^{2} + \left(\frac{W}{L}\frac{V^{2}}{gR}\right)^{2}\\
L^{2} &= W^{2} + W^{2}\frac{V^{4}}{g^{2}R^{2}}\\
&= W^{2} \left( 1 + \left(\frac{V^{2}}{gR}\right)^{2} \right)\\
L &= W \sqrt{ 1 + \left(\frac{V^{2}}{gR}\right)^{2} }
\end{align*}$$


