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
\rho\Delta y \Delta  x  \left(  \frac{\delta u}{\delta x}  + \frac{\delta v}{\delta y}  \right) &=
\end{align*}$$

Since we've taken density as constant we know there cannot be a change in the mass of the [[control volume]], hence $\frac{dm}{dt}=0$ and so:
$$  \frac{\delta u}{\delta x}  + \frac{\delta v}{\delta y}  = 0 $$

This equation looks similar to something we did recently [[hhhhuuuuuuuuuuuuuuuuummmmmmmmmmmmmmmm|:think:]], since $v$ and $u$ are just the components of the velocity vector in their respective directions it's a form of the [[divergence operator]] applied to velocity:

> ### $$ \frac{\delta u}{\delta x}  + \frac{\delta v}{\delta y} = \frac{\delta V_{x}}{\delta x}  + \frac{\delta V_{y}}{\delta y} = 0 = \nabla \cdot \vec{V} $$ 
>> where:
>> mass is conserved, density is constant.
>> $\vec{V}=$  [[velocity and speed|velocity]] vector
>> $u=V_{x}=$ velocity $x$ component
>> $v=V_{y}=$ velocity $y$ component
>> made use of [[divergence operator#^0f35d6]]

^31084a

So if we look back at what each value of the [[divergence operator]] means according to it's definition:
![[divergence operator#^951754]]
It can be seen that equaling zero means conservation, which is inline with the original assumption of mass conservation; hence if we have a vector field where at some point the [[divergence operator]] is not zero we know that mass isn't conserved, this means there exists a "source" or "drain" which is unrealistic.
