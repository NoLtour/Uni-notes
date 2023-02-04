---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Proof of second moment of area of a rectangle
![[Pasted image 20211115093700.png]]

We know from the [[second moment of area]] that: $I_{zz}=\int\int y^{2} \cdot dydz$

So:

$$\begin{align*}
   I_{zz} &= \int\int y^{2} \cdot dydz\\
&= \int^{b/2}_{-b/2} \left(  \int^{d/2}_{-d/2} y^{2} \cdot dy    \right)\cdot dz\\
&= \int^{b/2}_{-b/2} \left( \left [ \frac{y^{3}}{3} \right ]^{\frac{d}{2}}_\frac{-d}{2} \right)\cdot dz\\
&= \int^{b/2}_{-b/2} \left( \frac{(\frac{d}{2})^{3}}{3} - \frac{-(\frac{d}{2})^{3}}{3} \right)\cdot dz\\
&= \int^{b/2}_{-b/2} \left( \frac{d^{3}}{12} \right)\cdot dz\\
&= \frac{d^{3}}{12} \int^{b/2}_{-b/2} \left( 1 \right)\cdot dz\\
&= \frac{bd^{3}}{12}
\end{align*}$$ 

$$ \therefore I_{zz} = \frac{bd^{3}}{12} $$