---
aliases: ["supersonic expansion fan","expansion fan","turning angle","angle of the first Mach line","angle of the last Mach line","Prandtl-Meyer function"]
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

^3a6820

![[Pasted image 20231026104633.png]]

Here we can see the definitions of the angles:
- $\mu_{1}=$ angle of the first Mach line
- $\mu_{2}=$  angle of the last Mach line
- $\theta=$  turning angle (just like [[oblique shock angles|turning angle]] for [[oblique shocks]])

### Calculating

The following is derived from theory and shows you the angle changes required to expand a flow to a target Mach. Note that $\nu$ can also be found in the isentropic flow table.

> ### $$\begin{align*} \nu(M) &= \sqrt{ \frac{\gamma+1}{\gamma-1} } arctan\sqrt{ \frac{\gamma-1}{\gamma+1} (M^{2} - 1) } - \arctan\sqrt{M^{2} - 1}   \end{align*}$$
>> where:
>> $\nu(M)=$ the angle divergence (in radians) required to accelerate a flow from Mach 1 to target Mach $M$
>> $M=$ input Mach number 
>
>
> ### $$\begin{align*} \theta &= \nu(M_{2}) - \nu(M_{1})   \end{align*}$$
>> where:
>> $\nu=$ [[Prandtl–Meyer expansion fan|Prandtl-Meyer function]]
>> $M_{1}=$ the initial Mach number
>> $M_{2}=$ the final Mach number
>> $\theta=$ the angle divergence required to expand the flow from $M_{1}\to M_{2}$

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
&& && && \tan \mu &=  \frac{1}{\sqrt{M^{2} - 1}}\\
V d\theta \sin \mu&=   dV \cos \mu & &\to & d\theta \tan \mu&=   \frac{dV}{V} & &\to &   \frac{ d\theta}{\sqrt{M^{2} - 1}} &=   \frac{dV}{V}
\end{align*}$$

^77e61b

Now to get $V$ in terms of $M$, we will first use [[What's the product rule|product rule]]:

$$\begin{align*}
& & \text{product}&\text{ rule}\\
V &= M\:a && \to & dV &= M\:da + a\:dM\\
&& && \frac{dV}{M\:a} &= \frac{M\:da}{M\:a} + \frac{a\:dM}{M\:a} & &\to & \frac{dV}{V} &= \frac{  da}{ a} + \frac{ dM}{M }
\end{align*}$$

Subbing back the equation we got previously:

$$\begin{align*}
\frac{dV}{V} &= \frac{  da}{ a} + \frac{ dM}{M } & &\to & \frac{ d\theta}{\sqrt{M^{2} - 1}} &= \frac{  da}{ a} + \frac{ dM}{M } 
\end{align*}$$

I'm not going to detail the next part since it'll take too long, using "magic" you can combine the above equation with $\frac{a_{0}}{a^{2}} = 1 - \frac{\gamma-1}{2} M^{2}$ to get:

$$\begin{align*}
d\theta &= \frac{\sqrt{M^{2} - 1}}{1 + \frac{\gamma-1}{2} M^{2}} \frac{dM}{M} 
\end{align*}$$

Which when plotted produces:

![[Pasted image 20231027113416.png]]

Note that the $y$ axis is $d\theta/dM$ and $x$ is [[Mach number]].

What this tells us is that the ratio of $\theta$ change to Mach change is greatest around Mach 1.6 and lowest at Mach 1 or infinity.

In reality [[Prandtl–Meyer expansion fan]]s act in response to curvature, so $\theta$ is our input. Considering that $dM$ represents Mach increase, as is the nature of expansion in the supersonic domain, this function describes the rate of flow acceleration around a (convex) curved surface by it's current Mach number. 

Let's invert the function so it describes $dM/d\theta$, which means taking 1/f(x):

![[Pasted image 20231027114909.png]]

Let's consider these implications using a diverging nozzle (with constant $\frac{d\theta}{dx}$) with entry at $M=1$:
1) Initially the rate of Mach increase will be unbelievably high
2) The rate of Mach increase decreases rapidly, at Mach 1.01 it is $0.15\:Ma/\degree$  till at $M\approx 1.6$ it's $0.035\:Ma/\degree$
3) This tends back upward as you deviate away from Mach 1.6, though at a slower rate

#### Prandtl-Meyer function

Ok back to the equation, through further math magic and integration it becomes possible to get:

$$\begin{align*}
\int^{\theta'}_{0} d\theta &= \int^{M'}_{1} \frac{\sqrt{M^{2}-1}}{1+ \frac{\gamma-1}{2} M^{2}} \frac{d\theta}{M}\\
&\downarrow\\
\nu(M) &= \sqrt{ \frac{\gamma+1}{\gamma-1} } arctan\sqrt{ \frac{\gamma-1}{\gamma+1} (M^{2} - 1) } - \arctan\sqrt{M^{2} - 1}
\end{align*}$$

(This equation is known as the Prandtl-Meyer function)

Looking at the limit's this equation represents the angle change required to get a flow from Mach 1 to target Mach $M$. 

It is also given in the isentropic flow table, at each $M$:

![[Pasted image 20231027121534.png]]

This also means that if we want to find the angle change corresponding to change from $M_{1}$ to $M_{2}$ we can actually just use that function:

$$\begin{align*}
\theta &= \nu(M_{2}) - \nu(M_{1})
\end{align*}$$