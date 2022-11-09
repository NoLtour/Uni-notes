---
aliases: [""]
tags: []
---

## Stream function for a doublet


We can get the stream function of a doublet by placing a [[stream function for line source or sink|source and sink]] next to each other with an infinitesimally small separation. Recall the equation for a source/sink is:
$$ \psi(x,z) = \frac{Q}{2\pi} \arctan \left(\frac{z-z_{0}}{x-x_{0}}\right)  $$ So take this and get a source of strength $Q$ at $z_{0},x_{0}$ and then place a sink of strength $Q$ at $z_{0}+\Delta z,x_{0} + \Delta x$. Then we know that [[addition of stream functions]] is possible hence:

$$\begin{align*}
\psi_{source}(x,z) &=  \frac{Q}{2\pi} \arctan \left(\frac{z-z_{0}}{x-x_{0}}\right) & \psi_{sink}(x,z) &=  \frac{-Q}{2\pi} \arctan \left(\frac{z-z_{0}-\Delta z}{x-x_{0}-\Delta x}\right)
\end{align*}$$

$$\begin{align*}
\psi_{doublet}(x,z) &=  \frac{Q}{2\pi} \arctan \left(\frac{z-z_{0}}{x-x_{0}}\right)+\frac{-Q}{2\pi} \arctan \left(\frac{z-z_{0}-\Delta z}{x-x_{0}-\Delta x}\right)\\
&=  \frac{Q}{2\pi} \arctan \left(\frac{z-z_{0}}{x-x_{0}}\right)+\frac{-Q}{2\pi} \arctan \left(\frac{z-z_{0}-\Delta z}{x-x_{0}-\Delta x}\right)\\
\end{align*}$$
