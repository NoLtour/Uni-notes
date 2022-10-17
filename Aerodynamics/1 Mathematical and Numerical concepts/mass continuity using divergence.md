---
aliases: [""]
tags: []
---

## Mass continuity using [[divergence operator|divergence]]

If we start by considering a [[control volume]], then we can calculate the rate of mass change in a control volume by finding:

$$ \sum\limits ( \text{ velocty in } \times \text{ density in } \times \text{area}) - \sum\limits ( \text{ velocty out } \times \text{ density out } \times \text{area}) = \frac{dm}{dt} $$

Here we are doing it over a 2D area:
![[Pasted image 20221017144618.png]]

If we take $\rho$ as a constant, then plug the numbers into a single equation:
$$\begin{align*}
\Delta y \left( \rho \left(u+ \frac{\delta u}{\delta x} \Delta x\right) - \rho u \right) + \Delta x \left( \rho \left(v+ \frac{\delta v}{\delta y} \Delta y\right) - \rho v \right) &= \frac{dm}{dt} \\
\Delta y \left( \rho  \frac{\delta u}{\delta x} \Delta x \right) + \Delta x \left( \rho  \frac{\delta v}{\delta y} \Delta  y \right) &=\\
\Delta y \Delta  x \rho \left(  \frac{\delta u}{\delta x}   \frac{\delta v}{\delta y}  \right) &=
\end{align*}$$
