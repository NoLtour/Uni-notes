---
aliases: ["vortex sheet induced velocity","pressure difference and vortex sheet strength"]
tags: []
---

## Vortex sheet strength
### Modelling simplifications
As discussed in [[core principle of air foil lift]] we've got to make some simplifications, one of them is to do with the [[boundary layer]] on the foil. Basically we know that we're working with really really high Reynolds numbers, so we also know that the boundary layer will be really thin, in this case we approximate the boundary layer as a thin sheet (no thickness):
![[Pasted image 20221204153812.png]]

Now we've done this the vortex sheet strength at any point can be described using some function along a 1D line:
![[Pasted image 20221204153930.png]]
So we can now start getting somewhere useful. (this is the first of a [[it all works out in the end|LOT]] of simplification's we've got to do to get something reasonable)

### Notation

Generally we will represent the strength per unit length at some point along the vortex sheet with $\gamma$ where:

> ### $$\begin{align*} \gamma  &= f(s)  \end{align*}$$
>> where:
>> $\gamma=$ vortex sheet strength per unit length
>> $f(s)=$ some function of $s$
>> $s=$ position along the vortex sheet

Since $\gamma$ is [[circulation]] per unit length it can also be described as:

> ### $$\begin{align*} d\Gamma &=   \gamma  ds  \end{align*}$$
> ### $$\begin{align*} \Gamma &= \int^{b}_{a} \gamma(s) ds  \end{align*}$$
> ### $$ \Gamma = \int^{c}_{0} \gamma(\xi) d\xi $$
>> where:
>> $\Gamma=$ [[circulation]]
>> $a,b=$ limits of sheet
>> $\gamma=$ vortex sheet strength per unit length
>> $s=$ position along the vortex sheet
>> $c=$ chord length
>> $\xi=$ position along the chord after applying [[thin airfoil problem definition#Small camber assumption|small camber assumption]] (used during integration)

^9548d3

### Induced velocity from the vortex sheet

Let's say we know the [[vortex sheet strength]], how can we find the resulting velocity at some point $P$?
![[Pasted image 20221204153930.png]]
Well we know the equation for $\Gamma$ from [[vortex sheet strength#^9548d3]]:
$$\begin{align*}
d\Gamma &=   \gamma  ds 
\end{align*}$$
Then the equation for angular velocity some distance from a point for a single vortex is [[stream function for a vortex#^c7a30d]] which can be done for a small distance:
$$\begin{align*}
V_{\theta} &=  - \frac{\Gamma}{2\pi r} & &\to & dV_{\theta} &=  - \frac{d\Gamma}{2\pi r}
\end{align*}$$
We can then combine these equations, then by integrating you effectively sum the effects of [[vortex sheet strength]] at every point along the sheet on your point in question:
$$\begin{align*}
 dV_{\theta} &=  - \frac{\gamma  ds }{2\pi r}  &&\to & V_{\theta} &=  - \int ^{b}_{a} \frac{\gamma  }{2\pi r}ds
\end{align*}$$

### Sheet strength from cartesian velocity
We know that [[circulation]] can be found within a region by calculating the dot product of velocity and a distance vector tangential to the bound region ([[circulation#^ce6f85]]) hence we can find it for some point along the vortex sheet by using a tiny lil box:
![[Pasted image 20221204170113.png]]
For this tiny little box we calculate total circulation inside by summing up clockwise velocity times infintesimally small distance resulting in:
$$\begin{align*}
\Gamma_{\text{lil box}} &= -u_{2}ds+u_{1}ds+v_{1}dn-v_{2}dn & &\to & \Gamma_{\text{lil box}} &= (u_{1}-u_{2})ds+(v_{1}-v_{2})dn
\end{align*}$$
Then we can apply 2 thing's, firstly since this is circulation for a tiny little box it's clear that $\Gamma_{\text{lil box}}=\gamma ds$, secondly since this is a thin airfoil $dn<<<ds$ so we can approximate $dn=0$ this results in:
$$\begin{align*}
\Gamma_{\text{lil box}} &= (u_{1}-u_{2})ds+(v_{1}-v_{2})dn &\to& & \gamma ds &= (u_{1}-u_{2})ds&\to& & \gamma &= u_{1}-u_{2}
\end{align*}$$
Hence the [[vortex sheet strength]] at some point is equivalent to the difference in horizontal velocity above and below the point.

### Sheet strength and pressure
If we take [[Bernouillis equation]] we can apply it between any 2 arbitrary points since the flow is [[inviscid flow|inviscid]]:
$$\begin{align*}
p_{2} + \frac{1}{2} \rho u_{2}^{2} &=  p_{1} + \frac{1}{2} \rho u_{1}^{2} & &\to & p_{2} - p_{1}  &= \frac{1}{2} \rho (u_{1}^{2}-u_{2}^{2}) \\
&& &&  &= \frac{1}{2} \rho (u_{1}+u_{2}) (u_{1}-u_{2}) 
\end{align*}$$
From [[vortex sheet strength#Sheet strength from cartesian velocity]] we have a defenition for $(u_{1}-u_{2})$, and if you think about it $\frac{1}{2}(u_{1}+u_{2})=V_{\infty}$ hence:
$$\begin{align*}
p_{2} - p_{1} &= \rho V_{\infty} \gamma\\
\therefore\:\: \Delta p &\propto \gamma
\end{align*}$$
Hence the local sheet strength is directly proportional to the pressure difference on opposite sides of the foil! (this is a very [[yes fuck you I used pog|pog result]])