---
aliases: ["constants of motion"]
tags: []
---

## Constant of motion

### Generic description

In the context of an Ordinary Differential Equation (ODE) describing the motion of a system, a constant of motion (CoM) is a quantity that remains unchanged over time along the trajectory or orbit of the system.

In the context of orbits, one we're already familiar with would be [[specific orbital energy|orbital energy]], [[orbital semi-major axis|semi-major axis]], [[ellipse (year 2)|eccentricity]], [[perigee and apogee|periapsis]] ect.

Constants of motion are expressed as functions of position and velocity and constant along orbital paths, for them to be useful we desire independence. Formally we can demonstrate independence by showing that one constant cannot be used in isolation to find the value of another constant of motion.

We can prove a constant of motion is in fact a constant of motion by taking it's time derivative and proving it to be zero:

> ### $$\begin{align*} C(\vec{x},\vec{v})  &= \text{some constant of motion}  \end{align*}$$
> ### $$\begin{align*} \frac{d}{dt} C(\vec{x},\vec{v})  &= 0\end{align*}$$ 

### Orbital case
#### Constant
Multiple constants of motion can be used to define an orbit, here we vary another [[constant of motion]] ([[ellipse (year 2)|eccentricity]]) while keeping the [[orbital semi-major axis|semi-major axis]] the same:

![[Pasted image 20231215164821.png]]

Although different there is clearly similarity, the resulting orbits are different. Utilising [[constant of motion|constants of motion]] it also becomes more convenient to characterise orbits.

#### Dependence

The [[specific orbital moment of momentum|specific orbital angular momentum]] vector $\vec{h}$ is not independent of perigee since they have a direct relationship using state constants:

$$\begin{align*}
p &= \frac{|\vec{h}|^{2}}{\mu}
\end{align*}$$

On the other hand [[specific orbital moment of momentum|specific orbital angular momentum]] and [[ellipse (year 2)|eccentricity]] are independent, since they do not fully define eachother:

$$\begin{align*}
\vec{e} \cdot \vec{e}&= 0 & \vec{e}&= \frac{\dot{\vec{r}}\times \vec{h}}{\mu} - \frac{\vec{r}}{|\vec{r}|}
\end{align*}$$

Although they may constrain the potential states of the other, they don't fully define each other.
