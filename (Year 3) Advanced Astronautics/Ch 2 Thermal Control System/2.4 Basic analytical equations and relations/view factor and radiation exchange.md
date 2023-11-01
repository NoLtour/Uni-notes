---
aliases: [""]
tags: []
---

## View factor and radiation exchange

Any 2 surface's with a view of one another can emit radiation that can be absorbed by the other. We quantify this with [[view factor]] and can calculate the effects with the following:

> ### $$\begin{align*} Q_{net,1\to2}  &= A_{1} F_{1\to2} \varepsilon_{1} \sigma (T_{1}^{4} - T_{2}^{4})  \end{align*}$$
> ### $$\begin{align*} Q_{net,2\to1}  &= A_{2} F_{2\to1} \varepsilon_{2} \sigma (T_{2}^{4} - T_{1}^{4})  \end{align*}$$
> ### $$\begin{align*} A_{1} F_{1\to2} &= A_{2} F_{2\to1} \end{align*}$$
>> where:
>> $Q_{net,a\to b}=$ Heat transfer from $a$ to $b$ 
>> $F_{a\to b}=$ [[view factor]] from $a$ to $b$
>> $A=$ area of surface
>> $T=$ absolute surface temperature
>> $\sigma=$ [[Stefan-Boltzmann constant]]
>> $\varepsilon=$ [[real body emission|emittance]]

Of course in simplified models we only consider objects with significant $Q$ effects, so some bodies with especially small view factors can be ignored.

The relationship $A_{1} F_{1\to2} = A_{2} F_{2\to1}$ is known as the reciprocity rule. It makes sense if you think about it.