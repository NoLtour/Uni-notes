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
If we convert to polar coordinates:
$$\begin{align*}
\psi_{doublet}(\theta,r) &=  \frac{Q}{2\pi} (\theta_{1}-\theta_{2})
\end{align*}$$
If we kept $Q$ constant then as $\Delta \theta$ tends to zero the whole function would tent to zero which is not useful, so instead we are going to scale $Q$ according to the distance $B$ using the relationship: $Q2B=k$ where $k$ is some constant hence $Q=\frac{k}{2B}$:
$$\begin{align*}
\psi_{doublet}(\theta,r) &=  \frac{Q}{2\pi} (\theta_{1}-\theta_{2})\\
  &=  \frac{2BQ}{2\pi} (\theta_{1}-\theta_{2})\\
\end{align*}$$