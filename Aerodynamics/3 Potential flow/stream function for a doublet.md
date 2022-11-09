---
aliases: [""]
tags: []
---

## Stream function for a doublet


We can get the stream function of a doublet by placing a [[stream function for line source or sink|source and sink]] next to each other with an infinitesimally small separation. Recall the equation for a source/sink is:
$$ \psi(x,z) = \frac{Q}{2\pi} \arctan \left(\frac{z-z_{0}}{x-x_{0}}\right)  $$ So take this and get a source of strength $Q$ at $0,-B$ and then place a sink of strength $Q$ at $0 , B$:

$$\begin{align*}
\psi_{source}(x,z) &=  \frac{Q}{2\pi} \arctan \left(\frac{z }{x+B}\right) & \psi_{sink}(x,z) &=  \frac{-Q}{2\pi} \arctan \left(\frac{z }{x- B}\right)
\end{align*}$$
Then we know that [[addition of stream functions]] is possible hence:
$$\begin{align*}
\psi_{doublet}(x,z) &=  \frac{Q}{2\pi} \arctan \left(\frac{z }{x+B}\right) -\frac{Q}{2\pi} \arctan \left(\frac{z }{x- B}\right) 
\end{align*}$$
