---
aliases: [""]
tags: []
---

## Practical post mission disposal in LEO

### Lifetime targets

If we simulate the progression of space pollution in LEO over a while we can get the following:

![[Pasted image 20231109161717.png]]

It can be seen that if we do nothing (BAU) it becomes a real shitshow quite quickly, on the other hand the difference between immediate, 25 and 50 year disposal is not that significant. This is why for a while we've accepted 25 years as a reasonable disposal time.

A 25-50 year time means you can utilise [[space drag]] instead of lots of fuel, reducing deorbit cost.

That being said with the emergence of mega constellations international guidelines are trending towards 5 years/immediate de-orbiting.

### Cost

If we want to adjust an orbit enough to get it to decay to death within 25 years we need a certain amount of $\Delta V$:

![[Pasted image 20231109162152.png]]

In the extreme cases $~2000\:km$ it starts to become more practical to shift to a graveyard orbit simular to GEO instead of burning up.

### Approximating lifetime

The orbital lifetime is influenced by countless factors... but we do have some equations which (very) approximately predict LEO orbit time:

> ### $$\begin{align*} t_{L} &= \frac{H\tau}{2000 \pi a^{2} \rho \beta} & \beta &= \frac{C_{D}A}{m} & \tau &= 2\pi \sqrt{\frac{a^{3}}{\mu}}   \end{align*}$$
>> where:
>> $t_{L}=$ lifetime (seconds??)
>> $H=$ altitude
>> $\tau=$ [[keplers laws of orbital motion|orbital period]]
>> $a=$ [[orbital semi-major axis|semi-major axis]]
>> $\rho$ satellite density??
>> $\beta$ 1/ballistic coefficient
>> $C_{D}=$ solar pressure constant
>> $A=$ sat cross sectional area
>> $m=$ satellite mass
>> $\mu=GM=$ [[universal constant of gravitation|gravitational constant]] times Earths mass

In real life we use simulation software such as: STELA, STK or DAS.

