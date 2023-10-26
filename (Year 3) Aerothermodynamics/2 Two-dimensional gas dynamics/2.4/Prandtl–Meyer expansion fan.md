---
aliases: ["supersonic expansion fan","expansion fan","turning angle","angle of the first Mach line","angle of the last Mach line"]
tags: []
---

## Prandtl–Meyer expansion fan

### Intro

![[Expansion_fan.png]]

So far all phenomina have been compressive shocks, but of course there needs to be something nature can use to deal with expansion. This is that mechanism. 

Unlike shocks which create a single discrete change across some incredible thin boundary, expansion fans modify the flow over a drawn out region gradually modifying flow properties.

A direct consequence of this is the [[isentropic process|isentropic]] assumption:
- Instead of a single shock, expansion fans use "infinite, infinitesimally small 'shocks'" (one way to picture it)
- Look back at the [[normal shock properties equations#Entropy|entropy change across normal shock]], the larger the Mach change, the "exponentially" larger the entropy increase
- By taking infinitesimally small Mach changes, the total entropy increase is negligible (in an idealised system)
- Hence we can assume [[isentropic process|isentropic expansion]] for Mach fans

Something else to note is that this is a supersonic expansion, and hence it will result in an increase in speed so $M_{2}>M_{1}$. Just like what was observed in [[converging diverging nozzles]].

Since this process occurs in the event of expansion, it applies when dealing with convex corners.

#### Terms

![[Pasted image 20231026104633.png]]

Here we can see the definitions of the angles:
- $\mu_{1}=$ angle of the first Mach line
- $\mu_{2}=$  angle of the last Mach line
- $\theta=$  turning angle (just like [[oblique shock angles|turning angle]] for [[oblique shocks]])

### Calculating

#### Proof

To start with we'll have to create a model for one of the individual infinitesimally small expansion boundaries, then of course integrate across the region.

![[Pasted image 20231026104457.png]]

Since the fundemental mechanism at play are exactly what used for [[oblique shocks]], we can reuse some of the maths from there. We can get the Mach line angle from the [[oblique shock chart]], where $d\theta\approx0$. Which is [[oblique shock chart#^3557f5|this equation!]]
$$\begin{align*}
  \mu &=  \arctan \frac{1}{\sqrt{x^{2} + 1}} & &\to &  \tan \mu &=  \frac{1}{\sqrt{x^{2} + 1}}
\end{align*}$$

Using the value of $\mu$ we can get the tangential velocity components, then we can consider the fact that $V_{t1}=V_{t2}$ to get some useful stuff:

$$\begin{align*}
V_{1}\cos(\mu) &= V_{t1} & & & V_{2}\cos(\mu+d\theta) &= V_{t2}\\
V_{1}\cos(\mu) &= V_{t1} & & & (V_{1}+dV)\cos(\mu+d\theta) &= V_{t2}\\
&& V_{t1} &= V_{t2}\\
&& V_{1}\cos(\mu) &= (V_{1}+dV)\cos(\mu+d\theta)\\
\end{align*}$$

Making use of trigonometric identies we can expand out, then make use of small angle approximations to simplify:

$$\begin{align*}
& & \cos(A+B) &= \cos A \cos B - \sin A \sin B \\ 
V_{1}\cos(\mu) &= (V_{1}+dV)\cos(\mu+d\theta) & &\to & V_{1}\cos(\mu) &= (V_{1}+dV)[ \cos \mu \cos d\theta - \sin \mu \sin d\theta ]\\
&& &&   &= (V_{1}+dV)[ \cos \mu - d\theta \sin \mu ]\\
&& &&   &= V_{1} \cos \mu - V_{1} d\theta \sin \mu  + dV \cos \mu - dV d\theta \sin \mu\\
&& && V_{1} \cos \mu - V_{1} \cos \mu  &= - V_{1} d\theta \sin \mu  + dV \cos \mu\\
&& && V_{1} d\theta \sin \mu&=   dV \cos \mu\\
\end{align*}$$

A bit more rearanging can get it into a more useful form:

$$\begin{align*}
&& && && \tan \mu &=  \frac{1}{\sqrt{x^{2} + 1}}\\
V d\theta \sin \mu&=   dV \cos \mu & &\to & d\theta \tan \mu&=   \frac{dV}{V} & &\to &   \frac{ d\theta}{\sqrt{x^{2} + 1}} &=   \frac{dV}{V}
\end{align*}$$

Now to get $V$ in terms of $M$, we will first use [[What's the product rule|product rule]]:

$$\begin{align*}
& & \text{product}&\text{ rule}\\
V &= M\:a && \to & dV &= M\:da + a\:dM\\
&& && \frac{dV}{M\:a} &= \frac{M\:da}{M\:a} + \frac{a\:dM}{M\:a} & &\to & \frac{dV}{V} &= \frac{  da}{ a} + \frac{ dM}{M }
\end{align*}$$

Subbing back the equation we got previously:

$$\begin{align*}
\frac{dV}{V} &= \frac{  da}{ a} + \frac{ dM}{M } & &\to & \frac{ d\theta}{\sqrt{x^{2} + 1}} &= \frac{  da}{ a} + \frac{ dM}{M } 
\end{align*}$$
