---
aliases: [""]
tags: []
---

## Time and true anomaly from non zero start values

Something to keep in mind for:
- [[getting true anomaly from time for elliptic orbits|Kepler's equation]]
- [[getting true anomaly from time for parabolic and hyperbolic orbits|Barker's equation]]
- [[getting true anomaly from time for parabolic and hyperbolic orbits|hyperbolic Kepler's equation]]

Is that these give you $\Delta t$ from $t=0$ and likewise $\Delta \theta$ from $\theta=0$. So if instead we wish to get $\Delta t$ from $t_{1}$ to $t_{2}$ then:

> ### $$\begin{align*} \\\Delta t  &= t(\theta_{2}) - t(\theta_{1})  \end{align*}$$
> ### $$\begin{align*} \Delta \theta  &= \theta(t_{2}) - t\theta(t_{1}) \\\: \end{align*}$$  

This is quite obvious, especially when considering [[time along an elliptic orbit|these previously shown concepts]]. But it's [[because you see I am stupid|useful to state]] explicitly.

It is also necessary to keep in mind that only [[getting true anomaly from time for elliptic orbits#Getting true anomaly from time for elliptic orbits (Kepler’s equation)|mean anomaly]] is linear in time, but [[orbital elements and alignment|true anomaly]] obviously isn't:


> ### $$\begin{align*} \\t(M_{1}) - t(M_{2}) &= t(M_{1} - M_{2}) \end{align*}$$ 
> ### $$\begin{align*} t(\theta_{1}) - t(\theta_{2}) &\neq t(\theta_{1} - \theta_{2}) \\\:\end{align*}$$ 

