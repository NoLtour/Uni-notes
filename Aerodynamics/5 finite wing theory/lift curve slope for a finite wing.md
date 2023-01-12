---
aliases: [""]
tags: []
---

## Lift curve slope for a finite wing

### Equations bit
There isn't really much proof here, a lot of it is just "[[equations pulled out of my ass|here have this equation]]" still this bit will show the important equations and variable descriptions for more explenation read the other bits (the usual).

Depending on the wing layout used, the equation used to describe $\frac{dC_{L}}{d\alpha}$ changes with aspect ratio and taper ratio, for a specific wing if these things are constant then $a_{0}$ is the same and it is possible to calculate $a$ for simular wings.  The equations below only work for cases where the craft has a single wing and of course like all other things we've calculated in this module are [[they should give you ball park accurate numbers with reality though|just approximations]] of real life:

> ### $$\begin{align*} \text{Elliptic lift distrobution:}& & a &=  \frac{a_{0}}{1+ \frac{a_{0}}{\pi A} } \\\\ \text{General high aspect ratio:}& & a&= \frac{a_{0}}{1+ \frac{a_{0}}{\pi A}( 1 + \tau) }   \\\\\text{General low aspect ratio:}& & a &= \frac{a_{0}}{\sqrt{ 1 + \left( \frac{a_{0}}{\pi A} \right)^{2}  } + \frac{a_{0}}{\pi A}}   \\\\ \text{Swept wing:}& & a &= \frac{a_{0} \cos\Lambda}{\sqrt{ 1 + \left( \frac{a_{0} \cos\Lambda}{\pi A} \right)^{2}  } + \frac{a_{0} \cos\Lambda}{\pi A}} \end{align*}$$
>> where:
>> $a= \frac{dC_{L}}{d\alpha} = C_{L\alpha} =$  lift against AOA gradient
>> $a_{0}=$ aerofoils curve slope (in ideal flow is $2\pi$)
>> $A=$ [[wing aspect ratio|aspect ratio]]
>> $\tau=$ correction factor (typically about $0 \to 0.3$)
>> $\Lambda=$ [[wing sweep]]

### Elliptic planform wing
For an elliptic planform wing with no twist we know that the $C_{l}$ is the same across the entire span, which also means that $C_{l}=C_{L}$ keeping this in mind we can take the equation for lift coefficient with AOA:
$$\begin{align*}
C_{l} &= a_{0}( \alpha - \alpha_{i} - \alpha_{L=0} )
\end{align*}$$
Then sub in the equation defining $\alpha_{i}$ from [[elliptic lift distrobution analysis]], replace $C_{l}$ with $C_{L}$ and rearrange for $C_{L}$:
$$\begin{align*}
C_{L} &= a_{0}( \alpha - \frac{C_{L}}{\pi A} - \alpha_{L=0} )\\
&...\\
C_{L} &= \frac{a_{0}}{1+ \frac{a_{0}}{\pi A} } (\alpha - \alpha_{0})
\end{align*}$$
By doing this we get an equation that can be used to plot $C_{L}$ with AOA for a finite wing:
![[Pasted image 20221222122842.png]]

So unlike the [[thin cambered airfoil analysis#Lift coefficient|lift curve slope from thin foil theory]] which was a constant we can see that due to wing tip vortecies it's actually:

$$\begin{align*}
C_{L} &= \frac{a_{0}}{1+ \frac{a_{0}}{\pi A} } (\alpha - \alpha_{0}) & &\to & \frac{dC_{L}}{d\alpha} &= \frac{a_{0}}{1+ \frac{a_{0}}{\pi A} }
\end{align*}$$

We will also refer to $\frac{dC_{L}}{d\alpha}$ as $a$ or $C_{L\alpha}$.

### General lift distrobution
#### Medium high aspect ratio wings
The maths is beyond this module but it boils down to:

$$\begin{align*}
\frac{dC_{L}}{d\alpha} =a&= \frac{a_{0}}{1+ \frac{a_{0}}{\pi A}( 1 + \tau) }  
\end{align*}$$

Here $\tau$ is known as the correction factor which is greater than one, just like what we saw in [[general lift distrobution for a finite wing]] with the [[induced drag factor]] this is a correction factor that is some measure of deviation from an elliptic lift distrobution, it can be found from $B_{n}$ using the following formula but is generally given with a wing:

$$\begin{align*}
\tau &= \frac{b}{2SB_{1}} \sum\limits^{\infty}_{n=2} nB_{n} \int^{\pi}_{0} c(\theta_{0})\: \sin (n\theta_{0}) \: d\theta_{0}
\end{align*}$$

Depending on [[taper ratio]] and [[wing aspect ratio|aspect ratio]] the slope parameter varies:
![[Pasted image 20221222124015.png]]

Not an equation for the relationship, it's imperical.

#### Low aspect ratio wings
The equation shown in [[lift curve slope for a finite wing#Medium high aspect ratio wings]] does not work for low aspect ratio's, in those cases the following equation should be used:

$$\begin{align*}
a &= \frac{a_{0}}{\sqrt{ 1 + \left( \frac{a_{0}}{\pi A} \right)^{2}  } + \frac{a_{0}}{\pi A}}
\end{align*}$$

#### Swept wings
Both the other equations don't work for [[wing sweep|swept wings]]:
![[Pasted image 20221222124828.png]]
So instead when dealing with swept wings with low aspect ratios the following equation is used:

$$\begin{align*}
a &= \frac{a_{0} \cos\Lambda}{\sqrt{ 1 + \left( \frac{a_{0} \cos\Lambda}{\pi A} \right)^{2}  } + \frac{a_{0} \cos\Lambda}{\pi A}}
\end{align*}$$
