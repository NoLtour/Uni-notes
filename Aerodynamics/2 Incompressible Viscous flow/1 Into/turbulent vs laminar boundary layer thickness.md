---
aliases: [""]
tags: []
---

## Turbulent vs laminar boundary layer thickness

![[Pasted image 20221019112659.png]]

(In the diagram $y$ is distance normal to foil surface)

It can be seen that the distance between the surface and the [[freestream]] is greater in the [[boundary layer|turbulent boundary layer]] compared to the [[boundary layer|laminar boundary layer]], considering that [[boundary layer thickness]] is defined as the distance needed to reach 99% of freestream velocity it can clearly be stated that turbulence boundary layers are thicker than laminar ones.

If we then look at the rate of change of perpendicular air velocity vs distance from the surface ($\frac{du}{dy}$) it can clearly be seen on the graph that near the surface the velocity gradient is much higher in the turbulent case than the laminar case, expressed mathematically:
$$ \left. \frac{du}{dy} \right|^{TBL}_{y=0} > \left. \frac{du}{dy} \right|^{LBL}_{y=0} $$

We can describe shear stress from our understanding of [[newtonian fluids#^1d39aa|Newtoniam fluids]], aka the following equation applies $\tau = \mu \frac{du}{dy} \to \frac{\tau}{\mu} = \frac{du}{dy}$ hence using the above:

$$\begin{align*}
 \left. \frac{\tau}{\mu} \right|^{TBL}_{y=0} &> \left. \frac{\tau}{\mu} \right|^{LBL}_{y=0}\\\\
 \left. \tau  \right|^{TBL}_{y=0} &> \left. \tau \right|^{LBL}_{y=0}\\
\end{align*}$$
It becomes obvious that near the wall, the turbulent boundary layer has a greater wall shear and hence higher [[skin drag|skin friction]]. (The increased difference in velocity between adjacent fluid layers in turbulent layers leads to more friction)


