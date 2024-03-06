---
aliases: ["gusts and load factor"]
tags: []
---

## Effect of gusts on load factor

### Equation

Note that the following chart and relationship ignore stall, sufficiently high gusts can stall the wing. Considering that gusts effectively change AOA, we can imagine that high gusts push the AOA into the stall region. The value of $C_{L}$ which will stall the wing is [[stalling speed|max lift coefficient]] and is also discussed in [[maximum load factor]].

> ![[Pasted image 20240302175426.png]]
> ### $$\begin{align*} n &= 1 + \frac{1}{2} \rho  \frac{UV}{W} \left(S\frac{dC_{L}}{d\alpha} +   S_{T} \frac{dC_{LT}}{d\alpha} \right) &\approx  1 + \frac{1}{2} \rho UV \frac{1}{w} \frac{dC_{L}}{d\alpha} \end{align*}$$
>> where:
>> $n=$ [[load factor]]
>> $W=$ Weight
>> $\rho=$ atmospheric density
>> $S=$  main [[Wing plan area]]
>> $S_{T}=$  tail [[Wing plan area]]
>> $C_{L}=$ lift coefficient
>> $C_{LT}=$ tail lift coefficient
>> $w=$ [[wing loading]]
>> $U=$ upward gust velocity
>> $V=$ airspeed

### Derivation

We've established that [[load factor#Circular motion|circular motion can impart load factors]], but anything that causes upward/downward acceleration will create a load factor. This is where gusts come in, a gust in the horizontal or vertical direction will effect load factor:
- In the horizontal direction, it will lead to an effective increase/decrease in airspeed, which will change lift effecting load factor
- In the vertical direction it effectively changes AOA which changes lift and hence load factor

Gusts are caused by atmospheric weather and turbulence, strongly associated with sharp condition gradients between jet streams. The consequential shaking can create problematic loading conditions which of course must be considered in aircraft structural design.

![[Pasted image 20240302173102.png]]

A simple model of the effect of gusts is addition of a vertical velocity component U. Note that $U<<V$ hence small angle approximations are made:

$$\begin{align*}
V' &= \sqrt{U^{2} + V^{2} } &&\to& V' &\approx V\\
\Delta \alpha &= \arctan \frac{U}{V} &&\to& \Delta \alpha =\theta &\approx \frac{U}{V}
\end{align*}$$

Then an expression for [[load factor]] is also easily derived, here we assume that initially $L_{total}=W$:

$$\begin{align*}
n &= \frac{L+\Delta L+P+\Delta P}{W} &&\to& n &= \frac{L+P}{W} + \frac{\Delta L+\Delta P}{W}  &&\to& n &= 1 + \frac{\Delta L+\Delta P}{W}
\end{align*}$$

Definitions of $\Delta L$ and $\Delta P$ are also trivial:

$$\begin{align*}
&&\Delta C_{L} &= \frac{dC_{L}}{d\alpha} \theta &&& \theta &= \frac{U}{V} \\
\Delta L &= \frac{1}{2} \rho S \Delta C_{L} \: V^{2} &&\to& \Delta L &= \frac{1}{2} \rho S \frac{dC_{L}}{d\alpha} \theta \: V^{2} &&\to& \Delta L &= \frac{1}{2} \rho S \frac{dC_{L}}{d\alpha} V U \\
\Delta P &= \frac{1}{2} \rho S_{T} \Delta C_{LT} \: V^{2} &&\to& \Delta P &= \frac{1}{2} \rho S_{T} \frac{dC_{LT}}{d\alpha} \theta \: V^{2} &&\to& \Delta P &= \frac{1}{2} \rho S_{T} \frac{dC_{LT}}{d\alpha} V U \\
\end{align*}$$

Combining everything:

$$\begin{align*}
n &= 1 + \frac{\Delta L+\Delta P}{W} &&\to& n &= 1 + \frac{\frac{1}{2} \rho S \frac{dC_{L}}{d\alpha} V U+ \frac{1}{2} \rho S_{T} \frac{dC_{LT}}{d\alpha} V U}{W}
 &&\to& n &= 1 + \frac{1}{2} \rho  \frac{UV}{W} \left(S\frac{dC_{L}}{d\alpha} +   S_{T} \frac{dC_{LT}}{d\alpha} \right)
\end{align*}$$

If we neglect the tail plane a simpler form can be derived:

$$\begin{align*}
n &= 1 + \frac{1}{2} \rho UV \frac{1}{W/S} \frac{dC_{L}}{d\alpha} 
\end{align*}$$

Hence, gust induced [[load factor]] is:
- Proportional to aircraft speed
- Proportional to gust speed
- Inversely proportional to [[wing loading]]

Consequently, we can see that if we want to reduce the load factor to reduce the risk to structure in heavy turbulence we can:
- Decrease speed
- Increase wing loading (may be more difficult in flight)
