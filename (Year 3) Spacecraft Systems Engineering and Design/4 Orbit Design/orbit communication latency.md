---
aliases: [""]
tags: []
---

## Orbit communication latency

### Latency

This is pretty trivial, just find the length of signal path and divide by signal speed:

> ### $$\begin{align*}  t &= \frac{R}{c}  \end{align*}$$
>> where:
>> $t=$ latency
>> $R=$ [[calculating orbital coverage|slant range]] or general case: total path length
>> $c=$ [[speed of light]]

Obviously it can be more complicated in the case of multiple hops, eg: transmitter ground -> satellite -> receiver ground:

![[Pasted image 20231201225733.png]]

Not much more complicated though lol:

$$\begin{align*}
t &= \frac{R_{1}+R_{2}}{2}
\end{align*}$$

### Orbit context

![[Pasted image 20231201225847.png]]

Of course higher orbits have higher latency:
- GEO satellites generally often act as relays for constant transmissions, which makes sense since the latency would make 2 way communication painful
- LEO is where mega constellations exist, here latency is small enough to work for things like internet

Clearly latency is a consideration for satellite communication ability.
