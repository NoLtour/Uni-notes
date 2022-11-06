---
aliases: [""]
tags: []
---

## Stream function for line source or sink

### Derivation

![[Pasted image 20221106164053.png]]

If we take the origin at the point of the source/sink the maths becomes much cleaner. This is the same method as [[stream function for uniform flow#Derivation]] except now we will use the polar form of [[stream function (2D)|stream function]]. It is clear from observation that the angular velocity is zero, however the radial velocity is a bit more complex.
If we define the volume flow rate from the source as $\dot{q}$ then the 2D version is the area flow rate which is constant and can be defined as $Q$. It can then be observed that if you draw a circle of any radius around the origin the total area flow rate through it will be constant regardless of radius. Hence since we know the perimeter of the circle is $P=2\pi r$ and the area flow rate to be $Q=PV$ we can get:
$$\begin{align*}
Q &=  2\pi r V\\
\frac{Q}{2\pi r} &= V
\end{align*}$$
Since we know that $V$ is only acting in the radial direction, this can be written as $\frac{Q}{2\pi r} &= V_{r}$ now we just sub the identities of radial and angular veloicty into the stream function defenition in polar coordiantes and integrate:
