---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you derive the
## Venturi meter equation

![[Pasted image 20220214221351.png]]

Basically slap a bit of [[Bernouillis equation]], some [[conservation of mass in flow]] and a bit of [[pressure (hydrostatics)]] and...

$$\begin{align*}
P_{Atm} &= P_{1} - \rho g h_{1} & P_{Atm} &= P_{2} - \rho g h_{2} & A_{1} v_{1} &= A_{2} v_{2} & \frac{1}{2} \rho v_{1}^{2} + P_{1} &= \frac{1}{2} \rho v_{2}^{2} + P_{2}\\
P_{2} - \rho g h_{2} &= P_{1} - \rho g h_{1} & & & \frac{A_{1}}{A_{2}} v_{1} &= v_{2} &  P_{1} - P_{2} &= \frac{1}{2} \rho v_{2}^{2} - \frac{1}{2} \rho v_{1}^{2}\\
\rho g h_{1} - \rho g h_{2} &= P_{1} - P_{2} & & & \frac{A_{1}^{2}}{A_{2}^{2}} v_{1}^{2} &= v_{2}^{2} &  P_{1} - P_{2} &= \frac{1}{2} \rho (v_{2}^{2} - v_{1}^{2})\\
\rho g \Delta h &= \frac{1}{2} \rho (v_{2}^{2} - v_{1}^{2})\\
2 g \Delta h &= \frac{A_{1}^{2}}{A_{2}^{2}} v_{1}^{2} - v_{1}^{2}\\
2 g \Delta h &= \left(\frac{A_{1}^{2}}{A_{2}^{2}} - 1\right)v_{1}^{2}\\
 \frac{2 g \Delta h A_{2}^{2}}{A_{1}^{2} - A_{2}^{2}}&=v_{1}^{2}\\
A_{2} \sqrt \frac{2 g \Delta h  }{A_{1}^{2} - A_{2}^{2}}&=v_{1}\\
\end{align*}$$

This thing is based, because if you know the cross sectional area of the pipe it allows you to find the speed of the fluid without anything complex... simplicity is very useful!

As you can see, creative application of the stuff covered so far leads to neat shit... which is the goal of an engineer to make "neat shit" (which is the [[of course I would put some shit meme here|technical term]] of course).