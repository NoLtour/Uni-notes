---
aliases: [""]
tags: []
---

## Rankine oval

We can get a shape called a [[Rankine oval]] by placing a source and a sink in a uniform flow:
![[Pasted image 20221111113621.png]]
To simplify things it's best to place the source and sink on the x axis with equal distance $b$ from the origin.

The maths to get the [[stream function (2D)|stream function]] can be recycled from [[stream function for a doublet]]:
$$\begin{align*}
\psi_{doublet}(x,z) &=  \frac{Q}{2\pi} \left(\arctan \left(\frac{z }{x+B}\right) - \arctan \left(\frac{z }{x- B}\right)\right) & \theta_{1} &= \arctan \left(\frac{z }{x+ B}\right) & \theta_{2} &= \arctan \left(\frac{z }{x- B}\right)\\
\psi_{doublet}(x,z) &=  \frac{Q}{2\pi} \left(  \theta_{1} - \theta_{2} \right)
\end{align*}$$

Then adding the streamfunc
